#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-12-31
Purpose:
    Connect to Excel data model
"""


import os
import conf.configuration as cf


class Excel4Model:
    def __init__(self, file):
        self.file_path = os.path.join(cf.DATA, file)
