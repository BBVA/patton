Patton-cli - The Swiss knife of the Admin & Security auditor
======================================================

What's Patton-cli?
++++++++++++++++++

Patton-cli born with the objective to be a Swiss knife for system admins and security auditors, it could be filled with many different sources and report in many formats, being a great choice for scripting.

Installation
++++++++++++

**NOTE**

    Patton-cli need a Patton-server, be sure that you have a server already running!

Using pip
---------

This is the easiest way of installing Patton-cli:

.. code-block:: bash

    > python3.6 -m pip install patton-cli

Using Docker
------------

Patton-cli module includes a Dockerfile to generate a docker image. It can install `patton-cli` from either the pypi release, the github head, or from the current working directory. It accepts a `build-arg` for chose. Run one of:

.. code-block:: bash

    docker build -t patton-cli . --build-arg source=cwd
    docker build -t patton-cli . --build-arg source=github
    docker build -t patton-cli . --build-arg source=pypi

There's already a `published image <https://hub.docker.com/r/bbvalabs/patton-cli>`_ ready to pull and run.

Getting help
------------

Patton-cli has self-explained doc:

.. code-block:: bash

    > patton -h

    usage: patton [-h] [-v] [--patton-host PATTON_HOST] [-F {table,json,csv}] [-q]
              [-i FROM_FILE] [-o OUTPUT_FILE]
              [-e {python,alpine,simple_parser,auto,nmap,dpkg}] [-s] [-D] [-B]
              [-t {auto,nmap}] [-f]
              [INPUT_LIST [INPUT_LIST ...]]

    Patton cli

    positional arguments:
      INPUT_LIST

    optional arguments:
      -h, --help            show this help message and exit
      -v                    log level
      --patton-host PATTON_HOST
                            patton server host
      -F {table,json,csv}, --display-format {table,json,csv}
                            display format options
      -q, --quiet           do not display any information in stdout
      -i FROM_FILE, --from-file FROM_FILE
                            output file for results
      -o OUTPUT_FILE, --output-file OUTPUT_FILE
                            results file. formats: csv, json, raw
      -e {python,alpine,simple_parser,auto,nmap,dpkg}, --source-type {python,alpine,simple_parser,auto,nmap,dpkg}
                            use specific source parser
      -s, --skip-on-fail    doesn't abort execution on dependency check fail

    Working modes:
      -D, --dependency      check libraries and versions (default)
      -B, --banner          check banners (currently experimental)

    Specific option for banners:
      -t {auto,nmap}, --banner-type {auto,nmap}
                            http, ftp, ...-
      -f, --follow          read from stdin and do a continuously check

    Examples:

      * Checking specific library and output as table:
        > patton django:1.2 flask:1.1.0

      * Checking Python installed dependencies and output as CSV:
        > pip freeze | patton -F csv
        or
        > patton -F csv -i requirements.txt

      * Checking ubuntu dependencies display as table and dump in json file:
        > dpkg -l | patton -e dpkg -F table -o results.json

Usage examples
==============

Quick example
-------------

.. code-block:: bash

    > patton django:1.9

    +------------+-------------------------------------+---------------------+
    | Name       | CPEs                                | CVEs                |
    +------------+-------------------------------------+---------------------+
    | django:1.9 | cpe:/a:djangoproject:django:1.9:rc2 | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7234 (5.8) |
    |            | ----------------------------------- | ------------------- |
    |            | cpe:/a:djangoproject:django:1.9:rc2 | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7234 (5.8) |
    |            | ----------------------------------- | ------------------- |
    |            | cpe:/a:djangoproject:django:1.9:rc2 | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7234 (5.8) |
    |            | ----------------------------------- | ------------------- |
    |            | cpe:/a:djangoproject:django:1.9:rc2 | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7234 (5.8) |
    |            | ----------------------------------- | ------------------- |
    |            | cpe:/a:djangoproject:django:1.9:rc1 | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            | ----------------------------------- | ------------------- |
    |            | cpe:/a:djangoproject:django:1.9:rc1 | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            | ----------------------------------- | ------------------- |
    |            | cpe:/a:djangoproject:django:1.9:rc1 | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            | ----------------------------------- | ------------------- |
    |            | cpe:/a:djangoproject:django:1.9:rc1 | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            | ----------------------------------- | ------------------- |
    |            | cpe:/a:djangoproject:django:1.9:b1  | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    |            | ----------------------------------- | ------------------- |
    |            | cpe:/a:djangoproject:django:1.9:b1  | CVE-2017-7234 (5.8) |
    |            |                                     | ------------------- |
    |            |                                     | CVE-2017-7233 (5.8) |
    +------------+-------------------------------------+---------------------+

Getting vulnerabilities from different sources
----------------------------------------------

From Ubuntu
+++++++++++

.. code-block:: bash

    > dpkg -l | patton -e dpkg

From Brew
+++++++++

.. code-block:: bash

    > brew list --versions | patton

From Alpine
+++++++++++

.. code-block:: bash

    > apk version -v | patton -e alpine

From python requirements
++++++++++++++++++++++++

.. code-block:: bash

    > pip freeze | patton -e python

or

.. code-block:: bash

    > cat requirements.txt | patton -e python

or

.. code-block:: bash

    > patton -i requirements.txt -e python


From Golang requirements
++++++++++++++++++++++++

.. code-block:: bash

    > cat Gopkg.lock | patton -e golang

* Currently Golang's package versioning is still somewhat green, but the biggest solution right now is https://github.com/golang/dep


Formatting the output
---------------------

Patton-cli can display results in these formats:

- Table
- JSON
- CSV

.. code-block:: bash

    > cat requirements.txt | patton -e python -F csv

.. code-block:: bash

    > cat requirements.txt | patton -e python -F json

.. code-block:: bash

    > cat requirements.txt | patton -e python -F table

Exporting results
-----------------

Patton-cli can export the results in format:

- Raw (table)
- JSON
- CSV

The format of file is determined by the extension:

.. code-block:: bash

    > cat requirements.txt | patton -e python -o report.json

.. code-block:: bash

    > cat requirements.txt | patton -e python -o report.csv

.. code-block:: bash

    > cat requirements.txt | patton -e python -o report.raw

Quiet mode
----------

If you don't want that Patton-cli reports anything by the terminal, you can use **-q** option:


.. code-block:: bash

    > cat requirements.txt | patton -e python -q -o report.csv

Some funny examples
-------------------

Listing dependencies and check te vulns:

.. code-block:: bash

    > dpkg -l | tee patton -e dpkg -q -o reports.csv

Finding critical vulnerabilities:

.. code-block:: bash

    > dpkg -l | patton -e dpkg -F csv | grep "10\.0" > critial_vulns.txt
