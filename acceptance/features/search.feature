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
