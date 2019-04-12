WebHook
=======

What's Patton-Server WebHook
----------------------------

Each time patton-server updates its database from new CVEs feeds, you can set a webhook where Patton-Server will call when the process is finished.

Patton-server will only send to the WebHook the new CVEs found since last check.

This is useful if you want to notify to some other system with news CVE and you don't want to write the code to parse feeds, downloads, etc.

Set WebHook in Patton-Server
----------------------------

To setup the webhook you only need to specify the remote end-point URL:

.. code-block:: console

    > patton-server update-db -W https://myservice.com/patton-web-hook/


WebHook format
--------------

The webhook sends the information to the provided URL uning a **POST** request with a **JSON** payload.

This is an example of the **JSON** payload sent by the webhook:

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
