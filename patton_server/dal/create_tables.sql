CREATE TABLE IF NOT EXISTS vuln (
	id VARCHAR NOT NULL,
	PRIMARY KEY (id),
	published DATE,
	last_modified DATE,
	cwe VARCHAR,
	summary VARCHAR,
	cvss_score FLOAT,
	cvss_access_vector VARCHAR,
	cvss_access_complexity VARCHAR,
	cvss_authentication VARCHAR,
	cvss_confidentiality_impact VARCHAR,
	cvss_integrity_impact VARCHAR,
	cvss_availability_impact VARCHAR,
	cvss_source VARCHAR
);

CREATE TABLE IF NOT EXISTS prod (
	id VARCHAR NOT NULL,
	PRIMARY KEY (id),
	title VARCHAR,
	title_lang VARCHAR
);

CREATE TABLE IF NOT EXISTS vuln_product (
	id VARCHAR NOT NULL,
	vuln_id VARCHAR,
	prod_id VARCHAR,
	PRIMARY KEY (id),
	FOREIGN KEY(vuln_id) REFERENCES vuln (id),
	FOREIGN KEY(prod_id) REFERENCES prod (id)
);

CREATE TABLE IF NOT EXISTS prod_reference (
	id VARCHAR NOT NULL,
	prod_id VARCHAR,
	href VARCHAR,
	description VARCHAR,
	PRIMARY KEY (id),
	FOREIGN KEY(prod_id) REFERENCES prod (id)
);

CREATE TABLE IF NOT EXISTS cpe23 (
	id VARCHAR NOT NULL,
	prod_id VARCHAR,
	PRIMARY KEY (id),
	FOREIGN KEY(prod_id) REFERENCES prod (id)
);

CREATE TABLE IF NOT EXISTS cpe_norm (
	id VARCHAR NOT NULL,
	transformation VARCHAR,
	origin VARCHAR,
	input VARCHAR,
	output VARCHAR,
	PRIMARY KEY (id)
);
