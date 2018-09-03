Patton - The vulnerability knowledge store
==========================================

+----------------+-----------------------------------------------+
|Current version | 0.0.4                                         |
+----------------+-----------------------------------------------+
|Project site    | https://github.com/bbva/patton-server         |
+----------------+-----------------------------------------------+
|Issues          | https://github.com/bbva/patton-server/issues/ |
+----------------+-----------------------------------------------+
|Documentation   | https://patton-server.readthedocs.org/        |
+----------------+-----------------------------------------------+
|Python versions | 3.6 or above                                  |
+----------------+-----------------------------------------------+

How it works
============

patton-server is a small service that preprocess CVEs and CPEs from NIST and perform intelligent queries to a postgres database. You can consume the service via api, cli or with the postman in this repository.

.. image:: patton-diagram.png
   :width: 80 %
   :scale: 50 %
   :alt: diagram
   :align: center

You can see the Demo video for a quick start:

.. image:: http://img.youtube.com/vi/g5pROiIQUzk/0.jpg
   :target: http://www.youtube.com/watch?v=g5pROiIQUzk
   :width: 80 %
   :scale: 50 %
   :alt: diagram
   :align: center

What's Patton Server
====================

Patton Server can resolve any library name to their CPE. Then returns the associated CVEs for this CPE.

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
