#!/bin/sh

WORKERS=1
BACKLOG=512
MAX_CONCURRENT_DB_QUERIES=300
LISTEN_PORT=9000
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=patton

CONNECTION_STRING=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}


exec gosu 1000:1 patton-server -C ${CONNECTION_STRING} \
                  serve \
                  --listen 0.0.0.0 \
                  --port ${LISTEN_PORT} \
                  --workers ${WORKERS} \
                  --backlog ${BACKLOG}
