#!/bin/bash
docker run -d --rm \
    --name backend-python \
    -p 8443:8443 \
    -e AVISOS_DB_PSW="$PGPASSWORD" \
    --link some-postgres:some-postgres backend_python:1.0.0

