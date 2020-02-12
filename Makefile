SHELL = /bin/bash
YEAR = $(shell date +%Y)
NVDCVES_JSON = $(shell echo nvdcve-1.1-{2002..$(YEAR)}.stripped.json)

patton.db.gz: patton.db
	gzip -c "$<" > "$@"

patton.db: $(NVDCVES_JSON)
	cat $? > "$@"

nvdcve-1.1-%.json.gz:
	curl -s -o "$@" "https://nvd.nist.gov/feeds/json/cve/1.1/$@"

nvdcve-1.1-%.json: nvdcve-1.1-%.json.gz
	gzip -dc < "$<" > "$@"

nvdcve-1.1-%.stripped.json: nvdcve-1.1-%.json
	jq -c '.CVE_Items[] | [.cve.CVE_data_meta.ID, (.cve.description.description_data[] | [if .lang == "en" then .value else empty end] | join("\n")), [.configurations.nodes[] | .. | select(.vulnerable?) | .cpe23Uri]]' "$<" > "$@"
