from flask import Flask, request, jsonify
from flask.helpers import make_response
import psycopg2
import json
import os
import datetime

dbname=os.environ.get("AVISOS_DB","postgres")
dburl=os.environ.get("AVISOS_DB_URL","localhost")
porta=os.environ.get("AVISOS_DB_PORTA","5432")
dbuser=os.environ.get("AVISOS_DB_USER","postgres")
dbpsw=os.environ.get("AVISOS_DB_PSW","password")

db = psycopg2.connect(database=dbname,
        user=dbuser,
        password=dbpsw,
        host=dburl,
        port=porta
    )

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/api/', methods=['GET'])
def get_all():
    avisos = []
    sql = """
        select * from aviso;
    """
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
    app.run(host= '0.0.0.0', port=8080)
