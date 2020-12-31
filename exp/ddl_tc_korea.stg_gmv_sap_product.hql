

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.stg_gmv_sap_product`;
CREATE TABLE IF NOT EXISTS `korea.stg_gmv_sap_product`(
`sap_product_code` string COMMENT 'sap_product_code',
`sap_product_name` string COMMENT 'sap_product_name',
`sap_product_desc` string COMMENT 'sap_product_desc',
`sap_signature_short_name` string COMMENT 'sap_signature_short_name',
`hero_number` string COMMENT 'hero_number',
`hero_name` string COMMENT 'hero_name',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'GMV list for ad-hoc'
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;