from flask import Flask, request, jsonify
from flask.helpers import make_response
import psycopg2
import json
import os
import datetime

# Para JWT: 
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from cryptography.hazmat.primitives import serialization
import datetime

dbname=os.environ.get("AVISOS_DB","postgres")
dburl=os.environ.get("AVISOS_DB_URL","localhost")
porta=os.environ.get("AVISOS_DB_PORTA","5432")
dbuser=os.environ.get("AVISOS_DB_USER","postgres")
dbpsw=os.environ.get("AVISOS_DB_PSW","password")
PRIVKEY=os.environ.get("AVISOS_PRK","/home/cleuton/Documentos/projetos/bootcamp-dev-sr/s5/seguranca/private.pgp")
PRK_KEYPHRASE=os.environ.get("AVISOS_KEYPHRASE","bananateste")
CERT_FILE=os.environ.get("AVISOS_CERT_SSL","/home/cleuton/Documentos/projetos/bootcamp-dev-sr/s5/seguranca/cert.pem")
KEY_FILE=os.environ.get("AVISOS_SSL_KEY","/home/cleuton/Documentos/projetos/bootcamp-dev-sr/s5/seguranca/key.pem")

# Variáveis para implementar JWT:

PRIVATEKEY_PATH_JWT=os.environ.get("AVISOS_JWT_PRIVATE_KEY_PATH","/home/cleuton/Documentos/projetos/bootcamp-dev-sr/s5/backend_python/ssh/cleuton")
PUBLICKEY_PATH_JWT=os.environ.get("AVISOS_JWT_PUBLIC_KEY_PATH","/home/cleuton/Documentos/projetos/bootcamp-dev-sr/s5/backend_python/ssh/cleuton.pub")
PRIVATEKEY_JWT_PASSPHRASE=os.environ.get("AVISOS_JWT_PRIVATE_KEY_PASSPHRASE","teste")
VALIDADE_TOKEN_JWT_SEGUNDOS=os.environ.get("AVISOS_JWT_VALIDADE_SEGUNDOS","60")

# Tempo de espera entre tentativas de login falhas:

TEMPO_LOGIN=os.environ.get("AVISOS_TEMPO_LOGIN_SEGUNDOS","30")
TENTATIVAS_LOGIN=os.environ.get("AVISOS_TENTATIVAS_LOGIN","3")


db = psycopg2.connect(database=dbname,
        user=dbuser,
        password=dbpsw,
        host=dburl,
        port=porta,
        sslmode='require'
    )

file = open(PRIVKEY,mode='r')
PRIVATE_KEY_STRING = file.read()
file.close()

# Variáveis e funções para JWT:

def loadKeys():
    private_key = open(PRIVATEKEY_PATH_JWT, 'r').read()
    prKey = serialization.load_ssh_private_key(private_key.encode(), password=str.encode(PRIVATEKEY_JWT_PASSPHRASE))
    public_key = open(PUBLICKEY_PATH_JWT, 'r').read()
    pubKey = serialization.load_ssh_public_key(public_key.encode())
    return pubKey,prKey

PUBLICKEY_JWT, PRIVATEKEY_JWT = loadKeys()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Configurações da App Flask para JWT: 

app.config["JWT_PRIVATE_KEY"] = PRIVATEKEY_JWT
app.config["JWT_PUBLIC_KEY"] = PUBLICKEY_JWT
app.config['JWT_ALGORITHM'] = 'RS256'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(seconds=int(VALIDADE_TOKEN_JWT_SEGUNDOS))
jwt = JWTManager(app)

# Protecao contra ataque de forca bruta
# Melhor seria usar um REDIS, mas isto é eficaz
suspended_login = {}

def suspend(user):
    global suspended_login
    if user not in suspended_login:
        suspended_login[user] = {
            "tentativas" : 0,
            "suspenso" : False,
            "time" : datetime.datetime.now()
        }
        print(f"Marcando login {user} {suspended_login}")
    else:
        if not suspended_login[user]["suspenso"]:
            print(f"Nova tentativa de login de {user}")
            suspended_login[user]["tentativas"] += 1
            if suspended_login[user]["tentativas"] >= int(TENTATIVAS_LOGIN):
                print(f"Suspendendo login {user}")
                suspended_login[user]["suspenso"] = True
                suspended_login[user]["time"] = datetime.datetime.now()
        else:
            print(f"Atualizando bloqueio de login {user}")
            suspended_login[user]["time"] = datetime.datetime.now()

def check_suspended(user):
    global suspended_login
    if user in suspended_login:
        if suspended_login[user]["suspenso"]:
            agora = datetime.datetime.now()
            inicio = suspended_login[user]["time"]
            diff = agora - inicio
            print(f"Diferenca {diff.total_seconds():.9f} tempo {int(TEMPO_LOGIN)}")
            if diff.total_seconds() >= int(TEMPO_LOGIN):
                del suspended_login[user]
                print(f"Login {user} agora liberado")
                return False
            else:
                print(f"Login {user} ainda suspenso, e por mais tempo")
                suspended_login[user]["time"] = datetime.datetime.now()
                return True
        else:
            del suspended_login[user]

    return False


def decriptar():
    sql = f"""
    SELECT id, 
        pgp_pub_decrypt(titulo, keys.privkey,'{PRK_KEYPHRASE}') As titulo,
        pgp_pub_decrypt(resumo, keys.privkey,'{PRK_KEYPHRASE}') As resumo,
        pgp_pub_decrypt(thumb, keys.privkey,'{PRK_KEYPHRASE}') As thumb,
        pgp_pub_decrypt(imagem, keys.privkey,'{PRK_KEYPHRASE}') As imagem,
        pgp_pub_decrypt(texto, keys.privkey,'{PRK_KEYPHRASE}') As texto,
        pgp_pub_decrypt(data, keys.privkey,'{PRK_KEYPHRASE}') As data
         
    FROM aviso 
        CROSS JOIN
            (SELECT dearmor('{PRIVATE_KEY_STRING}') As privkey) As keys;

    """
    return sql

# Esta rota é para o usuário se autenticar.
# Se o token expirar, ele terá que logar novamente.
# Você pode estabeler mecanismo de refresh automático do token.

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "fulano" or password != "senhafulano":
        suspend(username)
        return jsonify({"msg": "Username ou senha incorretos"}), 401
    else:
        if check_suspended(username):
            return jsonify({"msg": "Login ainda suspenso"}), 401

    access_token = create_access_token(identity=username)

    # O default é retornar o token no corpo do request. 
    # O cliente tem que enviar um header "Authorization: Bearer <token>"

    return jsonify(access_token=access_token)

@app.route('/api/', methods=['GET'])
@jwt_required()
def get_all():
    avisos = []
    sql = decriptar()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        for registro in cursor:
            saida = {
                "id" : registro[0],
                "titulo" : registro[1],
                "resumo" : registro[2],
                "thumb" : registro[3],
                "imagem" : registro[4],
                "texto" : registro[5],
                "data" : registro[6]
            }
            avisos.append(saida)
    except psycopg2.ProgrammingError as e:
        print(f"ERRO: {e.pgerror}")
    dictAvisos = {
        "_embedded" : { "api" : avisos }
    }
    return jsonify(dictAvisos)





if __name__ == '__main__':
    context = (CERT_FILE,KEY_FILE) #certificate and key files
    app.run(host= '0.0.0.0', port=8080,ssl_context=context)
