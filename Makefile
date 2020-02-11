SHELL = /bin/bash
YEAR = $(shell date +%Y)
NVDCVES_JSON = $(shell echo nvdcve-1.1-{2002..$(YEAR)}.stripped.json)
NVDCVES_TSV = $(shell echo nvdcve-1.1-{2002..$(YEAR)}.tsv)

nvdcve.tsv: $(NVDCVES_TSV)
	cat $? > nvdcve.tsv

nvdcve.txz: nvdcve
	tar -Jcf nvdcve.txz nvdcve/

nvdcve-1.1-%.json.gz:
	curl -s -o "$@" "https://nvd.nist.gov/feeds/json/cve/1.1/$@"

nvdcve-1.1-%.json: nvdcve-1.1-%.json.gz
	gzip -dc < "$<" > "$@"

nvdcve-1.1-%.stripped.json: nvdcve-1.1-%.json
	jq '.CVE_Items[] | [{cve: .cve.CVE_data_meta.ID, descriptions: [.cve.description.description_data[].value], cpes: [.configurations.nodes[] | .. | select(.vulnerable?) | .cpe23Uri]}]' "$<" | jq -s add > "$@"

nvdcve-1.1-%.tsv: nvdcve-1.1-%.stripped.json
	jq '.[] | [.cve, (.descriptions|tostring), (.cpes|tostring)] | @tsv' < "$<" > "$@"
