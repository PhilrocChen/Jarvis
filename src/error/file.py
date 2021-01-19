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
    raise print(f"Value of {parameter} is incorrect. Please correct Excel.")


def table_info_miss(check_zip):
    for key, value in check_zip:
        if not value or pd.isnull(value):
            raise print(f"Table information: {key} is missing. Please correct Excel.")
        else:
            pass


