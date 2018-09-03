WebHook
=======

What's Patton-Server WebHook
----------------------------

Each time patton server update database for new CVEs feeds you can set a webhook where Patton-Server will call when process was finished.

Patton-Server only will send to the WebHook the new CVEs found from last check.

This is useful if you want to notify to some other system with news CVE and you don't want to write the code to parse feeds, downloads, etc.

Set WebHook in Patton-Server
----------------------------

To setup the webhook you only need to specify the remote end-point URL:

.. code-block:: console

    > patton-server update-db -W https://myservice.com/patton-web-hook/


.. note::

    Be careful with the database. Database must be created into PostgresSQL before Patton starts.

.. note::

    Be aware to put the ``-C`` option in the correct place. This option must be set **before** ``serve`` command.

WebHook format
--------------

The format send the information to the webhook is via HTTP and **JSON** format, using **POST** method.

This is an example of the JSON format sent to the webhook:

.. code-block:: json


    [
        {
            "CVE-2016-4800":
            [
                "cpe:2.3:a:eclipse:jetty:9.3.0:*:*:*:*:*:*:*",
                "cpe:2.3:a:eclipse:jetty:9.3.0:m0:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.0:m1:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.0:m2:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.0:rc0:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.0:rc1:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.1:*:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.2:*:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.3:*:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.4:*:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.4:rc0:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.4:rc1:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.5:*:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.6:*:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.7:*:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.7:rc0:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.7:rc1:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.8:*:*:*:*:*:*:*",
                 "cpe:2.3:a:eclipse:jetty:9.3.8:rc0:*:*:*:*:*:*"
            ]
        }
    ]