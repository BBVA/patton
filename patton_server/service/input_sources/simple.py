def simple_builder(library: str, version: str) -> str:
    """Return the full text query"""

    return f"({library.lower()}:* & {version.lower()}:*)"
