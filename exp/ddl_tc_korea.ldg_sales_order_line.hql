

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


CREATE EXTERNAL TABLE `korea.ldg_sales_order_line`(
`country` String COMMENT 'country',
`organization` String COMMENT 'organization',
`ident_source` String COMMENT 'ident_source',
`person_id` String COMMENT 'person_id',
`order_num` String COMMENT 'order_num',
`bar_code` String COMMENT 'bar_code',
`product` String COMMENT 'product',
`type` String COMMENT 'type',
`quantity` String COMMENT 'quantity',
`return_reason_cd` String COMMENT 'return_reason_cd',
`price` String COMMENT 'price',
`product_origin` String COMMENT 'product_origin',
`product_type` String COMMENT 'product_type',
`coupon_code` String COMMENT 'coupon_code',
`line_num` String COMMENT 'line_num',
`markdown_reason1` String COMMENT 'markdown_reason1',
`markdown_reason2` String COMMENT 'markdown_reason2',
`incl_amt_bf_disc` String COMMENT 'incl_amt_bf_disc',
`excl_amt_af_disc` String COMMENT 'excl_amt_af_disc',
`excl_amt_bf_disc` String COMMENT 'excl_amt_bf_disc',
`sap_item_code` String COMMENT 'sap_item_code'
)
COMMENT 'Sales Order Line from MARS'
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
LOCATION '/user/svc.korea/sourcing/mars/ldg_sales_order_line'
TBLPROPERTIES ( 'skip.header.line.count'='1')
;