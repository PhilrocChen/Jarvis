

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


CREATE EXTERNAL TABLE `korea.ldg_sales_order_line_adjustment`(
`adjustment_code` String COMMENT 'adjustment_code',
`adjustment_date` String COMMENT 'adjustment_date',
`adjustment_owner_name` String COMMENT 'adjustment_owner_name',
`order_number` String COMMENT 'order_num',
`order_line_number` String COMMENT 'line_num',
`order_type_code` String COMMENT 'type',
`sap_product_code` String COMMENT 'product',
`sap_item_code` String COMMENT 'sap_item_code',
`product_origin_code` String COMMENT 'product_origin',
`bar_code` String COMMENT 'bar_code',
`order_quantity` String COMMENT 'quantity',
`order_price_amount` String COMMENT 'price',
`incl_amt_bf_disc_amount` String COMMENT 'incl_amt_bf_disc',
`excl_amt_af_disc_amount` String COMMENT 'excl_amt_af_disc',
`excl_amt_bf_disc_amount` String COMMENT 'excl_amt_bf_disc'
)
COMMENT 'Sales Order Line Adjustment'
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
LOCATION '/user/svc.korea/sourcing/manual/ldg_sales_order_line_adjustment'
TBLPROPERTIES ( 'skip.header.line.count'='1')
;