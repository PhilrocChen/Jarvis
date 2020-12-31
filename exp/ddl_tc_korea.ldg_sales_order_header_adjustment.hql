

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


CREATE EXTERNAL TABLE `korea.ldg_sales_order_header_adjustment`(
`adjustment_code` String COMMENT 'adjustment_code',
`adjustment_date` String COMMENT 'adjustment_date',
`adjustment_owner_name` String COMMENT 'adjustment_owner_name',
`order_num` String COMMENT 'order_num',
`order_type_code` String COMMENT 'type',
`order_date` String COMMENT 'order_dt',
`doc_date` String COMMENT 'doc_dt',
`market_id` String COMMENT 'country',
`sap_signature_code` String COMMENT 'organization',
`ident_source_code` String COMMENT 'ident_source',
`counter_id` String COMMENT 'counter_id',
`ba_id` String COMMENT 'ba_id',
`person_id` String COMMENT 'person_id'
)
COMMENT 'Sales Order Header Adjustment'
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
LOCATION '/user/svc.korea/sourcing/manual/ldg_sales_order_header_adjustment'
TBLPROPERTIES ( 'skip.header.line.count'='1')
;