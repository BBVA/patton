.. image:: https://badge.fury.io/py/patton-server.svg
    :target: https://badge.fury.io/py/patton-server

.. image:: https://img.shields.io/badge/style-flat-green.svg?longCache=true&style=flat&logo=docker
    :target: https://hub.docker.com/r/bbvalabs/patton-server/

.. image:: https://img.shields.io/badge/style-flat-green.svg?longCache=true&style=flat&logo=docker
    :target: https://hub.docker.com/r/bbvalabs/patton-cli/

Patton - The vulnerability knowledge store
==========================================

+----------------+-----------------------------------------------+
|Current version | 1.0.2                                         |
+----------------+-----------------------------------------------+
|Project site    | https://github.com/bbva/patton                |
+----------------+-----------------------------------------------+
|Issues          | https://github.com/bbva/patton/issues/        |
+----------------+-----------------------------------------------+
|Documentation   | https://patton.readthedocs.org/               |
+----------------+-----------------------------------------------+
|Python versions | 3.6 or above                                  |
+----------------+-----------------------------------------------+

What's Patton
=============

Patton is a set of tools for helping admins and security auditors to search for vulnerabilities in software components. Currrently it has 2 main modules:

- Patton-server: A service that builds a knowledge database about vulnerability information (CVEs). This information is then linked with product details (CPE) to finally allow to ask in a very clever way.
- Patton-cli: A powerful command line client that allows to extract and check for vulnerabilities in your systems in a many different ways.

Documentation
=============

You can find Patton's documentation at `Read the Docs <https://patton.readthedocs.org/>`_.

Contributing
============

Any collaboration is welcome!

There're many tasks to do. You can check the `Issues <https://github.com/bbva/patton/issues/>`_ and send us a Pull Request.

Also you can read the `TODO <https://github.com/bbva/patton/blob/master/TODO.md>`_ file.

License
=======

This project is distributed under `Apache 2 license <https://github.com/bbva/patton/blob/master/LICENSE>`_
