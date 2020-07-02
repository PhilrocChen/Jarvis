#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-03-21
Purpose:
    All designed error message which related to files.
"""

import pandas as pd


def content_miss():
    print("There is no Excel sheet <Content>. Please correct Excel.")


def sheet_miss():
    print("There is no table can be found in Excel sheet <Content>. Please click refresh button in it.")


def value_incorrect(parameter):
    _format = "Value of {} is incorrect. Please correct Excel."
    raise print(_format.format(parameter))


def table_info_miss(check_zip):
    for key, value in check_zip:
        if not value or pd.isnull(value):
            _format = "Table information: {} is missing. Please correct Excel."
            raise print(_format.format(key))
        else:
            pass


