

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.itg_fact_sales_order`;
CREATE TABLE IF NOT EXISTS `korea.itg_fact_sales_order`(
`order_number` string COMMENT 'header_order_num',
`order_line_number` string COMMENT 'line_line_num',
`order_type_code` string COMMENT 'line_type',
`order_date` timestamp COMMENT 'header_order_dt',
`doc_date` timestamp COMMENT 'header_doc_dt',
`market_id` string COMMENT 'header_country',
`sap_signature_code` string COMMENT 'header_organization',
`ident_source_code` string COMMENT 'header_ident_source',
`counter_id` string COMMENT 'header_counter_id',
`mall_name` string COMMENT 'mall_name',
`channel_name` string COMMENT 'channel_name',
`channel_mode_code` string COMMENT 'channel_mode_code',
`ba_id` string COMMENT 'header_ba_id',
`person_id` string COMMENT 'header_person_id',
`sap_product_code` string COMMENT 'line_product',
`sap_item_code` string COMMENT 'line_sap_item_code',
`product_origin_code` string COMMENT 'line_product_origin',
`bar_code` string COMMENT 'line_bar_code',
`order_quantity` int COMMENT 'line_quantity',
`order_price_amount` decimal(22,7) COMMENT 'line_price',
`incl_amt_bf_disc_amount` decimal(22,7) COMMENT 'line_incl_amt_bf_disc',
`excl_amt_af_disc_amount` decimal(22,7) COMMENT 'line_excl_amt_af_disc',
`excl_amt_bf_disc_amount` decimal(22,7) COMMENT 'line_excl_amt_bf_disc',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'Sales Order Line Item level with Header information by join from MARS'
PARTITIONED BY (
  `doc_month_code` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;