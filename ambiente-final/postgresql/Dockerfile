# Build: sudo docker build -t mypostgres:1.0.0 .

FROM postgres

# Vamos adicionar os arquivos para SSL:

RUN mkdir /var/temp
COPY server.crt /var/temp
COPY server.key /var/temp
COPY postgresql.conf /var/temp
RUN chown -R 999:999 /var/temp/

# Agora vamos adicionar o script de pos inicializacao
# Alem de reiniciar o servico, ele cria o banco 
# e a tabela encriptada

COPY postinit.sh /docker-entrypoint-initdb.d/
COPY criabanco-pgcrypto.sql /docker-entrypoint-initdb.d/

# Rode como: 
# sudo docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d mypostgres:1.0.0
# Subir um pgadmin:
# sudo docker run -p 8088:80 --link some-postgres:postgres \
# -e "PGADMIN_DEFAULT_EMAIL=seuemail@seuprovedor.com" \
# -e "PGADMIN_DEFAULT_PASSWORD=password" \
# -d dpage/pgadmin4