#!/bin/bash
docker build -t mypostgres:1.0.0 .
docker run --rm \
    --name some-postgres \
    -p 5432:5432 \
    -e POSTGRES_PASSWORD="$PGPASSWORD" \
    -v /home/ederson/Documentos/Aprendendo/senior-cleuton-udemy/ambiente-final/postgresql/data:/var/lib/postgresql/data/ \
    -d mypostgres:1.0.0
