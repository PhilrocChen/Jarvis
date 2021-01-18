#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2021-01-14
Purpose:
    1. Populate table info from Excel to CSV
"""

from conf import configuration as cf
from src.parser.excel import Excel
from src.parser.table import TableInfo
from src.transform.table2ddl import Table2DDL
from src.transform.table2graph import Table2Graph


def main():
    data = Excel("OneData_DataModel_KOREA_2021.xlsm")
    table_info = TableInfo(cf.TABLE_INFO_FROM_CONFIG_LIST[0], data)
    table_info.write_csv()


if __name__ == main():
    main()
