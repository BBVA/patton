#!/usr/bin/env bash
set -xeu

# INFO: set this to 1 to check the xml schema and analyze the db table structure
download_schema=

download_path=/tmp/patton/
rm -rf $download_path

mkdir -p $download_path
download(){
	file=$(basename $1)
	wget -q $1 -O $download_path/$file && gunzip $download_path/$file || true
}

download_cpe() {
	download https://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.gz
	[ -n $download_schema ] && download https://scap.nist.gov/schema/cpe/2.3/cpe-dictionary_2.3.xsd
}

download_cve() {
	for i in $(seq 2002 2018)
	do
		download https://static.nvd.nist.gov/feeds/xml/cve/2.0/nvdcve-2.0-$i.xml.gz
	done
	[ -n $download_schema ] && download https://scap.nist.gov/schema/nvd/nvd-cve-feed_2.0.xsd
}

download_cpe
download_cve
python db.py --recreate
time python loader.py
