#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-03-21
Purpose:
    Get table information and save to ddl
"""

import datetime
import conf.configuration as cf
import src.error.file as fe
from src.database.table import Table
from src.file.save2exp import Save2Exp


class Table2DDL:

    def __init__(
            self,
            table_info
    ):
        self.table_info = table_info

    def get_tables(self):
        try:
            for table in self.table_info:
                # file header
                _file_header = "/*"
                _file_header = _file_header + "\n  Description: Jarvis auto generation"
                _file_header = _file_header + "\n  Author: Jarvis"
                _date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                _script_format = "\n  Last Modified: {}"
                _file_header = _file_header + _script_format.format(_date_time)
                _file_header = _file_header + "\n*/"
                # file body
                body_script, partition_key_list = self.create_body(table[0], table[1])
                file_name, header_script, tail_script = self.create_header_tail(table[0], partition_key_list)
                _script_format = "{}\n\n\n{}\n{}\n{}"
                script = _script_format.format(_file_header, header_script, body_script, tail_script)
                _script_format = "{}: Script generated successfully: {}"
                file_save = Save2Exp(file_name, script)
                file_save.file_save()
                print(_script_format.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), file_name))
        except Exception as e:
            print(e)

    def create_header_tail(self, table, partition_key_list):
        _table = Table(table)
        _database_name = _table.database_name()
        _table_name = _table.table_name()
        _table_layer = _table.table_layer()
        _table_type = _table.table_type()
        # File name
        _script_format = "ddl_tc_{}.{}"
        file_name = _script_format.format(_database_name, _table_name)
        # Table type check
        if _table_type == cf.TABLE_TYPE_LIST[0]:
            if _table_layer == cf.TABLE_LAYER_LIST[0]:
                header_script, tail_script = self.tail_landing_internal(table, partition_key_list)
            else:
                header_script, tail_script = self.tail_other_internal(table, partition_key_list)
        elif _table_type == cf.TABLE_TYPE_LIST[1]:
            header_script, tail_script = self.tail_landing_external(table, partition_key_list)
        else:
            header_script = ""
            tail_script = ""
        _script_format = "{}: DDL header and tail built successful."
        print(_script_format.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return file_name, header_script, tail_script

    @staticmethod
    def create_body(table_header, table_body):
        body_script = ""
        partition_key_list = []
        _table = Table(table_header)
        _table_layer = _table.table_layer()
        for index, row in table_body.iterrows():
            _column_partition_key = row[cf.TABLE_BODY_STRUCTURE[4]].strip()
            if _column_partition_key == cf.TABLE_BODY_PARTITION_KEY_LIST[0]:
                partition_key_list.append(row[cf.TABLE_BODY_STRUCTURE[1]].strip())
            else:
                _script_format = "`{}`"
                _column_physical_name = _script_format.format(row[cf.TABLE_BODY_STRUCTURE[1]].strip())
                if _table_layer == cf.TABLE_LAYER_LIST[0]:
                    _column_type = "String"
                else:
                    _column_type = row[cf.TABLE_BODY_STRUCTURE[2]].strip()
                _column_comment = row[cf.TABLE_BODY_STRUCTURE[7]].strip()
                # Mandatory check
                _check_key_list = [
                    cf.TABLE_BODY_STRUCTURE[1],
                    cf.TABLE_BODY_STRUCTURE[2],
                    cf.TABLE_BODY_STRUCTURE[7]
                ]
                _check_value_list = [
                    _column_physical_name,
                    _column_type,
                    _column_comment
                ]
                check_zip = zip(_check_key_list, _check_value_list)
                fe.table_info_miss(check_zip)
                if body_script:
                    _script_format = ",\n{} {} COMMENT '{}'"
                    _body_script = _script_format.format(_column_physical_name, _column_type, _column_comment)
                    body_script = body_script + _body_script
                else:
                    _script_format = "{} {} COMMENT '{}'"
                    _body_script = _script_format.format(_column_physical_name, _column_type, _column_comment)
                    body_script = body_script + _body_script
        _script_format = "{}: DDL body built successful."
        _date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(_script_format.format(_date_time))
        return body_script, partition_key_list

    @staticmethod
    def tail_landing_external(table, partition_key_list):
        tail_script = ""
        _table = Table(table)
        _database_name = _table.database_name()
        _table_name = _table.table_name()
        _table_comment = _table.table_comment()
        _row_format_serde = _table.row_format_serde()
        _data_file_location = _table.data_file_location()
        _partitioned_by = _table.partitioned_by(partition_key_list)
        _store_as = _table.store_as()
        _table_properties = _table.table_properties()
        _with_serdeproperties = _table.with_serdeproperties()
        # Check External table required information
        _check_key_list = [
            cf.TABLE_HEADER_STRUCTURE[10][0]
        ]
        _check_value_list = [
            _data_file_location
        ]
        check_zip = zip(_check_key_list, _check_value_list)
        fe.table_info_miss(check_zip)
        # Header script
        _script_format = "CREATE EXTERNAL TABLE `{}.{}`("
        header_script = _script_format.format(_database_name, _table_name)
        # Tail script
        tail_script = tail_script + ")"
        # Table comment
        _script_format = "\nCOMMENT '{}'"
        _tail_script = _script_format.format(_table_comment)
        tail_script = tail_script + _tail_script
        # Partition
        if _partitioned_by:
            _script_format = "\nPARTITIONED BY (\n{}\n)"
            _tail_script = _script_format.format(_partitioned_by)
            tail_script = tail_script + _tail_script
        else:
            pass
        # Row format serde
        _script_format = "\nROW FORMAT SERDE '{}'"
        _tail_script = _script_format.format(_row_format_serde)
        tail_script = tail_script + _tail_script
        # CSV or Excel
        if _row_format_serde == cf.ROW_FORMAT_SERDE_LIST[0][1]:
            # With Serde Properties
            _script_format = "\n{}"
            _tail_script = _script_format.format(_with_serdeproperties)
            tail_script = tail_script + _tail_script
        else:
            pass
        # STORED AS
        _script_format = "\n{}"
        _tail_script = _script_format.format(_store_as)
        tail_script = tail_script + _tail_script
        # External table location
        _script_format = "\nLOCATION '{}'"
        _tail_script = _script_format.format(_data_file_location)
        tail_script = tail_script + _tail_script
        # CSV or Excel
        if _row_format_serde == cf.ROW_FORMAT_SERDE_LIST[1][1]:
            # Table properties
            _script_format = "\n{}"
            _tail_script = _script_format.format(_table_properties)
            tail_script = tail_script + _tail_script
        else:
            pass
        tail_script = tail_script + "\n;"
        return header_script, tail_script

    @staticmethod
    def tail_landing_internal(table, partition_key_list):
        tail_script = ""
        _table = Table(table)
        _database_name = _table.database_name()
        _table_name = _table.table_name()
        _table_comment = _table.table_comment()
        _row_format_serde = _table.row_format_serde()
        _partitioned_by = _table.partitioned_by(partition_key_list)
        _store_as = _table.store_as()
        _with_serdeproperties = _table.with_serdeproperties()
        # Header script
        _script_format = "CREATE TABLE IF NOT EXISTS `{}.{}`("
        header_script = _script_format.format(_database_name, _table_name)
        # Tail script
        tail_script = tail_script + ")"
        # Table comment
        _script_format = "\nCOMMENT '{}'"
        _tail_script = _script_format.format(_table_comment)
        tail_script = tail_script + _tail_script
        # Partition
        if _partitioned_by:
            _script_format = "\nPARTITIONED BY (\n{}\n)"
            _tail_script = _script_format.format(_partitioned_by)
            tail_script = tail_script + _tail_script
        else:
            pass
        # Row format serde
        _script_format = "\nROW FORMAT SERDE '{}'"
        _tail_script = _script_format.format(_row_format_serde)
        tail_script = tail_script + _tail_script
        # With Serde Properties
        _script_format = "\n{}"
        _tail_script = _script_format.format(_with_serdeproperties)
        tail_script = tail_script + _tail_script
        # STORED AS
        _script_format = "\n{}"
        _tail_script = _script_format.format(_store_as)
        tail_script = tail_script + _tail_script
        tail_script = tail_script + "\n;"
        return header_script, tail_script

    @staticmethod
    def tail_other_internal(table, partition_key_list):
        tail_script = ""
        _table = Table(table)
        _database_name = _table.database_name()
        _table_name = _table.table_name()
        _table_comment = _table.table_comment()
        _table_layer = _table.table_layer()
        _table_type = _table.table_type()
        _row_format_serde = _table.row_format_serde()
        _data_file_location = _table.data_file_location()
        _partitioned_by = _table.partitioned_by(partition_key_list)
        _clustered_by = _table.clustered_by()
        _sorted_by = _table.sorted_by()
        _buckets_number = _table.buckets_number()
        _store_as = _table.store_as()
        _table_properties = _table.table_properties()
        # Header script
        _script_format = "CREATE TABLE IF NOT EXISTS `{}.{}`("
        header_script = _script_format.format(_database_name, _table_name)
        # Tail script
        tail_script = tail_script + ")"
        # Table comment
        _script_format = "\nCOMMENT '{}'"
        _tail_script = _script_format.format(_table_comment)
        tail_script = tail_script + _tail_script
        # Partition
        if _partitioned_by:
            _script_format = "\nPARTITIONED BY (\n{}\n)"
            _tail_script = _script_format.format(_partitioned_by)
            tail_script = tail_script + _tail_script
        else:
            pass
        # Cluster
        if _clustered_by and _sorted_by and _buckets_number:
            _script_format = "\nCLUSTERED BY ({}) SORTED BY ({}) INTO {} BUCKETS"
            _tail_script = _script_format.format(_clustered_by, _sorted_by, _buckets_number)
            tail_script = tail_script + _tail_script
        else:
            pass
        # Row format serde
        _script_format = "\nROW FORMAT SERDE '{}'"
        _tail_script = _script_format.format(_row_format_serde)
        tail_script = tail_script + _tail_script
        # STORED AS
        _script_format = "\n{}"
        _tail_script = _script_format.format(_store_as)
        tail_script = tail_script + _tail_script
        tail_script = tail_script + "\n;"
        return header_script, tail_script
