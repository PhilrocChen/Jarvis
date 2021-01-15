#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2021-01-12
Purpose:
    1. Read data from Excel
    2. Parse info
    3. Generate Graph Dot file
    4. Generate Graph svg
"""

from conf import configuration as cf
from src.parser.excel import Excel
from src.parser.table import TableInfo
from src.transform.table2graph import Table2Graph
import os
import subprocess


def main():
    data = Excel("OneData_DataModel_KOREA_2021.xlsm")
    table_info = TableInfo(cf.TABLE_INFO_FROM_CONFIG_LIST[0], data)
    graph = Table2Graph(table_info.table_info)
    graph.get_tables()
    # graph.get_tables('korea.itg_fact_sales_order')

    graphdot = "JavisGraphDot.txt"
    graph = "JavisGraph.svg"
    _script_format = "dot -Tsvg {} -o {}"
    graph_script = _script_format.format(graphdot, graph)

    os.chdir(cf.EXP)
    subprocess.run(graph_script, shell=True)


if __name__ == main():
    main()
