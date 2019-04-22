Patton - Vulnerability Matching
===============================


+----------------+--------------------------------------------+
|Current version | 0.0.1                                      |
+----------------+--------------------------------------------+
|Project site    | https://github.com/bbva/patton-cli         |
+----------------+--------------------------------------------+
|Issues          | https://github.com/bbva/patton-cli/issues/ |
+----------------+--------------------------------------------+
|Python versions | 3.6 or above                               |
+----------------+--------------------------------------------+

What's Patton-cli?
==================

P

Usage examples
==============

Getting Vulnerabilities from Ubuntu-like system
-----------------------------------------------

.. code-block:: bash

   > dpkg -l | awk '{print $2":"$3}' | sed 's/:amd64//g' |  sed '1,/.*:/s/.*://' | patton-cli check-dependencies

**TODO: Improve this kind of tests**

  * Analyze a Python file dependencies:
    - From stdin:
       > cat requirements.txt | {patton_cli} check-dependencies
    - From file:
       > {patton_cli} -i requirements.txt check-dependencies

  * Analyze dependencies using cli arguments:
     > {patton_cli} check-dependencies django:1.2 flask:1.1.0

  * Change display modes:
     - Table display mode:
        > {patton_cli} -D table check-dependencies django:1.2 flask:1.1.0
     - JSON display mode:
        > {patton_cli} -D json check-dependencies django:1.2 flask:1.1.0
     - RAW display mode:
        > {patton_cli} -D raw check-dependencies django:1.2 flask:1.1.0
     - CVS display mode:
        > {patton_cli} -D csv check-dependencies django:1.2 flask:1.1.0

  * Save results in a file:
     - Output file in JSON format:
        > {patton_cli} -o output.json check-dependencies django:1.2
     - Output file in CVS format:
        > {patton_cli} -o output.csv check-dependencies django:1.2
     - Output file in Table format:
        > {patton_cli} -o output.raw check-dependencies django:1.2

  * Combine Patton-cli with other tools:
     - When nmap finish, it results will be used as input for Patton-cli
     > nmap -n localhost | {patton_cli} check-banners

     - Running nmap concurrently with Patton-cli. While nmap is running, Patton will store results in a file
     > nmap -n localhost | tee {patton_cli} -c -o nmapResults.json check-banners


Getting vulnerabilities from a Python dependencies file
-------------------------------------------------------

You can choose one of these modes:

.. code-block:: bash

   > cat requirements.txt | patton-cli check-dependencies
    +--------------------------------------------+------------------+
    | CPE                                        | CVEs             |
    +--------------------------------------------+------------------+
    | cpe:/a:djangoproject:django:1.2.3          | CVE-2011-0698    |
    |                                            | CVE-2011-0696    |
    |                                            | CVE-2011-4140    |
    |                                            | CVE-2011-4136    |

    ...

    | ------------------------------------------ | ---------------- |
    | cpe:/a:flask-oidc_project:flask-oidc:0.1.2 | CVE-2016-1000001 |
    +--------------------------------------------+------------------+

or:


.. code-block:: bash

   > patton-cli -i requirements-dev.txt check-dependencies
    +--------------------------------------------+------------------+
    | CPE                                        | CVEs             |
    +--------------------------------------------+------------------+
    | cpe:/a:djangoproject:django:1.2.3          | CVE-2011-0698    |
    |                                            | CVE-2011-0696    |
    |                                            | CVE-2011-4140    |
    |                                            | CVE-2011-4136    |

    ...

    | ------------------------------------------ | ---------------- |
    | cpe:/a:flask-oidc_project:flask-oidc:0.1.2 | CVE-2016-1000001 |
    +--------------------------------------------+------------------+

Getting Vulnerabilities from brew (OS X)
----------------------------------------

Obtaining vulnerabilities from your local dependencies:

.. code-block:: bash

  > brew list --versions | patton-cli check-dependencies
    +---------------------------------+----------------+
    | CPE                             | CVEs           |
    +---------------------------------+----------------+
    | cpe:/a:pcre:pcre:8.41           | CVE-2017-11164 |
    | ------------------------------- | -------------- |
    | cpe:/a:lame_project:lame:3.99.5 | CVE-2017-11720 |
    |                                 | CVE-2017-15019 |
    |                                 | CVE-2017-9872  |

    ....

    |                                 | CVE-2017-17942 |
    |                                 | CVE-2017-18013 |
    | ------------------------------- | -------------- |
    | cpe:/a:gnu:libtasn1:4.12        | CVE-2017-10790 |
    | ------------------------------- | -------------- |
    | cpe:/a:ffmpeg:ffmpeg:3.4.1      | CVE-2017-17555 |
    +---------------------------------+----------------+


Contributing
============

Any collaboration is welcome!

There're many tasks to do.You can check the `Issues <https://github.com/bbva/patton/issues/>`_ and send us a Pull Request.

Also you can read the `TODO <https://github.com/bbva/patton/blob/master/TODO.rst>`_ file.

License
=======

This project is distributed under `Apache 2 license <https://github.com/bbva/idsfree/blob/master/LICENSE>`_



---
This product includes software developed at
BBVA (https://www.bbva.com/)
