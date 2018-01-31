def dpkg_builder(library: str, version: str) -> str:
    """Return the full text query"""

    has_two_points = version.find(":")
    if has_two_points:
        version = version[has_two_points + 1:]

    # Case to parse:
    #   5.22.1-9ubuntu0.2
    # Valid result:
    #   5.22.1:rc9
    has_sep = version.find("-")
    if has_sep:
        version = version[has_two_points + 1:]

    # Case to parse:
    #   1.3.dfsg2-1build1
    # Valid result
    #   1.3:rc2

    return f"({library.lower()}:* & {version.lower()}:*)"

