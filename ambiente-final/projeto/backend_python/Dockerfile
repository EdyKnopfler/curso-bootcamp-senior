# Build: sudo docker build -t backend_python:1.0.0 .

FROM python

# Criando uma pasta e copiando o código-fonte:

RUN mkdir /opt/backend_python
ADD ./ /opt/backend_python/ 

RUN ls -la /opt/backend_python

# Novo usuario e permissoes:

RUN useradd -ms /bin/bash backenduser && \
    echo 'backenduser:&jsgcksj3408moas%@@#1' | chpasswd && \
    chown -R backenduser /opt/backend_python 

# Instalando dependencias python:
# Inclui o gunicorn que eh recomendado para producao:

RUN pip install -r /opt/backend_python/requirements.txt

# Variaveis de ambiente: 

ENV AVISOS_DB="postgres"
ENV AVISOS_DB_URL="some-postgres"
ENV AVISOS_DB_PORTA="5432"
ENV AVISOS_DB_USER="postgres"
ENV AVISOS_PRK="/opt/backend_python/seguranca/private.pgp"
ENV AVISOS_KEYPHRASE="bananateste"
ENV AVISOS_CERT_SSL="/opt/backend_python/seguranca/cert.pem"

### Atencao: Retire a passphrase da chave primaria do SSL:
# openssl pkey -in key.pem -out key.pem
## Senao ele ficara pedindo que seja digitada e vai dar erro!!!!

ENV AVISOS_SSL_KEY="/opt/backend_python/seguranca/key.pem"

# Variáveis para implementar JWT:

ENV AVISOS_JWT_PRIVATE_KEY_PATH="/opt/backend_python/ssh/cleuton"
ENV AVISOS_JWT_PUBLIC_KEY_PATH="/opt/backend_python/ssh/cleuton.pub"
ENV AVISOS_JWT_PRIVATE_KEY_PASSPHRASE="teste"
ENV AVISOS_JWT_VALIDADE_SEGUNDOS="60"

# Tempo de espera entre tentativas de login falhas:

ENV AVISOS_TEMPO_LOGIN_SEGUNDOS="30"
ENV AVISOS_TENTATIVAS_LOGIN="3"

# Comando para executar dentro do conteiner:

USER backenduser
WORKDIR /opt/backend_python

# Estou usando gunicorn que eh production-grade:
# Atencao que mudamos a porta para 8443 padrao
# para aplicacoes que servem https:

CMD gunicorn --bind 0.0.0.0:8443 --certfile=/opt/backend_python/seguranca/cert.pem --keyfile=/opt/backend_python/seguranca/key.pem servidor:app

# Rode como: 
# sudo docker run -d --name backend-python -p 8443:8443 --link some-postgres:some-postgres backend_python:1.0.0
