Overview
========

This document will give you a brief introduction to Patton and how you can use it.

What's Patton
-------------

Patton can resolve any library name to their CPE and then returns the associated CVEs list for that library.

How does it works
-----------------

Patton provides a small service (patton-server) that resolves CVEs and CPEs from NIST and perform intelligent queries to a postgres database. You can consume the service via api, a command-line client or using the Postman collection provided in this repository.

.. image:: /_static/images/patton-diagram.png
   :alt: Patton diagram
   :align: center

A Demo video is available for a quick start:

.. image:: http://img.youtube.com/vi/g5pROiIQUzk/0.jpg
   :target: http://www.youtube.com/watch?v=g5pROiIQUzk
   :width: 80 %
   :scale: 50 %
   :alt: Patton demo
   :align: center

What's the different with other projects?
-----------------------------------------

There're other projects, like `CVE Search <https://github.com/cve-search/cve-search>`_ that also allows you to store and search for CVE information. What's the difference then with Patton?

Clever matching
+++++++++++++++

Unlike CVE-Search (and other projects) Patton doesn't need a CPE as its input, instead it is able to **deduce the CPE**.

**Patton's purpose is to allow you to use simpler and clever queries** deducing from them the information needed to make the search. For example: from a library name and its version, patton-server can deduce the related CPEs and, from them, recover the associated CVEs.

Be updated
----------

Patton can alert you when new vulnerabilities are released, as you can configure a server webhook that patton-server will invoke ONLY when new vulnerabilities are published.
