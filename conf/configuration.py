#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-03-21
Purpose:
    All configurations in system where programmer to do control.
"""

import os
import datetime


"""
System root path
"""
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'Jarvis')
DATA = os.path.join(ROOT, 'data')
EXP = os.path.join(ROOT, 'exp')
CONF = os.path.join(ROOT, 'conf')
CONF_FILE = os.path.join(CONF, 'file')

"""
System parameter
"""
"""
Content
"""
CONTENT = 'Content'
CONTENT_STRUCTURE = [
    ['Content', [0, 1]],
    ['Category', [0, 2]],
]
CONTENT_STRUCTURE_PHYSICAL_MODEL = 'Physical Model'

"""
Table
"""
TABLE_STRUCTURE_START_ROW = 17
TABLE_HEADER_STRUCTURE = [
    ['Database name', [0, 1]],
    ['Table name', [1, 1]],
    ['Table comment', [2, 1]],
    ['Table layer', [3, 1]],
    ['Table type', [4, 1]],
    ['Row Format Serde', [5, 1]],
    ['Field Delim', [6, 1]],
    ['Quote Char', [7, 1]],
    ['Separator Char', [8, 1]],
    ['Serialization Encoding', [9, 1]],
    ['Data file location (External table and file loading)', [10, 1]],
    ['Clustered by (Clustered Only)', [11, 1]],
    ['Sorted by (Clustered Only)', [12, 1]],
    ['Buckets number (Clustered Only)', [13, 1]],
    ['Refresh frequency,', [14, 1]],
]

TABLE_BODY_STRUCTURE = [
    'Column Logic Name',
    'Column Physical Name',
    'Column Type',
    'Primary Key',
    'Partition Key',
    'Nullable',
    'Private Default Value',
    'Column Comment',
    'Data Validation',
]
TABLE_BODY_PARTITION_KEY_LIST = ['Y']

"""
Hive Table DDL config
"""
TABLE_LAYER_LIST = ['Landing']
TABLE_TYPE_LIST = ['Internal', 'External']
ROW_FORMAT_SERDE_LIST = [
    ['CSV', 'org.apache.hadoop.hive.serde2.OpenCSVSerde'],
    ['Excel', 'org.zuinnote.hadoop.excel.hive.serde.ExcelSerde'],
    ['Text', 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'],
    ['PARQUET', 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe']
]

"""
Mysql Database
"""
MYSQL_HOST = 'yimian.mysql.database.chinacloudapi.cn'
MYSQL_PORT = 3306
MYSQL_USER = 'lrl_apac@yimian'
MYSQL_PASSWORD = 'WCQNA5+{c[n1'
MYSQL_DB = 'lrl_apac'
MYSQL_CHARSET = 'utf8mb4'

"""
SqlServer Database
One Data Audit
"""
SQLSERVER_SERVER = 'sgapacsagdbp1a.283e64fb58c7.database.windows.net'
SQLSERVER_USER = 'adp_etlaudit'
SQLSERVER_PASSWORD = 'adp_etlaudit123'
SQLSERVER_DATABASE = 'ADP_ETL_Audit'

