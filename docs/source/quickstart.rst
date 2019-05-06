Quick start
===========

This document will give you a brief introduction to Patton and how you can use it.

What's Patton
-------------

Patton can resolve any library name to their CPE and then returns the associated CVEs list for that library.

How it works
++++++++++++

Patton provides a small service (patton-server) that resolves CVEs and CPEs from NIST and perform intelligent queries to a postgres database. You can consume the service via api, a command-line client or using the Postman collection provided in this repository.

.. image:: _static/patton-diagram.png
   :alt: Patton diagram
   :align: center

A Demo video is available for a quick start:

.. image:: http://img.youtube.com/vi/g5pROiIQUzk/0.jpg
   :target: http://www.youtube.com/watch?v=g5pROiIQUzk
   :width: 80 %
   :scale: 50 %
   :alt: Patton demo
   :align: center

Finding library vulnerabilities
+++++++++++++++++++++++++++++++

Given a software library in raw format, i.e: django, and a version, i.e: 1.2, Patton can find all the Product Identification for that version of the library and then extract all their public known vulnerabilities.

How to use Patton server?
+++++++++++++++++++++++++

Patton server exposes a REST API that you can use in three different ways:

- Using raw curl / wget / [YOUR FAVORITE HTTP CLIENT] to make requests to the patton-server.
- Using `Patton-cli <https://github.com/bbva/patton/>`_: Patton-cli is a powerful command-line client for Patton-server that allows you to extract and check for vulnerabilities in your systems in a many different ways, this is the recommend way to access the server.
- Using the provided `Postman collection <_static/Patton.postman_collection.json>`_ . **Postman 2.1 is needed to open the collection**.

Example using curl:

.. code-block:: console

    > curl -X POST -d '{"source": "auto", "libraries" : [{"library": "Microsoft IIS","version": "7"}]' --header "Content-Type: application/json" http://my-patton-service.com

What's the different with other projects?
-----------------------------------------

There're other projects, like `CVE Search <https://github.com/cve-search/cve-search>`_ that also allows you to store and search for CVE information. What's the difference then with Patton?

Clever matching
+++++++++++++++

Unlike CVE-Search (and other projects) Patton doesn't need a CPE as its input, instead it is able to **deduce the CPE**.

**Patton's purpose is to allow you to use simpler and clever queries** deducing from them the information needed to make the search. For example: from a library name and its version, patton-server can deduce the related CPEs and, from them, recover the associated CVEs.

Be updated
----------

Patton can alert you when new vulnerabilities are released, as you can configure a server webhook that Patton-server will invoke ONLY when new vulnerabilities are published.
