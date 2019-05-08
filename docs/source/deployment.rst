Using docker-compose
====================

In order to ease deployment some files are provided in the compose directory to allow users to star a server from scratch using docker-compose. These are the files and their purpose:

- db-credentials.env Contains the environmental variable values needed to authenticate against a database server.
- patton-config.env Contains the environmental variable values to configure the paton-server instance.
- docker-compose.yml Starts a container for the server and another one for the updater, programmed to execute every 4 hours. POSTGRES_HOST environment variable must be provided in order to provide the database to the containers.
- docker-compose-database.yml Starts a container with a postgresql database and configures the patton-server containers to connect to this instance.

Deploy with **internal** database
=================================

In order to start a fully containerized environment run:

.. code-block:: console

    > docker-compose -f docker-compose.yml -f docker-compose-database.yml up

Deploy with **external** database
=================================

If you want to run against an existing database server run:

.. code-block:: console

    > docker-compose -f docker-compose.yml -f docker-compose-database.yml -e POSTGRES_HOST=somehost up
