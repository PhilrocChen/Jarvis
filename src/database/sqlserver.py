#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-05-20
Purpose:
    Connect to Hive metadata
"""

import conf.configuration as cf
import pymssql


class SqlServer:
    def __init__(self, sql):
        self.sql = sql

    def connector(self):
        connection = pymssql.connect(
            server=cf.SQLSERVER_SERVER,
            user=cf.SQLSERVER_USER,
            password=cf.SQLSERVER_PASSWORD,
            database=cf.SQLSERVER_DATABASE
        )
        if connection:
            print('Connection established.')
            try:
                cursor = connection.cursor()
                cursor.execute(self.sql)
                for row in cursor:
                    print("ID=%d, Name=%s" % (row['id'], row['name']))
                connection.close()
            except Exception as e:
                print(e)
        else:
            print('Connection failed.')
