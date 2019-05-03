#!/bin/bash

function usage () {
  echo -e "\nusage: ${1#./} COMMAND [OPTIONS]"
  echo -e "\nCommands:"
  echo "  help             Show this help and exit"
  echo "  start-server      Start patton-server"
  echo "  update-database  Launch database update"
  echo -e "\nOptions:"
  echo "  -c, --cron-expr  A cron expression to program update executions. If not provided only one run is executed"
  echo "  -w, --webhook    URL to be called after the update process finish"
}

cron_expr=""
webhook=""

# Get command to execute
command=$1
if [ ${command} == 'help' ]; then
  usage $0
  exit 0
elif [ ${command} != 'start-server' -a ${command} != 'update-database' ]; then
  usage $0
  exit 1
fi

shift

# Parse commandline parameters
while [ "$1" != "" ]; do
  case $1
    in
      -c) cron_expr="$2" ; shift 2;;
      --cron-expr=*) cron_expr="${1#*=}" ; shift;;
      -w) webhook="-W $2" ; shift 2;;
      --webhook=*) webhook="-W ${1#*=}" ; shift;;
      *) echo mira lo que viene ---"$i"---
  esac
done

echo "$cron_expr $webhook"
# Get env variables and build connection string
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

# Launch patton-server
if [ ${command} == 'update-database' ]; then
  if [ -n ${cron_expr} ]; then
    # Create job
    echo "[*] Building crontab"
    echo "${cron_expr} patton-server -C ${CONNECTION_STRING} -v update-db ${webhook}" > /etc/crontabs/update-patton
    chmod +x /etc/crontabs/update-patton
    crontab /etc/crontabs/update-patton

    # Run in foreground
    touch /var/log/cron.log
    echo "[*] Launching cron tasks"
    exec crond -n
  else
    exec patton-server -C ${CONNECTION_STRING} -v update-db ${webhook}
  fi
elif [ ${command} == 'start-server' ]; then
  # Populate DB if neccessary
  echo "[*] Population Patton DB"
  patton-server -C ${CONNECTION_STRING} -v init-db

  exec patton-server -C ${CONNECTION_STRING} \
                    serve \
                    --listen 0.0.0.0 \
                    --port ${LISTEN_PORT} \
                    --workers ${WORKERS} \
                    --backlog ${BACKLOG}
fi
