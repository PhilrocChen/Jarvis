

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


CREATE EXTERNAL TABLE `korea.ldg_sales_order_header`(
`country` String COMMENT 'country',
`organization` String COMMENT 'organization',
`ident_source` String COMMENT 'ident_source',
`person_id` String COMMENT 'person_id',
`order_num` String COMMENT 'order_num',
`order_dt` String COMMENT 'order_dt',
`counter_id` String COMMENT 'counter_id',
`ba_id` String COMMENT 'ba_id',
`type` String COMMENT 'type',
`amount` String COMMENT 'amount',
`remark` String COMMENT 'remark',
`status` String COMMENT 'status',
`quantity` String COMMENT 'quantity',
`gpbuy_flg` String COMMENT 'gpbuy_flg',
`points` String COMMENT 'points',
`source` String COMMENT 'source',
`doc_dt` String COMMENT 'doc_dt',
`markdown_reason` String COMMENT 'markdown_reason',
`incl_amt_bf_disc` String COMMENT 'incl_amt_bf_disc',
`excl_amt_af_disc` String COMMENT 'excl_amt_af_disc',
`excl_amt_bf_disc` String COMMENT 'excl_amt_bf_disc'
)
COMMENT 'Sales Order Header from Mars'
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
LOCATION '/user/svc.korea/sourcing/mars/ldg_sales_order_header'
TBLPROPERTIES ( 'skip.header.line.count'='1')
;