SHELL = /bin/bash
YEAR = $(shell date +%Y)
NVDCVES_JSON = $(shell echo nvdcve-1.1-{2002..$(YEAR)}.reduced.json)

patton.db.xz: patton.db
	xz -9e --keep --force "$<"

patton.db: $(NVDCVES_JSON)
	cat $? > "$@"

nvdcve-1.1-%.json.gz:
	curl -s -o "$@" "https://nvd.nist.gov/feeds/json/cve/1.1/$@"

nvdcve-1.1-%.json: nvdcve-1.1-%.json.gz
	gzip -dc < "$<" > "$@"

# Simplify nvdcve files to three field jsonlines removing
# rejected CVEs.
# ["CVE", "DESCRIPTION, ["CPE1", "CPE2"]]
nvdcve-1.1-%.stripped.json: nvdcve-1.1-%.json
	jq -c '.CVE_Items[] | [.cve.CVE_data_meta.ID, ([.cve.description.description_data[] | if .lang == "en" then .value else empty end] | join("\n")), [.configurations.nodes[] | .. | select(.vulnerable?) | .cpe23Uri]]' "$<" | jq -c 'if (.[2] | length == 0) and (.[1] | test("\\*\\* REJECT \\*\\*")) then empty else . end' > "$@"

# Creates a file with a CVE per line
nvdcve-1.1-%.cves.json: nvdcve-1.1-%.stripped.json
	jq -c '.[0]' < "$<" > "$@"

# Creates a file with a CVE description per line
nvdcve-1.1-%.description.json: nvdcve-1.1-%.stripped.json
	jq -c '.[1]' < "$<" | docker run -i cesargallego/desc-stripper > "$@"

# Creates a file with a CVE CPE tree per line
nvdcve-1.1-%.cpes.json: nvdcve-1.1-%.stripped.json
	jq -c '.[2]' < "$<" | docker run -i nilp0inter/cpelst2tree > "$@"

# Mix CVE, Description and CPE tree into a single file
nvdcve-1.1-%.reduced.json: nvdcve-1.1-%.cves.json nvdcve-1.1-%.description.json nvdcve-1.1-%.cpes.json
	python3 -c 'import sys as s,json as j; [print(j.dumps(list(x))) for x in zip(*(map(j.loads, open(f).readlines()) for f in s.argv[1:]))]' nvdcve-1.1-$*.cves.json nvdcve-1.1-$*.description.json nvdcve-1.1-$*.cpes.json > "$@"
