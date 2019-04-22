import os

from typing import List, Union, Dict, Set, Tuple

import xml.etree.ElementTree as ET

from patton_client import PCInvalidFormatException


def parse_from_file(file_name_content: str) -> Union[Set[Tuple[str, str]],
                                                     PCInvalidFormatException]:
    """

    :param file_name_content:
    :type file_name_content:
    :return:
    :rtype:
    """

    # Check that is a correct Nmap file
    # Read the first 2 lines and try to read the content:
    # <!DOCTYPE nmaprun>
    if "<!DOCTYPE nmaprun>" not in "".join(
            file_name_content.splitlines()[0:2]):
        raise PCInvalidFormatException(
            f"file '{os.path.basename(file_name)}' "
            f"doesn't appear to a valid XML nmap file. Ensure that"
            f"nmap report format is in XML")

    e = ET.fromstring(file_name_content)

    temp_products = {
        x.attrib["product"]: x.attrib["version"] for x in
        e.findall(".//service")
        if x.attrib["name"] != "unknown" and "version" in x.attrib
        and "product" in x.attrib
    }

    results = set()

    for product, version in temp_products.items():
        _product, *_ = product.strip().split(" ", maxsplit=2)
        _version, *_ = version.strip().split(" ", maxsplit=2)

        results.add((_product.lower(), _version.lower()))

    return results


def parse_from_continuous() -> Union[Dict[str, str],
                                     PCInvalidFormatException]:
    pass
