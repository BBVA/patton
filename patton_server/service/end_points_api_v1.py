from sanic import Blueprint
from sanic.response import json

from .cpes_managers.cpe_managers_v1 import query_cpe

end_points_api_v1 = Blueprint("end_points_api_v1")


@end_points_api_v1.route('/<package>/<version>', methods=['GET'])
async def package_search(request, package, version):
    """
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
    """
    return json(await query_cpe(request.app.pool, [[package, version]]))


@end_points_api_v1.route('/batch/', methods=['POST'])
async def batch_package_search(request):
    """
    Input JSON format:

    [
        ["django", "1.2"],
        ["flask", "1.0.1"]
    ]

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
    """

    try:
        return json(await query_cpe(request.app.pool, request.json))
    except (Exception, ValueError) as e:
        return json({"message": e}, 400)


__all__ = ("end_points_api_v1",)
