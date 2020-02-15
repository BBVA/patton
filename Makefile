SHELL = /bin/bash
YEAR = $(shell date +%Y)
NVDCVES_JSON = $(shell echo nvdcve-1.1-{2002..$(YEAR)}.reduced.json)

patton.db.xz: patton.db
	xz -9 --keep --force "$<"

patton.db: $(NVDCVES_JSON)
	cat $? > "$@"

nvdcve-1.1-%.json.gz:
	curl -s -o "$@" "https://nvd.nist.gov/feeds/json/cve/1.1/$@"

nvdcve-1.1-%.json: nvdcve-1.1-%.json.gz
	gzip -dc < "$<" > "$@"

nvdcve-1.1-%.stripped.json: nvdcve-1.1-%.json
	jq -c '.CVE_Items[] | [.cve.CVE_data_meta.ID, ([.cve.description.description_data[] | if .lang == "en" then .value else empty end] | join("\n")), [.configurations.nodes[] | .. | select(.vulnerable?) | .cpe23Uri]]' "$<" > "$@"

nvdcve-1.1-%.cpes.json: nvdcve-1.1-%.stripped.json
	jq -c '.[2]' < "$<" | docker run -i nilp0inter/cpelst2tree > "$@"

nvdcve-1.1-%.reduced.json: nvdcve-1.1-%.cpes.json nvdcve-1.1-%.stripped.json
	python3 -c 'import sys as s,json as j; [print(j.dumps(l[:2]+[r])) for l, r in zip(map(j.loads,open(s.argv[1]).readlines()),map(j.loads,open(s.argv[2]).readlines()))]' nvdcve-1.1-$*.stripped.json nvdcve-1.1-$*.cpes.json > "$@"
