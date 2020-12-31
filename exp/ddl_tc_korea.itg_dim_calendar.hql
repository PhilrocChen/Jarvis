

--  Description: Jarvis auto generation
--  Author: Jarvis
--  Last Modified: 2020-12-31 17:12:45


DROP TABLE IF EXISTS `korea.itg_dim_calendar`;
CREATE TABLE IF NOT EXISTS `korea.itg_dim_calendar`(
`date_id` int COMMENT 'date_id',
`date` timestamp COMMENT 'date',
`day` int COMMENT 'day',
`day_desc` string COMMENT 'day_desc',
`week_num` int COMMENT 'week_num',
`day_of_week` int COMMENT 'day_of_week',
`day_of_week_desc` string COMMENT 'day_of_week_desc',
`week_start_date` timestamp COMMENT 'week_start_date',
`week_end_date` timestamp COMMENT 'week_end_date',
`month` int COMMENT 'month',
`month_short_desc` string COMMENT 'month_short_desc',
`r3m_start_month` string COMMENT 'r3m_start_month',
`last_month` string COMMENT 'last_month',
`month_year` string COMMENT 'month_year',
`quarter` string COMMENT 'quarter',
`quarter_year` string COMMENT 'quarter_year',
`semester` string COMMENT 'semester',
`semester_year` string COMMENT 'semester_year',
`year` int COMMENT 'year',
`last_year_today` timestamp COMMENT 'last_year_today',
`load_ts` timestamp COMMENT 'load_ts',
`workday_flag` string COMMENT 'workday_flag',
`date_desc` string COMMENT 'date_desc',
`insert_timestamp` timestamp COMMENT 'insert_timestamp',
`source_system_code` string COMMENT 'source_system_code',
`batch_date` string COMMENT 'batch_date'
)
COMMENT 'Calendar with Korea holiday'
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat'
OUTPUTFORMAT
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
;