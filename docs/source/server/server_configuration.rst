Server Configuration
====================

Server options
--------------

By default patton-Server will listen at **port 8000**.

To check for all the options and their defaults that patton-Server provides you can type:

.. code-block:: console

    > patton-server serve -h

    usage: patton-server serve [-h] [-l LISTEN] [-p PORT] [-w WORKERS]
                           [-b BACKLOG] [-d] [-M MAXIMUM_CONCURRENT]

    optional arguments:
      -h, --help            show this help message and exit
      -l LISTEN, --listen LISTEN
                            listen address. Default: 127.0.0.1
      -p PORT, --port PORT  listen port for service. Default: 8000
      -w WORKERS, --workers WORKERS
                            workers. Default: 1
      -b BACKLOG, --backlog BACKLOG
                            maximum concurrent connections
      -d, --debug           enable debug. Default: disabled
      -M MAXIMUM_CONCURRENT, --maximum-concurrent MAXIMUM_CONCURRENT
                            maximum packages to analyze (DON'T TOUCH THIS OPTION!)


Customizing Postgres Connection
-------------------------------

patton-server needs to connect to a Postgres Server in which its database lives. This connection is configured by providing a connection string.

The default connection string is: ``postgres://username:password@localhost:5432/dbname``

You can specify a custom connection string using ``-C`` parameter in patton-server:

.. code-block:: console

    > patton-server -C postgres://myuser:mypassword@10.0.0.1:5432/MyDatabase serve

.. note::

    Be careful, the database must exist in PostgresSQL before patton-server starts.

.. note::

    Be aware to put the ``-C`` option in the correct place. This option must be set **before** the``serve`` command.
