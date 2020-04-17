Feature: Search Software Vulnerabilities

  Scenario: Find vulnerabilities in a product name with specific version
    Given I have search term "Apache JSPWiki" and version "2.11"
    When I execute Patton search with search type "product"
    Then I get at least one cve
      | CVE ID         | URL                                             |
      | CVE-2019-10090 | https://nvd.nist.gov/vuln/detail/CVE-2019-10090 |

  Scenario: Find vulnerabilities in a library that affects only when runs in a specific framework.
    Given I have search term "Tinymce Color Picker"
    And It is a Wordpress plugin
    When I execute Patton search with search type "fulltext"
    Then I get at least one cve
      | CVE ID         | URL                                            |
      | CVE-2014-3845  | https://nvd.nist.gov/vuln/detail/CVE-2014-3845 |

  Scenario: Find vulnerabilities in a system running Ubuntu package manager
      Given I have the output of "Ubuntu" package manager
        """
        ii  docker   1.4.1   amd64   Docker: the open-source application container engine
        """
      When I execute Patton search with search type "pkg_ubuntu"
      Then I get at least one cve
          | CVE ID         | URL                                                          |
          | CVE-2019-5736  | https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736 |


  Scenario: Find vulnerabilities in all installed packages in Debian system
    NOTE: The version of each package is forced to 0 to maximize the chances of
    reported vulnerabilites.
    Given I have the raw output of installed packages for "Debian" package manager
      """
      Package: busybox
      Status: install ok installed
      Priority: optional
      Section: utils
      Installed-Size: 768
      Maintainer: Debian Install System Team <debian-boot@lists.debian.org>
      Architecture: amd64
      Version: 0
      Replaces: busybox-static
      Depends: libc6 (>= 2.28)
      Breaks: initramfs-tools (<< 0.99)
      Conflicts: busybox-static
      Description: Tiny utilities for small and embedded systems
       BusyBox combines tiny versions of many common UNIX utilities into a single
       small executable. It provides minimalist replacements for the most common
       utilities you would usually find on your desktop system (i.e., ls, cp, mv,
       mount, tar, etc.). The utilities in BusyBox generally have fewer options than
       their full-featured GNU cousins; however, the options that are included
       provide the expected functionality and behave very much like their GNU
       counterparts.
       .
       This package installs the BusyBox binary but does not install
       symlinks for any of the supported utilities. Some of the utilities
       can be used in the system by installing the busybox-syslogd,
       busybox-udhcpc or busybox-udhcpd packages.
      Homepage: http://www.busybox.net

      Package: python2.7
      Status: install ok installed
      Priority: optional
      Section: python
      Installed-Size: 377
      Maintainer: Matthias Klose <doko@debian.org>
      Architecture: amd64
      Multi-Arch: allowed
      Version: 0
      Replaces: python-profiler (<= 2.7.1-2), python2.7-minimal (<< 2.7.3-7~)
      Depends: python2.7-minimal (= 2.7.16-2+deb10u1), libpython2.7-stdlib (= 2.7.16-2+deb10u1), mime-support
      Suggests: python2.7-doc, binutils
      Breaks: python-virtualenv (<< 1.7.1.2-2~), vim-athena (<< 2:7.3.547-4), vim-gnome (<< 2:7.3.547-4), vim-gtk (<< 2:7.3.547-4), vim-nox (<< 2:7.3.547-4)
      Conflicts: python-profiler (<= 2.7.1-2)
      Description: Interactive high-level object-oriented language (version 2.7)
       Python is a high-level, interactive, object-oriented language. Its 2.7 version
       includes an extensive class library with lots of goodies for
       network programming, system administration, sounds and graphics.
      """

    When I execute Patton search with type "pkg_debian"
    Then I get at least these vulnerabilities
      | Library Name | Library Version | CVE ID           |
      | busybox      |               0 | CVE-2011-5325    |
      | busybox      |               0 | CVE-2013-1813    |
      | busybox      |               0 | CVE-2014-4607    |
      | busybox      |               0 | CVE-2014-9645    |
      | busybox      |               0 | CVE-2015-9261    |
      | busybox      |               0 | CVE-2016-2147    |
      | busybox      |               0 | CVE-2016-2148    |
      | busybox      |               0 | CVE-2017-15873   |
      | busybox      |               0 | CVE-2017-16544   |
      | busybox      |               0 | CVE-2018-1000517 |
      | busybox      |               0 | CVE-2018-20679   |
      | python2.7    |               0 | CVE-2010-1634    |
      | python2.7    |               0 | CVE-2010-2089    |
      | python2.7    |               0 | CVE-2011-1521    |
      | python2.7    |               0 | CVE-2011-3389    |
      | python2.7    |               0 | CVE-2011-4944    |
      | python2.7    |               0 | CVE-2012-0845    |
      | python2.7    |               0 | CVE-2012-1150    |
      | python2.7    |               0 | CVE-2013-1753    |
      | python2.7    |               0 | CVE-2013-4238    |
      | python2.7    |               0 | CVE-2013-7440    |
      | python2.7    |               0 | CVE-2014-1912    |
      | python2.7    |               0 | CVE-2014-4616    |
      | python2.7    |               0 | CVE-2014-4650    |
      | python2.7    |               0 | CVE-2014-7185    |
      | python2.7    |               0 | CVE-2014-9365    |
      | python2.7    |               0 | CVE-2016-0772    |
      | python2.7    |               0 | CVE-2016-5636    |
      | python2.7    |               0 | CVE-2016-5699    |
      | python2.7    |               0 | CVE-2017-1000158 |
      | python2.7    |               0 | CVE-2018-1000802 |
      | python2.7    |               0 | CVE-2018-1060    |
      | python2.7    |               0 | CVE-2018-1061    |
      | python2.7    |               0 | CVE-2018-14647   |
      | python2.7    |               0 | CVE-2018-20852   |
      | python2.7    |               0 | CVE-2019-16056   |
      | python2.7    |               0 | CVE-2019-16935   |
      | python2.7    |               0 | CVE-2019-5010    |
      | python2.7    |               0 | CVE-2019-9636    |
      | python2.7    |               0 | CVE-2019-9740    |
      | python2.7    |               0 | CVE-2019-9947    |
      | python2.7    |               0 | CVE-2019-9948    |
      | python2.7    |               0 | CVE-2020-8492    |

    And Not found these false positives
      | Library Name | Library Version | CVE ID           |
      | busybox      |               0 | CVE-2006-1058    |
      | busybox      |               0 | CVE-2011-2716    |
      | busybox      |               0 | CVE-2016-6301    |
      | busybox      |               0 | CVE-2017-15874   |
      | busybox      |               0 | CVE-2017-3209    |
      | busybox      |               0 | CVE-2018-1000500 |
      | busybox      |               0 | CVE-2019-5747    |
      | python2.7    |               0 | CVE-2010-3492    |
      | python2.7    |               0 | CVE-2010-3493    |
      | python2.7    |               0 | CVE-2011-4940    |
      | python2.7    |               0 | CVE-2013-7040    |
      | python2.7    |               0 | CVE-2016-2183    |
      | python2.7    |               0 | CVE-2019-10160   |


  Scenario: Find vulnerabilities in all installed packages in Ubuntu system
    Given I have the raw output of installed packages for "Ubuntu" package manager
      """
      Desired=Unknown/Install/Remove/Purge/Hold
      | Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
      |/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
      ||/ Name                              Version               Architecture          Description
      +++-=================================-=====================-=====================-========================================================================
      ii  libpython3.5:amd64                3.5.2-2ubuntu0~16.04. amd64                 Shared Python runtime library (version 3.5)
      ii  python3-jinja2                    2.8-1                 all                   small but fast and easy to use stand-alone template engine
      ii  bind9-host                        1:9.10.3.dfsg.P4-8ubu amd64                 Version of 'host' bundled with BIND 9.X
      ii  docker-ce                         17.09.1~ce-0~ubuntu   amd64                 Docker: the open-source application container engine
      """

    When I execute Patton search with type "pkg_ubuntu2"
    Then I get at least these vulnerabilities
      | Library Name           | Library Version         | CVE ID                |
      | python3-jinja2         | 2.8-1                   | CVE-2016-10745        |
      | bind9-host             | 1:9.10.3.dfsg.P4-8ubu   | CVE-2018-5741         |
      | docker-ce              | 17.09.1~ce-0~ubuntu     | CVE-2017-14992        |

    And Not found these false positives
      | Library Name           | Library Version         | CVE ID                |
      | python3-cryptography   | 1.2.3-1ubuntu0.1        | CVE-2019-5736         |
      | python3-jwt            | 1.3.0-1ubuntu0.1        | CVE-2017-11424        |
