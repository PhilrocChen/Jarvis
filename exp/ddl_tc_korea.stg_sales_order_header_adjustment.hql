

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.stg_sales_order_header_adjustment`;
CREATE TABLE IF NOT EXISTS `korea.stg_sales_order_header_adjustment`(
`adjustment_code` string COMMENT 'adjustment_code',
`adjustment_date` date COMMENT 'adjustment_date',
`adjustment_owner_name` string COMMENT 'adjustment_owner_name',
`order_num` string COMMENT 'order_num',
`order_type_code` string COMMENT 'type',
`order_date` timestamp COMMENT 'order_dt',
`doc_date` timestamp COMMENT 'doc_dt',
`market_id` string COMMENT 'country',
`sap_signature_code` string COMMENT 'organization',
`ident_source_code` string COMMENT 'ident_source',
`counter_id` string COMMENT 'counter_id',
`ba_id` string COMMENT 'ba_id',
`person_id` string COMMENT 'person_id',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'Sales Order Header Adjustment'
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;