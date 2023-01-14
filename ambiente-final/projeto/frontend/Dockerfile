# Buld: sudo docker build -t frontend:1.0.0 .

FROM nginx

# Copia nosso template de configuracao:

RUN mkdir -p /etc/nginx/templates
COPY templates/default.conf.template /etc/nginx/templates
RUN rm -f /etc/nginx/conf.d/default.conf

# Copia os arquivos SSL:

RUN mkdir -p /etc/nginx/ssl
COPY templates/server.crt /etc/nginx/ssl
COPY templates/server.key /etc/nginx/ssl

# Copia os arquivos dist:

ADD dist/quadrofront /usr/share/nginx/html/

RUN ls -la /usr/share/nginx/html/

# Prepara as variaveis de ambiente para
# configurar o template

ENV NGINX_SERVER_NAME="localhost"
ENV NGINX_BACKEND_URL="https://backend-python:8443"

# Para subir: 
# sudo docker run -d --name frontend -p 443:443 --link backend-java:backend-java frontend:1.0.0
