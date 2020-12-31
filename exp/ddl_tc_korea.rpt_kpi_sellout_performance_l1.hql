

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.rpt_kpi_sellout_performance_l1`;
CREATE TABLE IF NOT EXISTS `korea.rpt_kpi_sellout_performance_l1`(
`doc_date` timestamp COMMENT 'doc_date',
`doc_month_code` string COMMENT 'month code from header_doc_dt, exp: 202010',
`channel_mode_code` string COMMENT 'channel_mode_code',
`channel_name` string COMMENT 'channel_name',
`mall_name` string COMMENT 'mall_name',
`sap_signature_short_name` string COMMENT 'sap_signature_short_name',
`month_short_desc` string COMMENT 'month_short_desc',
`prev_year_sellout_amount` decimal(22,7) COMMENT 'prev_year_sellout_amount',
`actual_sellout_amount` decimal(22,7) COMMENT 'actual_sellout_amount',
`budget_amount` decimal(22,7) COMMENT 'budget_amount',
`trend_target_amount` decimal(22,7) COMMENT 'trend_target_amount',
`commercial_target_amount` decimal(22,7) COMMENT 'commercial_target_amount',
`achieve_budget_pct` decimal(22,7) COMMENT 'achieve_budget_pct',
`achieve_trend_pct` decimal(22,7) COMMENT 'achieve_trend_pct',
`achieve_target_pct` decimal(22,7) COMMENT 'achieve_target_pct',
`evol_pct` decimal(22,7) COMMENT 'evol_pct',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'KPI aggregate table Level 1'
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;