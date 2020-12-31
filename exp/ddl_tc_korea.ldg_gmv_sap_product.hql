

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


CREATE EXTERNAL TABLE `korea.ldg_gmv_sap_product`(
`sap_product_code` String COMMENT 'sap_product_code',
`sap_product_name` String COMMENT 'sap_product_name',
`sap_product_desc` String COMMENT 'sap_product_desc',
`sap_signature_short_name` String COMMENT 'sap_signature_short_name',
`hero_number` String COMMENT 'hero_number',
`hero_name` String COMMENT 'hero_name'
)
COMMENT 'GMV list for ad-hoc'
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES
(
  'field.delim'=',',
  'quoteChar'='\"',
  'separatorChar'=',',
  'serialization.encoding'='UTF-8'
)
STORED AS INPUTFORMAT
  'org.apache.hadoop.mapred.TextInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION '/user/svc.korea/sourcing/manual/ldg_gmv_sap_product'
TBLPROPERTIES ( 'skip.header.line.count'='1')
;