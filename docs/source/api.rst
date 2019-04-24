Rest API
========

Getting CVEs from library names
+++++++++++++++++++++++++++++++

.. http:post:: /api/v1/check-dependencies/?(int:cpeDetailed)

   Parameter ``cpeDetailed`` is optional. By default their value is '0'. Setting their value to 1 makes Patton-server to return a more detailed list of CPE and CVEs

   JSON parameter ``source`` could take these values:

   - **auto**: a synonym of python
   - **dpkg**: For Ubuntu / Debian-like systems
   - **alpine**: Alpine Docker system
   - **python**: Python source libraries
   - **maven**: Maven format as a source

   **Example request**

   .. sourcecode:: http

      POST /api/v1/check-dependencies/ HTTP/1.1
      Host: patton.owaspmadrid.org:8000
      Content-Type: application/json

      {
          "source": "auto",
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
   :statuscode 404: there's no CVE information


   **Example request with param** ``cpeDetailed``:

   .. sourcecode:: http


      POST /api/v1/check-dependencies?cpeDetailed=1 HTTP/1.1
      Host: patton.owaspmadrid.org:8000
      Accept: application/json

      {
          "source": "auto",
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


   **Example response with param** ``cpeDetailed``:

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

Getting CVE Information from CVE
+++++++++++++++++++++++++++++++++

.. http:get:: /api/v1/cve/{cve:string}

   ``cve`` parameter is an string that contains a valid CVE.

   **Example request**

   .. sourcecode:: http

      GET /api/v1/cve/CVE-2017-17837 HTTP/1.1
      Host: patton.owaspmadrid.org:8000
      Accept: application/json


   **Example response**

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

        [
            {
                "href": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-17837",
                "description": "The Apache DeltaSpike-JSF 1.8.0 module has a XSS injection leak in the windowId handling. The default size of the windowId get's cut off after 10 characters (by default), so the impact might be limited. A fix got applied and released in Apache deltaspike-1.8.1.",
                "score": 4.3
            }
        ]
