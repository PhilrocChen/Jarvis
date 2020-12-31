

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.rpt_sellout_daily_agg_l1`;
CREATE TABLE IF NOT EXISTS `korea.rpt_sellout_daily_agg_l1`(
`doc_date` timestamp COMMENT 'doc_date',
`channel_mode_code` string COMMENT 'channel_mode_code',
`channel_name` string COMMENT 'channel_name',
`mall_name` string COMMENT 'mall_name',
`sap_signature_short_name` string COMMENT 'sap_signature_short_name',
`month_short_desc` string COMMENT 'month_short_desc',
`prev_year_sellout_amount` decimal(22,7) COMMENT 'prev_year_sellout_amount',
`actual_sellout_amount` decimal(22,7) COMMENT 'actual_sellout_amount',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'Sellout aggregation on daily brand channel level from MARS'
PARTITIONED BY (
  `doc_month_code` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;