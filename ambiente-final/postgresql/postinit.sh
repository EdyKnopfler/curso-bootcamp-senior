#!/bin/bash
set -e
cp /var/temp/* /var/lib/postgresql/data/
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    SELECT pg_reload_conf();
EOSQL