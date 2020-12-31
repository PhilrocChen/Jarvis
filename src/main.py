#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-03-21
Purpose:
    1. Dynamically read data model from excel to get information. And extract to DDL script.
    2. Compare with meta data for sync and check. (This is going to be phase 2)
"""

from src.file.excel import Excel
from src.file.table2ddl import Table2DDL


def main():
    data = Excel("OneData_DataModel_KOREA_20201030.xlsm")
    ddl = Table2DDL(data.table_info)
    ddl.get_tables()


if __name__ == main():
    main()
