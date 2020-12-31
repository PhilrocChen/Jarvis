

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.stg_manual_actual_sellout_monthly`;
CREATE TABLE IF NOT EXISTS `korea.stg_manual_actual_sellout_monthly`(
`channel_name` string COMMENT 'channel_name',
`mall_name` string COMMENT 'mall_name',
`sap_signature_short_name` string COMMENT 'sap_signature_short_name',
`year_name` string COMMENT 'year_name',
`month_short_desc` string COMMENT 'month_short_desc',
`actual_sellout_amount` decimal(22,7) COMMENT 'actual_sellout_amount',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'E-Boutique and Open Sale monthly data'
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;