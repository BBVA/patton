import csv
import json
import os.path as op

from typing import Dict, List
from pprint import pprint
from argparse import Namespace

from terminaltables import AsciiTable
from patton_client.exceptions import *


class PattonRunningConfig:

    def __init__(self,
                 nargs_input: List[str],
                 follow_checking: bool,
                 data_from_file: str,
                 quiet_mode: bool,
                 banner_type: str,
                 display_format: str,
                 patton_host: str,
                 source_type: str,
                 output_file: str,
                 skip_on_fail: bool):
        self.patton_host = patton_host
        self.skip_on_fail = skip_on_fail
        self.nargs_input = nargs_input
        self.display_format = display_format
        self.follow_checking = follow_checking
        self.quiet_mode = quiet_mode
        self.banner_type = banner_type
        self.data_from_file = data_from_file
        self.output_file = output_file
        self.source_type = source_type

        #
        # Constrains
        #
        #  If continuous mode selected -> quiet mode is selected
        if self.follow_checking:
            self.quiet_mode = True

            if not self.output_file:
                raise PCException("When you choose the continuous mode you"
                                  "need to specify an output file")

    @classmethod
    def from_argparser(cls, argparsed: Namespace):
        return PattonRunningConfig(
            quiet_mode=argparsed.QUIET_MODE,
            follow_checking=getattr(argparsed, "FOLLOW_CHECKING", None),
            banner_type=getattr(argparsed, "BANNER_TYPE", None),
            data_from_file=argparsed.FROM_FILE,
            source_type=argparsed.SOURCE_TYPE,
            nargs_input=argparsed.INPUT_LIST,
            display_format=argparsed.DISPLAY_FORMAT,
            patton_host=argparsed.PATTON_HOST,
            output_file=argparsed.OUTPUT_FILE,
            skip_on_fail=argparsed.SKIP_ON_FAIL)


class PattonResults:

    ALLOWED_DUMP_FORMATS = ("csv", "json", "raw")

    def __init__(self,
                 results: Dict,
                 running_config:
                 PattonRunningConfig):
        self.results = results
        self.running_config = running_config

    @classmethod
    def from_api(cls, json_result, patton_config):
        return PattonResults(json_result, patton_config)

    def _to_table(self):
        display_results = [
            ['Name', 'CPEs', 'CVEs'],
        ]

        def _transform_data(data,
                            col1_size=None,
                            col2_size=None,
                            col3_size=None):
            good_data = []

            len_dep_values = len(data.items()) - 1
            for h, (dep_name, dep_values) in enumerate(data.items()):

                cpes_len = len(dep_values.get("cpes", [])) - 1
                for j, cpes in enumerate(dep_values.get("cpes", [])):

                    cpe = cpes.get("cpe")
                    cpe_len = len(cpes.get("cves", [])) - 1
                    for i, cve_obj in enumerate(cpes.get("cves", [])):

                        cve = cve_obj.get("cve")
                        cvss = cve_obj.get("score")

                        if j == 0 and i == 0:
                            good_data.append([dep_name, cpe,
                                              f"{cve} ({cvss})"])
                        elif 0 <= j < cpes_len + 1 and i == 0:
                            good_data.append(["", cpe, f"{cve} ({cvss})"])
                        else:
                            good_data.append(["", "", f"{cve} ({cvss})"])

                        if col1_size and i < cpe_len:
                            good_data.append(("",
                                              "",
                                              "-" * col3_size))

                    if col1_size and j < cpes_len:
                        good_data.append(("",
                                          "-" * col2_size,
                                          "-" * col3_size))

                if col1_size and h < len_dep_values:
                    good_data.append(("-" * col1_size,
                                      "-" * col2_size,
                                      "-" * col3_size))

            return good_data

        if not self.results:
            display_results.append(["-", "No found CVEs"])
        else:
            tmp_table = AsciiTable(_transform_data(self.results))

            col1, col2, col3 = tmp_table.column_widths
            display_results.extend(_transform_data(self.results,
                                                   col1,
                                                   col2,
                                                   col3))

        t = AsciiTable(display_results)
        return t.table

    def _to_csv(self):

        results = set()

        for h, (dep_name, dep_values) in enumerate(self.results.items()):

            for j, cpes in enumerate(dep_values.get("cpes", [])):

                cpe = cpes.get("cpe")
                for i, cve_obj in enumerate(cpes.get("cves", [])):
                    cve = cve_obj.get("cve")
                    cvss = cve_obj.get("score")
                    summary = cve_obj.get("summary")
                    results.add((
                        dep_name, cpe, cve, str(cvss), summary
                    ))

        return results

    def display(self, mode="table"):

        if not self.running_config.quiet_mode:
            if mode in ("raw", "json"):
                pprint(self.results)
            elif mode == "table":
                print(self._to_table())
            elif mode == "csv":
                print("# Name", "CPE", "CVE", "Score")
                print("\n".join([", ".join(x) for x in self._to_csv()]))
            else:
                self._to_table()

    def dump(self):
        """Dump to file"""

        # NO Dump file selected -> DO NOTHING
        if self.running_config.output_file:

            # Determinate file format
            _, extension = op.splitext(self.running_config.output_file)
            extension = extension.replace(".", "")

            if extension not in self.ALLOWED_DUMP_FORMATS:
                raise PCException(
                    f"Extension of dump file is not available. "
                    f"Allowed extensions are: "
                    f"{', '.join(self.ALLOWED_DUMP_FORMATS)}")

            with open(self.running_config.output_file, "w") as f:
                if extension == "csv":
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(("# Name",
                                         "CPE",
                                         "CVE",
                                         "Score",
                                         "Summary"))
                    csv_writer.writerows(self._to_csv())

                elif extension == "json":
                    json.dump(self.results,
                              f,
                              indent=4,
                              sort_keys=True)

                elif extension == "raw":
                    f.write(self._to_table())


__all__ = ("PattonRunningConfig", "PattonResults")
