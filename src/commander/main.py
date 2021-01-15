#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-03-21
Purpose:
    1. Dynamically read data model from excel to get information. And extract to DDL script.
    2. Compare with meta data for sync and check. (This is going to be phase 2)
"""

from conf import configuration as cf
from src.parser.excel import Excel
from src.parser.table import TableInfo
from src.transform.table2ddl import Table2DDL
from src.transform.table2graph import Table2Graph


def main():
    data = Excel("OneData_DataModel_KOREA_2021.xlsm")
    # ddl = TableInfo(data.table_info)
    # ddl.get_tables()
    table_info = TableInfo(data, cf.TABLE_INFO_FROM_CONFIG_LIST[0])
    graph = Table2Graph(table_info.read_tables())
    graph.get_tables()


if __name__ == main():
    main()
