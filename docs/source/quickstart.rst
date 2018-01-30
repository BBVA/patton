Quick start
===========

This document is a quick introduction for use Patton Service

First of run Patton Server
++++++++++++++++++++++++++

1 - Install Patton Server
-------------------------

.. code-block:: bash

  > python3.6 -m pip install patton-server

2 - Install PostgresSQL
-----------------------

Patton uses a PostgresSQL database. The most easy way to install is using Docker:

.. code-block:: bash

  > docker run -d -p 5432:5432 -e POSTGRES_USER=patton -e POSTGRES_DB=patton postgres

3 - Initialize database
-----------------------

Third step we need to populate database:

.. code-block:: bash

  > patton-server init-db


.. note::

  This process could take some time. I our benchmarks, time should round between 4 - 6 minutes


Running Patton Server
+++++++++++++++++++++

After install and populate Patton database, we can start Patton server:

.. code-block:: bash

  > patton-server serve


Updating Patton database
++++++++++++++++++++++++

Patton borrow the vulnerability information from NIST, updating their database with new information form them.

Usually NIST releases new vulnerability information around 2 hours (following the NIST guidelines). Then, choice an update time, no less than 2 hours. 1 or 2 times per day should be a reasonable balance.

To update Patton server you only need to execute:

.. code-block:: bash

   > patton-server update-db

Optionally, you can choose a webhook to call with the news CVEs, when the updating process was done:


.. code-block:: bash

   > patton-server update-db -W http://mysite.com/


