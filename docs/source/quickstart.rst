Quick start
===========

This document is a quick introduction to Patton Server.

What's Patton Server
--------------------

Patton Server can resolve any library name to their CPE. Then returns the associated CVEs for this CPE.

Finding library vulnerabilities
-------------------------------

- Given a software library in raw format, i.e: django
- And a version in a possible version, i.e: 1.2

Patton can find all the Product Identification for **Django** and their public vulnerabilities.

How to use Patton server?
-------------------------

Patton serve has a REST API. You can check if in different ways:

- Using raw curl / wget / [YOUR FAVORITE HTTP CLIENT]
- Using the `Postman collection <https://github.com/BBVA/patton-server/blob/master/Patton.postman_collection.json>`_. **Postman 2.1 is needed to open collection**.
- Using `Patton-cli <https://github.com/bbva/patton-cli/>`_: We recommend to use this way. Patton-cli is a powerful client for Patton server that allow to extract and check vulnerabilities for your systems in a many different ways.

Example using curl:

.. code-block:: console

    > curl -X POST -d '{"source": "auto", "libraries" : [{"library": "Microsoft IIS","version": "7"}]' --header "Content-Type: application/json" http://my-patton-service.com


What's the different with other projects?
-----------------------------------------

There're other project, like `CVE Search <https://github.com/cve-search/cve-search>`_ that also stores CVE information. What's is the difference then with Patton?

Clever matching
+++++++++++++++

Differing with the approach of CVE-Search (and other projects) Patton don't need a CPE as input. Patton **deduces the CPE**.

**The actually Patton purpose is build clever queries** and deduce information. Por example: from a library name and their version, can deduce the related CPEs and associated CVEs.

Be updated
----------

Patton can alert you when new vulnerabilities are released:

You can configure the Patton web-hook and it will alert you with ONLY with new vulnerabilities published.
