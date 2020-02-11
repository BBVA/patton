Feature: Search Software Vulnerabilities

    Scenario: Find vulnerabilities in a product name with specific version
        Given Search term "Apache JSPWiki" version "2.11"
        When I execute Patton search
        Then I get at least one cve
            | CVE ID         | URL                                             |
            | CVE-2019-10090 | https://nvd.nist.gov/vuln/detail/CVE-2019-10090 |

    Scenario: Find vulnerabilities in a library that affects only when runs in a specific framework.
        Given Search term "Tinymce Color Picker"
        And It is a Wordpress plugin

        When I execute Patton Search
        Then We get at least one cve
            | CVE ID         | URL                                            |
            | CVE-2014-3845  | https://nvd.nist.gov/vuln/detail/CVE-2014-3845 |


    Scenario: Find vulnerabilities in a system running Ubuntu package manager
        Given Output of Ubuntu package manager
            | Raw output line                                                                                    |
            | ii  docker-ce   17.09.1~ce-0~ubuntu   amd64   Docker: the open-source application container engine |

        When Has public vulnerabilities
        Then We get at least one cve
            | CVE ID         | URL                                                          |
            | CVE-2019-5736  | https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-5736 |
