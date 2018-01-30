API
===


Getting CVEs from library names
+++++++++++++++++++++++++++++++

.. http:post:: /api/v1/check-dependencies/?(int:cpeDetailed)

   Parameter `cpeDetailed` is optional. By default their value is '0'. Setting their value to 1, Patton Server return a more detailed list of CPE and CVEs

   **Example request**:

   .. sourcecode:: http

      POST /api/v1/check-dependencies/ HTTP/1.1
      Host: patton.owaspmadrid.org
      Content-Type: application/json

      {
          "method": "auto",
          "libraries" : [
              {
                  "library": "django",
                  "version": "1.2"
              },
              {
                  "library": "postgres",
                  "version": "8"
              }
          ]
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
             "django:1.2": {
                 "cpes": [
                     "cpe:/a:djangoproject:django:1.2.1",
                     "cpe:/a:djangoproject:django:1.2.4",
                     "cpe:/a:djangoproject:django:1.2.3",
                     "cpe:/a:djangoproject:django:1.2",
                     "cpe:/a:djangoproject:django:1.2.2",
                     "cpe:/a:djangoproject:django:1.2.6",
                     "cpe:/a:djangoproject:django:1.2.2",
                     "cpe:/a:djangoproject:django:1.2.3",
                     "cpe:/a:djangoproject:django:1.2.4",
                     "cpe:/a:djangoproject:django:1.2.4"
                 ],
                 "cves": [
                     {
                         "cve": "CVE-2011-0698",
                         "score": 7.5
                     },
                     {
                         "cve": "CVE-2011-0698",
                         "score": 7.5
                     },
                     {
                         "cve": "CVE-2011-0698",
                         "score": 7.5
                     },
                     {
                         "cve": "CVE-2011-0698",
                         "score": 7.5
                     }
                 ]
             },
             "postgres:8": {
                 "cpes": [
                     "cpe:/a:postgresql:postgresql:8.4.15",
                     "cpe:/a:postgresql:postgresql:8.3.12",
                     "cpe:/a:postgresql:postgresql:8.4.13",
                     "cpe:/a:postgresql:postgresql:8.3",
                     "cpe:/a:postgresql:postgresql:8.3.4",
                     "cpe:/a:postgresql:postgresql:8.3",
                     "cpe:/a:postgresql:postgresql:8.3.4",
                     "cpe:/a:postgresql:postgresql:8.4.3"
                 ],
                 "cves": [
                     {
                         "cve": "CVE-2013-1902",
                         "score": 10
                     },
                     {
                         "cve": "CVE-2013-1903",
                         "score": 10
                     },
                     {
                         "cve": "CVE-2013-1903",
                         "score": 10
                     }
                 ]
             }
       }

   :statuscode 200: no error
   :statuscode 404: there's no user

  **Example request with param: 'cpeDetailed'**:

   .. sourcecode:: http

      POST /api/v1/check-dependencies?cpeDetailed=1 HTTP/1.1
      Host: patton.owaspmadrid.org
      Accept: application/json

      {
          "method": "auto",
          "libraries" : [
              {
                  "library": "django",
                  "version": "1.2"
              },
              {
                  "library": "postgres",
                  "version": "8"
              }
          ]
      }

   ** Example response with param 'cpeDetailed'**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
          "django:1.2": {
              "cpes": [
                  {
                      "cpe": "cpe:/a:djangoproject:django:1.2.4",
                      "cves": [
                          {
                              "cve": "CVE-2011-0698",
                              "score": 7.5
                          },
                          {
                              "cve": "CVE-2011-4140",
                              "score": 6.8
                          },
                          {
                              "cve": "CVE-2011-0696",
                              "score": 6.8
                          }
                      ]
                  },
                  {
                      "cpe": "cpe:/a:djangoproject:django:1.2",
                      "cves": [
                          {
                              "cve": "CVE-2011-0698",
                              "score": 7.5
                          }
                      ]
                  }
              ],
              "cves": [
                  {
                      "cve": "CVE-2011-0698",
                      "score": 7.5
                  },
                  {
                      "cve": "CVE-2011-0698",
                      "score": 7.5
                  },
                  {
                      "cve": "CVE-2011-0696",
                      "score": 6.8
                  }
              ]
          }
          "postgres:8": {
              "cpes": [
                  {
                      "cpe": "cpe:/a:postgresql:postgresql:8.4.15",
                      "cves": [
                          {
                              "cve": "CVE-2013-1902",
                              "score": 10
                          }
                      ]
                  },
                  {
                      "cpe": "cpe:/a:postgresql:postgresql:8.3.12",
                      "cves": [
                          {
                              "cve": "CVE-2013-1903",
                              "score": 10
                          },
                          {
                              "cve": "CVE-2013-1902",
                              "score": 10
                          }
                      ]
                  }
              ],
              "cves": [
                  {
                      "cve": "CVE-2013-1902",
                      "score": 10
                  },
                  {
                      "cve": "CVE-2013-1903",
                      "score": 10
                  },
                  {
                      "cve": "CVE-2013-1902",
                      "score": 10
                  },
                  {
                      "cve": "CVE-2013-1902",
                      "score": 10
                  }
              ]
          }
      }
