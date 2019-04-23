.. image:: https://badge.fury.io/py/patton-server.svg
    :target: https://badge.fury.io/py/patton-server

.. image:: https://img.shields.io/badge/style-flat-green.svg?longCache=true&style=flat&logo=docker
    :target: https://hub.docker.com/r/bbvalabs/patton-server/

.. image:: https://img.shields.io/badge/style-flat-green.svg?longCache=true&style=flat&logo=docker
    :target: https://hub.docker.com/r/bbvalabs/patton-cli/

Patton - The vulnerability knowledge store
==========================================

+----------------+-----------------------------------------------+
|Current version | 1.0.3                                         |
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

Patton is a set of tools that allow Admins and security auditors to search for vulnerabilities on software components.

At this moment it contains two modules:
  * `Patton-server <https://github.com/bbva/patton//tree/master/server>`_: Resolves any library name to their CPE and then returns the associated CVEs for this CPE.
  * `Patton-cli <https://github.com/bbva/patton//tree/master/client>`_: Is a powerful client for Patton-server that allows you to extract and check vulnerabilities for your systems in a many different ways.

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
