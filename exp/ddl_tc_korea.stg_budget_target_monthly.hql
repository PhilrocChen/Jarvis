

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.stg_budget_target_monthly`;
CREATE TABLE IF NOT EXISTS `korea.stg_budget_target_monthly`(
`channel_name` string COMMENT 'channel_name',
`mall_name` string COMMENT 'mall_name',
`sap_signature_short_name` string COMMENT 'sap_signature_short_name',
`year_name` string COMMENT 'year_name',
`month_name` string COMMENT 'month_name',
`pre_budget_amount` decimal(22,7) COMMENT 'pre_budget_amount',
`budget_amount` decimal(22,7) COMMENT 'budget_amount',
`trend_target_amount` decimal(22,7) COMMENT 'trend_target_amount',
`commercial_target_amount` decimal(22,7) COMMENT 'commercial_target_amount',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'Budget and Target montly data'
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;