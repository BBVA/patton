#!/bin/sh

if [ -z ${WORKERS} ]; then
    export WORKERS=1
fi
if [ -z ${BACKLOG} ]; then
    export BACKLOG=512
fi
if [ -z ${LISTEN_PORT} ]; then
    export LISTEN_PORT=9000
fi
if [ -z ${MAX_CONCURRENT_DB_QUERIES} ]; then
    export MAX_CONCURRENT_DB_QUERIES=300
fi
if [ -z ${POSTGRES_HOST} ]; then
    export POSTGRES_HOST=127.0.0.1
fi
if [ -z ${POSTGRES_USER} ]; then
    export POSTGRES_USER=postgres
fi

if [ -z ${POSTGRES_PORT} ]; then
    export POSTGRES_PORT=5432
fi

if [ -z ${POSTGRES_PASSWORD} ]; then
    export POSTGRES_PASSWORD=postgres
fi

if [ -z ${POSTGRES_DB} ]; then
    export POSTGRES_DB=patton
fi

if [ -z ${PATTON_DEBUG} ]; then
    export PATTON_DEBUG=0
fi

export CONNECTION_STRING=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

# Wait until DB is available
echo "[*] Waiting por PostgresDB"
/usr/local/bin/wait-for-it.sh ${POSTGRES_HOST}:${POSTGRES_PORT}

# Populate DB
echo "[*] Population Patton DB"
patton-server -C ${CONNECTION_STRING} -v init-db

# Run the service
echo "[*] Launching Patton service"
exec gosu 1000:1 patton-server -C ${CONNECTION_STRING} \
                  serve \
                  --listen 0.0.0.0 \
                  --port ${LISTEN_PORT} \
                  --workers ${WORKERS} \
                  --backlog ${BACKLOG}
