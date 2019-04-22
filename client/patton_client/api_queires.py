import json
import aiohttp
import logging

from typing import List, Dict

from patton_client import PattonRunningConfig, PCServerResponseException, \
    PCException

log = logging.getLogger("patton-cli")


def _prepare_query(dep_list: Dict[str, str],
                   config: PattonRunningConfig) -> Dict:
    # detect and separate dependencies form library name
    obj_query = {
        "method": "auto",
        "libraries": [
            {
                "library": dep_name,
                "version": dep_version
            }
            for dep_name, dep_version in dep_list.items()
        ]
    }
    return obj_query


async def do_api_query(dep_list: Dict,
                       patton_url: str,
                       patton_config: PattonRunningConfig) -> Dict:

    if not patton_url.startswith("http"):
        patton_url = f"http://{patton_url}"

    async with aiohttp.ClientSession() as session:
        async with session.post(
                patton_url,
                data=json.dumps(dep_list),
                headers={'content-type': 'application/json'}) as resp:
            if resp.status == 200:
                server_response = await resp.json()
            else:
                server_response = await resp.text()

                raise PCServerResponseException(
                    f"Server error: {server_response}")

        return server_response


async def check_dependencies_in_patton(dep_list: List[str],
                                       patton_config: PattonRunningConfig) \
        -> Dict:

    patton_url = f'{patton_config.patton_host}/api/v1/' \
                 f'check-dependencies?cpeDetailed=1'

    query_data = _prepare_query(dep_list, patton_config)
    query_data["source"] = patton_config.source_type

    try:
        return await do_api_query(query_data, patton_url, patton_config)
    except (aiohttp.client_exceptions.ServerDisconnectedError,
            aiohttp.client_exceptions.ClientConnectorError):
        raise PCException("Can't connect to Patton Server")


async def check_banners_in_patton(dep_list: List[str],
                                  patton_config: PattonRunningConfig) \
        -> Dict:

    patton_url = f'{patton_config.patton_host}/api/v1/check-banners'

    try:
        return await do_api_query(dep_list, patton_url, patton_config)
    except aiohttp.client_exceptions.ServerDisconnectedError:
        raise PCException("Can't connect to Patton Server")
