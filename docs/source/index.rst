Welcome to Patton's documentation!
==================================

+----------------+-----------------------------------------------+
|Current version | .. include:: ../../server/VERSION                                              |
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

Contents
========

.. toctree::
   :maxdepth: 2

   quickstart
   install
   server_configuration
   api
   cli
   webhook
   docker
   fails
