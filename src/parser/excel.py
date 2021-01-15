#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-03-21
Purpose:
    Read data from Excel and analysis
"""

import os
import pandas as pd
import conf.configuration as cf
import src.error.file as fe
import src.connector.excel4model as e4m


class Excel:

    def __init__(
            self,
            file
    ):
        self.file = file
        self.file_path = e4m.Excel4Model(self.file).file_path

    def read_content(self):
        try:
            _content_df = pd.read_excel(self.file_path, sheet_name=cf.CONTENT)
            _physical_table_df = _content_df[
                _content_df[cf.CONTENT_STRUCTURE[1][0]] == cf.CONTENT_STRUCTURE_PHYSICAL_MODEL
            ]
            physical_table_list = list(set(_physical_table_df[cf.CONTENT].dropna()))
            return physical_table_list
        except Exception as e:
            print(e)
            fe.content_miss()

    physical_table_list = property(read_content)

    def read_tables(self):
        table_info = []
        if self.physical_table_list:
            try:
                for table in self.physical_table_list:
                    _table_header = self.read_table_heard(table)
                    _table_body = self.read_table_body(table)
                    table_info.append([_table_header, _table_body])
                return table_info
            except Exception as e:
                print(e)
        else:
            fe.sheet_miss()

    table_info = property(read_tables)

    def read_table_heard(self, table):
        _table_info = pd.read_excel(self.file_path, sheet_name=table, header=0)
        table_header = []
        for i in range(len(cf.TABLE_HEADER_STRUCTURE)):
            _col = _table_info.iloc[cf.TABLE_HEADER_STRUCTURE[i][1][0], cf.TABLE_HEADER_STRUCTURE[i][1][1]]
            table_header.append(_col)
        return table_header

    def read_table_body(self, table):
        table_body = pd.read_excel(self.file_path, sheet_name=table, header=cf.TABLE_STRUCTURE_START_ROW)
        return table_body
