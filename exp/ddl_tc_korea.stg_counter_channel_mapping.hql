

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.stg_counter_channel_mapping`;
CREATE TABLE IF NOT EXISTS `korea.stg_counter_channel_mapping`(
`channel_mode_code` string COMMENT 'channel_mode_code',
`channel_name` string COMMENT 'channel_name',
`mall_name` string COMMENT 'mall_name',
`sap_signature_short_name` string COMMENT 'sap_signature_short_name',
`counter_id` string COMMENT 'counter_id',
`ba_id` string COMMENT 'ba_id',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'Counter Channel Mapping'
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;