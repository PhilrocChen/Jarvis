#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-03-21
Purpose:
    Connect to Hive metadata
"""

import conf.configuration as cf
import pymysql.cursors


class Mysql:
    def __init__(self, sql):
        self.sql = sql

    def connector(self):
        connection = pymysql.connect(
            host=cf.MYSQL_HOST,
            port=cf.MYSQL_PORT,
            user=cf.MYSQL_USER,
            passwd=cf.MYSQL_PASSWORD,
            db=cf.MYSQL_DB,
            charset=cf.MYSQL_CHARSET,
            cursorclass=pymysql.cursors.DictCursor
        )
        if connection:
            print('Connection established.')
            try:
                cursor = connection.cursor()
                cursor.execute(self.sql)
                results = cursor.fetchall()
                for row in results:
                    print(row)
                cursor.close()
                connection.close()
            except Exception as e:
                print(e)
        else:
            print('Connection failed.')
