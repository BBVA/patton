Running using Docker
====================

Both, patton-server and patton-cli, are available as a docker image so you can pull and run from a container.

Patton-server quick run with Docker
-----------------------------------

.. code-block:: console

    > docker run --rm -p 9000:9000 bbvalabs/patton-server

It will run with this defaults:

- Listen por 9000
- Database:
  - host: 127.0.0.1
  - port: 5432
  - user: postgres
  - password: postgres
  - database name: patton
- Maximum concurrent connections: 512

Patton server Docker has these configuration environment vars:

- WORKERS (default: 1. Do not change this value if you're not really sure you're doing!)
- BACKLOG (default: 512)
- LISTEN_PORT (default: 9000)
- POSTGRES_HOST (default: 127.0.0.1)
- POSTGRES_PORT (default: 5432)
- POSTGRES_USER (default: postgres)
- POSTGRES_PASSWORD (default: postgres)
- POSTGRES_DB (default: patton)

.. code-block:: console

    > docker run --rm -e BACKLOG=512 -e LISTEN_PORT=8080 -e POSTGRES_USER=my_user -p 8080:8080 bbvalabs/patton-server


Patton-cli quick run with Docker
-----------------------------------

.. code-block:: console

    > docker run --rm -p 9000:9000 bbvalabs/patton-cli django:1.9 -o report.json
