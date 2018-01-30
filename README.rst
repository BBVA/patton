Patton - The vulnerability knowledge store
==========================================

+----------------+-----------------------------------------------+
|Current version | 0.0.3                                         |
+----------------+-----------------------------------------------+
|Project site    | https://github.com/bbva/patton-server         |
+----------------+-----------------------------------------------+
|Issues          | https://github.com/bbva/patton-server/issues/ |
+----------------+-----------------------------------------------+
|Documentation   | https://patton-server.readthedocs.org/        |
+----------------+-----------------------------------------------+
|Python versions | 3.6 or above                                  |
+----------------+-----------------------------------------------+

What's Patton Server
====================

Patton server is project that store the vulnerability information (CVEs) and link it with product details (CPE) and allow to ask in a very clever way.

For example:

Finding library vulnerabilities
-------------------------------

- Given a software library in raw format, i.e: django
- And a version in a possible version, i.e: 1.2

Patton can find all the Product Identification for **Django** and their public vulnerabilities.

Finding software from raw text
------------------------------

- Given a HTTP server banner, i.e: "Apache 2.2-ubuntu2 +PHP Mod"

Patton can find, with a very exact way, vulnerabilities for Apache and the specific version

How to use Patton server?
=========================

Patton serve has a REST API. You can check if in different ways:

- Using raw curl / wget / [YOUR FAVORITE HTTP CLIENT]
- Using the Postman collection you can find in this repo (named patton_server.postman.json)
- **Using Patton-cli (https://github.com/bbva/patton-cli/**: We recommend to use this way. Patton-cli is a powerful client for Patton server that allow to extract and check vulnerabilities for your systems in a many different ways.

Documentation
=============

Go to documentation site: https://patton-server.readthedocs.org/

Contributing
============

Any collaboration is welcome!

There're many tasks to do.You can check the `Issues <https://github.com/bbva/patton-server/issues/>`_ and send us a Pull Request.

Also you can read the `TODO <https://github.com/bbva/patton-server/blob/master/TODO.md>`_ file.

License
=======

This project is distributed under `Apache 2 license <https://github.com/bbva/patton-server/blob/master/LICENSE>`_
