

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.stg_sales_order_line`;
CREATE TABLE IF NOT EXISTS `korea.stg_sales_order_line`(
`header_country` string COMMENT 'header_country',
`header_organization` string COMMENT 'header_organization',
`header_ident_source` string COMMENT 'header_ident_source',
`header_person_id` string COMMENT 'header_person_id',
`header_order_num` string COMMENT 'header_order_num',
`header_order_dt` timestamp COMMENT 'header_order_dt',
`header_counter_id` string COMMENT 'header_counter_id',
`header_ba_id` string COMMENT 'header_ba_id',
`header_type` string COMMENT 'header_type',
`header_amount` decimal(22,7) COMMENT 'header_amount',
`header_remark` string COMMENT 'header_remark',
`header_status` string COMMENT 'header_status',
`header_quantity` int COMMENT 'header_quantity',
`header_gpbuy_flg` string COMMENT 'header_gpbuy_flg',
`header_points` string COMMENT 'header_points',
`header_source` string COMMENT 'header_source',
`header_doc_dt` timestamp COMMENT 'header_doc_dt',
`header_markdown_reason` string COMMENT 'header_markdown_reason',
`header_incl_amt_bf_disc` decimal(22,7) COMMENT 'header_incl_amt_bf_disc',
`header_excl_amt_af_disc` decimal(22,7) COMMENT 'header_excl_amt_af_disc',
`header_excl_amt_bf_disc` decimal(22,7) COMMENT 'header_excl_amt_bf_disc',
`line_bar_code` string COMMENT 'line_bar_code',
`line_product` string COMMENT 'line_product',
`line_type` string COMMENT 'line_type',
`line_quantity` int COMMENT 'line_quantity',
`line_return_reason_cd` string COMMENT 'line_return_reason_cd',
`line_price` decimal(22,7) COMMENT 'line_price',
`line_product_origin` string COMMENT 'line_product_origin',
`line_product_type` string COMMENT 'line_product_type',
`line_coupon_code` string COMMENT 'line_coupon_code',
`line_line_num` string COMMENT 'line_line_num',
`line_markdown_reason1` string COMMENT 'line_markdown_reason1',
`line_markdown_reason2` string COMMENT 'line_markdown_reason2',
`line_incl_amt_bf_disc` decimal(22,7) COMMENT 'line_incl_amt_bf_disc',
`line_excl_amt_af_disc` decimal(22,7) COMMENT 'line_excl_amt_af_disc',
`line_excl_amt_bf_disc` decimal(22,7) COMMENT 'line_excl_amt_bf_disc',
`line_sap_item_code` string COMMENT 'line_sap_item_code',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'Sales Order Line Item level with Header information by join from MARS'
PARTITIONED BY (
  `header_doc_month_code` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;