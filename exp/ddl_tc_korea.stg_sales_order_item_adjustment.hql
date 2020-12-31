

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.stg_sales_order_item_adjustment`;
CREATE TABLE IF NOT EXISTS `korea.stg_sales_order_item_adjustment`(
`adjustment_code` string COMMENT 'adjustment_code',
`adjustment_date` date COMMENT 'adjustment_date',
`adjustment_owner_name` string COMMENT 'adjustment_owner_name',
`order_number` string COMMENT 'order_num',
`order_line_number` string COMMENT 'line_num',
`order_type_code` string COMMENT 'type',
`sap_product_code` string COMMENT 'product',
`sap_item_code` string COMMENT 'sap_item_code',
`product_origin_code` string COMMENT 'product_origin',
`bar_code` string COMMENT 'bar_code',
`order_quantity` int COMMENT 'quantity',
`order_price_amount` decimal(22,7) COMMENT 'price',
`incl_amt_bf_disc_amount` decimal(22,7) COMMENT 'incl_amt_bf_disc',
`excl_amt_af_disc_amount` decimal(22,7) COMMENT 'excl_amt_af_disc',
`excl_amt_bf_disc_amount` decimal(22,7) COMMENT 'excl_amt_bf_disc',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'Sales Order Item Adjustment'
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;