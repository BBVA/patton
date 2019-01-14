from sanic import Blueprint
from sanic.response import json

from .cpes_managers.cpe_managers_v2 import query_cpe
from .banners_managers.banners_managers_v2 import query_banners

end_points_api_v1 = Blueprint("end_points_api_v1")


@end_points_api_v1.route('/api/v1/check-dependencies', methods=['POST'])
async def check_libraries_v2(request):
    """
    Input JSON format:

    {
        "method": "auto",
        "libraries" : [
            {
                "library": "django",
                "version": "1.2"
            }
        ]
    }

    Output JSON format:

    {
        "django:1.2" : {
            "cpes": ["cpe1", "cpe2"]
            "cves": [
                {
                    "cve": "CVE-1999-0001",
                    "score: 9.8
                },
                {
                    "cve": "CVE-2000-0001",
                    "score: 9.8
                }
            ]

        }
    }


    Output JSON format with query param: cpeDetailed=1

    {
        "django:1.2" : {
            "cpes": [
                {
                    cpe: "cpe1",
                    cves: [
                        {
                            "cve": "CVE-1999-0001",
                            "score: 9.8
                        },
                        {
                            "cve": "CVE-2000-0001",
                            "score: 5.8
                        }

                    ]
                },
                {
                    cpe: "cpe2",
                    cves: [
                        {
                            "cve": "CVE-2019-1277",
                            "score: 4.8
                        },
                        {
                            "cve": "CVE-1111-9182",
                            "score: 1.8
                        }
                    ]
                }
            ]
            "cves": [
                {
                    "cve": "CVE-1999-0001",
                    "score: 9.8
                },
                {
                    "cve": "CVE-2000-0001",
                    "score: 9.8
                }
            ]

        }
    }

    """

    try:
        try:
            detailed_cpe = int(request.raw_args.get("cpeDetailed", 0))
        except ValueError:
            detailed_cpe = 0

        return json(await query_cpe(request.app.pool,
                                    request.json,
                                    detailed_cpe,
                                    request.app.config["MAXIMUM_CONCURRENT"]))
    except (Exception, ValueError) as e:
        return json({"message": e}, 400)


@end_points_api_v1.route('/api/v1/cve/<cve>', methods=['GET'])
async def get_cve_info(request, cve):
    """
    Given a CVE ID returns their information

    Return format:

    [
        {
            "href": "URL",
            "description": "LONG DESCRIPTION OF CVE",
            "score": "X.Y",
            "cvss_access_vector" = "NETWORK",
            "cvss_access_complexity" = "LOW",
            "cvss_authentication" = "NONE",
            "cvss_confidentiality_impact" = "COMPLETE",
            "cvss_integrity_impact" = "PARTIAL",
            "cvss_availability_impact" = "PARTIAL",
        }
    ]

    """

    try:
        db_pool = request.app.pool

        query = "select summary, cvss_score, cvss_access_vector, cvss_access_complexity, cvss_authentication, cvss_confidentiality_impact, cvss_integrity_impact, cvss_availability_impact from vuln where vuln.id like %s;"

        results = []
        results_append = results.append
        async with db_pool.acquire() as connection:
            async with connection.cursor() as cur:
                await cur.execute(query, (cve, ))

                async for row in cur:
                    results_append(
                        {
                            "href": f"https://cve.mitre.org/"
                                    f"cgi-bin/cvename.cgi?name={cve}",
                            "description": row[0],
                            "score": row[1],
                            "cvss_access_vector" = row[2],
                            "cvss_access_complexity" = row[3],
                            "cvss_authentication" = row[4],
                            "cvss_confidentiality_impact" = row[5],
                            "cvss_integrity_impact" = row[6],
                            "cvss_availability_impact" = row[7]
                        }
                    )

        return json(results)
    except (Exception, ValueError) as e:
        return json({"message": e}, 400)


@end_points_api_v1.route('/api/v1/check-banners',
                         methods=['POST'])
async def check_banners(request):

    try:
        return json({"message": "Not implemented yet"})
    except (Exception, ValueError, IndexError) as e:
        return json({"message": e}, 400)


__all__ = ("end_points_api_v1",)
