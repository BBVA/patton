from sanic import Blueprint
from sanic.response import json

from .cpes_managers.cpe_managers_v2 import query_cpe
from .banners_managers.banners_managers_v2 import query_banners

end_points_api_v2 = Blueprint("end_points_api_v2")


@end_points_api_v2.route('/api/v1/check-dependencies', methods=['POST'])
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
                                    detailed_cpe))
    except (Exception, ValueError) as e:
        return json({"message": e}, 400)


@end_points_api_v2.route('/api/v1/check-banners',
                         methods=['POST'])
async def check_banners(request):

    try:
        return json(await query_banners(request.app.pool, request.json))
    except (Exception, ValueError, IndexError) as e:
        return json({"message": e}, 400)


__all__ = ("end_points_api_v2",)
