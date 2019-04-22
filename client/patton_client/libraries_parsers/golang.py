import re
import logging

from typing import List, Dict

from patton_client import PattonRunningConfig, PCException

log = logging.getLogger("patton-cli")

def golang_parser(lines: str, config: PattonRunningConfig) -> Dict:

    def clean(s):
        return s.strip().replace('"', '')

    results = {}

    lines = lines[:lines.find("[solve-meta]")].strip()
    content = "\n".join([line for line in lines.split("\n") if not line.startswith("#") and line != ""])
    projects = [project.strip() for project in content.split("[[projects]]") if project != '']

    for project in projects:
        project_dict = {clean(val.split(" = ")[0]): clean(val.split(" = ")[1]) for val in project.split("\n")}
        version = project_dict.get("version") or project_dict.get("revision", "")
        results[project_dict["name"]] = version

    return results
