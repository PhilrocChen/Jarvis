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
from src.parser.table import Table
from src.generator.save2exp import Save2Exp


class Table2DDL:

    def __init__(
            self,
            table_info
    ):
        self.table_info = table_info

    def get_tables(self):
        for table in self.table_info:
            # transform header
            _file_header = f"\n--  Description: Jarvis auto generation" \
                           f"\n--  Author: Jarvis" \
                           f"\n--  Last Modified: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            # transform body
            body_script, partition_key_list = self.create_body(table[0], table[1])
            file_name, header_script, tail_script = self.create_header_tail(table[0], partition_key_list)
            script = f"{_file_header}\n\n\n{header_script}\n{body_script}\n{tail_script}"
            file_save = Save2Exp(cf.SAVE2EXP_FILE_TYPE_LIST[0], file_name, script)
            file_save.file_save()
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Script generate successfully: {file_name}")

    def create_header_tail(self, table, partition_key_list):
        _table = Table(table)
        _database_name = _table.database_name()
        _table_name = _table.table_name()
        _table_layer = _table.table_layer()
        _table_type = _table.table_type()
        # File name
        file_name = f"ddl_tc_{_database_name}.{_table_name}"
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
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: DDL header and tail built successful.")
        return file_name, header_script, tail_script

    @staticmethod
    def create_body(table_header, table_body):
        body_script = ""
        partition_key_list = []
        _table = Table(table_header)
        _table_layer = _table.table_layer()
        for index, row in table_body.iterrows():
            _column_partition_key = str(row[cf.TABLE_BODY_STRUCTURE[5]]).strip()
            if _column_partition_key == cf.TABLE_BODY_PARTITION_KEY_LIST[0]:
                partition_key_list.append(str(row[cf.TABLE_BODY_STRUCTURE[1]]).strip())
            else:
                _column_physical_name = f"`{str(row[cf.TABLE_BODY_STRUCTURE[1]]).strip()}`"
                if _table_layer == cf.TABLE_LAYER_LIST[0]:
                    _column_type = "String"
                else:
                    _column_type = str(row[cf.TABLE_BODY_STRUCTURE[2]]).strip()
                _column_comment = str(row[cf.TABLE_BODY_STRUCTURE[8]]).strip()
                # Mandatory check
                _check_key_list = [
                    cf.TABLE_BODY_STRUCTURE[1],
                    cf.TABLE_BODY_STRUCTURE[2],
                    cf.TABLE_BODY_STRUCTURE[8]
                ]
                _check_value_list = [
                    _column_physical_name,
                    _column_type,
                    _column_comment
                ]
                check_zip = zip(_check_key_list, _check_value_list)
                fe.table_info_miss(check_zip)
                if body_script:
                    body_script += f",\n{_column_physical_name} {_column_type} COMMENT '{_column_comment}'"
                else:
                    body_script += f"{_column_physical_name} {_column_type} COMMENT '{_column_comment}'"
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: DDL body built successful.")
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
        # Check table required information
        _check_key_list = [
            cf.TABLE_HEADER_STRUCTURE[10][0]
        ]
        _check_value_list = [
            _data_file_location
        ]
        check_zip = zip(_check_key_list, _check_value_list)
        fe.table_info_miss(check_zip)
        # Header script
        header_script = f"CREATE EXTERNAL TABLE `{_database_name}.{_table_name}`("
        # Tail script
        tail_script += ")"
        # Table comment
        tail_script += f"\nCOMMENT '{_table_comment}'"
        # Partition
        if _partitioned_by:
            tail_script += f"\nPARTITIONED BY (\n{_partitioned_by}\n)"
        else:
            pass
        # Row format serde
        tail_script += f"\nROW FORMAT SERDE '{_row_format_serde}'"
        # CSV or Excel
        if _row_format_serde == cf.ROW_FORMAT_SERDE_LIST[0][1]:
            # With Serde Properties
            tail_script += f"\n{_with_serdeproperties}"
        else:
            pass
        # STORED AS
        tail_script += f"\n{_store_as}"
        # External table location
        tail_script += f"\nLOCATION '{_data_file_location}'"
        # CSV or Excel
        if _row_format_serde == cf.ROW_FORMAT_SERDE_LIST[1][1]:
            # Table properties
            tail_script += f"\n{_table_properties}"
        else:
            pass
        # Table Properties
        tail_script += "\nTBLPROPERTIES ( 'skip.header.line.count'='1')" \
                       "\n;"
        return header_script, tail_script

    @staticmethod
    def tail_landing_internal(table, partition_key_list):
        tail_script = ""
        _table = Table(table)
        _database_name = _table.database_name()
        _table_name = _table.table_name()
        _table_comment = _table.table_comment()
        _row_format_serde = _table.row_format_serde()
        _data_file_location = _table.data_file_location()
        _partitioned_by = _table.partitioned_by(partition_key_list)
        _store_as = _table.store_as()
        _with_serdeproperties = _table.with_serdeproperties()
        # Header script
        header_script = f"DROP TABLE IF EXISTS `{_database_name}.{_table_name}`;" \
                        f"\nCREATE TABLE IF NOT EXISTS `{_database_name}.{_table_name}`("
        # Tail script
        tail_script = tail_script + ")"
        # Table comment
        tail_script += f"\nCOMMENT '{_table_comment}'"
        # Partition
        if _partitioned_by:
            tail_script += f"\nPARTITIONED BY (\n{_partitioned_by}\n)"
        else:
            pass
        # Row format serde
        tail_script += f"\nROW FORMAT SERDE '{_row_format_serde}'"
        # With Serde Properties
        tail_script += f"\n{_with_serdeproperties}"
        # STORED AS
        tail_script += f"\n{_store_as}" \
                       f"\n;"
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
        header_script = f"DROP TABLE IF EXISTS `{_database_name}.{_table_name}`;" \
                        f"\nCREATE TABLE IF NOT EXISTS `{_database_name}.{_table_name}`("
        # Tail script
        tail_script = tail_script + ")"
        # Table comment
        tail_script += f"\nCOMMENT '{_table_comment}'"
        # Partition
        if _partitioned_by:
            tail_script += f"\nPARTITIONED BY (\n{_partitioned_by}\n)"
        else:
            pass
        # Cluster
        if _clustered_by and _sorted_by and _buckets_number:
            tail_script += f"\nCLUSTERED BY ({_clustered_by}) SORTED BY ({_sorted_by}) INTO {_buckets_number} BUCKETS"
        else:
            pass
        # Row format serde
        tail_script += f"\nROW FORMAT SERDE '{_row_format_serde}'"
        # STORED AS
        tail_script += f"\n{_store_as}" \
                       f"\n;"
        return header_script, tail_script
