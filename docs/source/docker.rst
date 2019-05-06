Running using Docker
====================

Both, `patton-server <https://hub.docker.com/r/bbvalabs/patton-server>`_ and `patton-cli <https://hub.docker.com/r/bbvalabs/patton-cli>`_, are available as a docker image so you can pull and run from a container.

patton-cli quick run with Docker
-----------------------------------

.. code-block:: console

    > docker run --rm bbvalabs/patton-cli -h

Will show up patton-cli commandline help.

.. code-block:: console

    > docker run --rm bbvalabs/patton-cli --patton-host 192.168.4.2

Will connect to patton-server at 192.168.4.2 and ask for CVEs on django:1.9.

The docker container for pattin-cli supports the same parameters as the binary.

patton-server quick run with Docker
-----------------------------------

.. code-block:: console

    > docker run --rm -p 9000:9000 bbvalabs/patton-server start-server

Will run patton-server with this defaults:

- Listen por 9000
- Database:
  - host: 127.0.0.1
  - port: 5432
  - name: patton
  - user: postgres
  - password: postgres
- Maximum concurrent connections: 512

.. code-block:: console

    > docker run --rm bbvalabs/patton-server update-database -w https://somewhere.in/time

Will run patton-server database updater with the following defaults and invoking the URL https://somewhere.in/time after finishing the update:

- Database:
  - host: 127.0.0.1
  - port: 5432
  - name: patton
  - user: postgres
  - password: postgres

Customizing execution of paton-server container
-----------------------------------------------

The default entrypoint of the docker image is a wrapper script that manages and prepare the environment, it supports the following commands:
- help . Shows the usage message and exit.
- start-server. Start the patton-server.
- update-database. Launches the updater process. it supports the following options:
  - -c, --cron-expr. The cron expresion to program executions of the update process. If not present the update process runs once.
  - -w --webhook. The URL to use as webhook.

patton-server docker image uses the following environment variables to customize execution:

- WORKERS (default: 1. Do not change this value if you're not really sure you're doing!)
- BACKLOG (default: 512)
- LISTEN_PORT (default: 9000)
- PATTON_DEBUG (default: 0)
- POSTGRES_HOST (default: 127.0.0.1)
- POSTGRES_PORT (default: 5432)
- POSTGRES_DB (default: patton)
- POSTGRES_USER (default: postgres)
- POSTGRES_PASSWORD (default: postgres)

.. code-block:: console

    > docker run --rm -e BACKLOG=512 -e LISTEN_PORT=8080 -e POSTGRES_USER=my_user -p 8080:8080 bbvalabs/patton-server start-server

paton-server deployment with docker-compose
-------------------------------------------

In order to ease deployment some files are provided in the compose directory to allow users to star a server from scratch using docker-compose. These are the files and their purpose:
- db-credentials.env Contains the environmental variable values needed to authenticate against a database server.
- patton-config.env Contains the environmental variable values to configure the paton-server instance.
- docker-compose.yml Starts a container for the server and another one for the updater, programmed to execute every 4 hours. POSTGRES_HOST environment variable must be provided in order to provide the database to the containers.
- docker-compose-database.yml Starts a container with a postgresql database and configures the patton-server containers to connect to this instance.

In order to start a fully containerized environment run:

.. code-block:: console

    > docker-compose -f docker-compose.yml -f docker-compose-database.yml up

If you want to run against an existing database server run:

.. code-block:: console

    > docker-compose -f docker-compose.yml -f docker-compose-database.yml -e POSTGRES_HOST=somehost up
