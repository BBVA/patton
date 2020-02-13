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
        ii  docker-ce   17.09.1~ce-0~ubuntu   amd64   Docker: the open-source application container engine
        """
      When I execute Patton search with search type "pkg_ubuntu"
      Then I get at least one cve
          | CVE ID         | URL                                                          |
          | CVE-2019-5736  | https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736 |
