

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.stg_manual_open_sales_daily`;
CREATE TABLE IF NOT EXISTS `korea.stg_manual_open_sales_daily`(
`channel_name` string COMMENT 'channel_name',
`mall_name` string COMMENT 'mall_name',
`sap_signature_short_name` string COMMENT 'sap_signature_short_name',
`year_name` string COMMENT 'year_name',
`month_name` string COMMENT 'month_name',
`day_name` string COMMENT 'day_name',
`actual_sellout_amount` decimal(22,7) COMMENT 'actual_sellout_amount',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'Open Sale Daily for operation purpose'
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;