

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


CREATE EXTERNAL TABLE `korea.ldg_workday_calendar`(
`date_id` String COMMENT 'date_id',
`date_desc` String COMMENT 'date_desc',
`workday_flag` String COMMENT 'Workday "Y", Holiday "N"'
)
COMMENT 'Holiday and special workday Calendar'
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
LOCATION '/user/svc.korea/sourcing/manual/ldg_workday_calendar'
TBLPROPERTIES ( 'skip.header.line.count'='1')
;