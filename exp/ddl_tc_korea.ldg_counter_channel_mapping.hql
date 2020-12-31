

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


CREATE EXTERNAL TABLE `korea.ldg_counter_channel_mapping`(
`channel_mode_code` String COMMENT 'channel_mode_code',
`channel_name` String COMMENT 'channel_name',
`mall_name` String COMMENT 'mall_name',
`sap_signature_short_name` String COMMENT 'sap_signature_short_name',
`counter_id` String COMMENT 'counter_id',
`ba_id` String COMMENT 'ba_id'
)
COMMENT 'Counter Channel Mapping'
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
LOCATION '/user/svc.korea/sourcing/manual/ldg_counter_channel_mapping'
TBLPROPERTIES ( 'skip.header.line.count'='1')
;