

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


CREATE EXTERNAL TABLE `korea.ldg_budget_target_monthly`(
`channel_name` String COMMENT 'channel_name',
`mall_name` String COMMENT 'mall_name',
`sap_signature_short_name` String COMMENT 'sap_signature_short_name',
`year_name` String COMMENT 'year_name',
`month_name` String COMMENT 'month_name',
`pre_budget_amount` String COMMENT 'pre_budget_amount',
`budget_amount` String COMMENT 'budget_amount',
`trend_target_amount` String COMMENT 'trend_target_amount',
`commercial_target_amount` String COMMENT 'commercial_target_amount'
)
COMMENT 'Budget and Target montly data'
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
LOCATION '/user/svc.korea/sourcing/manual/ldg_budget_target_monthly'
TBLPROPERTIES ( 'skip.header.line.count'='1')
;