#!/usr/bin/env sh
set -xeu

source ${ENV:-.env}

download_path=${PATTON_DOWNLOAD_FOLDER}
rm -rf $download_path
mkdir -p $download_path

download(){
	file=$(basename $1)
	wget -q $1 -O $download_path/$file && gunzip $download_path/$file || true
}

download_cpe() {
	download https://static.nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.gz
}

download_cve() {
	for i in $(seq 2002 2018)
	do
		download https://static.nvd.nist.gov/feeds/xml/cve/2.0/nvdcve-2.0-$i.xml.gz
	done
}

download_cpe
download_cve
