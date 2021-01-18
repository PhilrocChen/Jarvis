#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-03-21
Purpose:
    Connect to Hive metadata
"""

import unittest
import os
import conf.configuration as cf
import src.connector.mysql as mysql


class DatabaseConnect(unittest.TestCase):
    
    def test_mysql_connect(self):
        file = os.path.join(cf.DATA, 'test.sql')
        with open(file, 'r') as f:
            sql = f.read()
        print(sql)
        test = mysql.Mysql(sql)
        test.connector()


if __name__ == "__main__":
    unittest.main()
