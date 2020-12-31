

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


CREATE EXTERNAL TABLE `korea.ldg_manual_sellout_monthly`(
`channel_name` String COMMENT 'channel_name',
`mall_name` String COMMENT 'mall_name',
`sap_signature_short_name` String COMMENT 'sap_signature_short_name',
`year_name` String COMMENT 'year_name',
`month_name` String COMMENT 'month_name',
`actual_sellout_amount` String COMMENT 'actual_sellout_amount'
)
COMMENT 'E-Boutique and Open Sale monthly data'
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
LOCATION '/user/svc.korea/sourcing/manual/ldg_manual_sellout_monthly'
TBLPROPERTIES ( 'skip.header.line.count'='1')
;