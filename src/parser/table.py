#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-05-19
Purpose:
    Table Definition
"""

import conf.configuration as cf
import src.error.file as fe
import pandas as pd
import os


class TableInfo:
    def __init__(
            self,
            config,
            excel=None
    ):
        self.config = config
        self.excel = excel
        self.header_read_csv = os.path.join(cf.DATA, 'Header.csv')
        self.body_read_csv = os.path.join(cf.DATA, 'Body.csv')
        self.header_write_csv = os.path.join(cf.EXP, 'Header.csv')
        self.body_write_csv = os.path.join(cf.EXP, 'Body.csv')

    def read_tables(self):
        if self.config == cf.TABLE_INFO_FROM_CONFIG_LIST[0]:
            table_info = []
            if self.excel.physical_table_list:
                try:
                    for table in self.excel.physical_table_list:
                        _table_header = self.excel.read_table_heard(table)
                        _table_body = self.excel.read_table_body(table)
                        table_info.append([_table_header, _table_body])
                    return table_info
                except Exception as e:
                    print(e)
            else:
                fe.sheet_miss()
        elif self.config == cf.TABLE_INFO_FROM_CONFIG_LIST[1]:
            table_info = self.table_info_from_dataframe()
            return table_info
        else:
            pass

    table_info = property(read_tables)

    def table_info_to_dataframe(self):
        _table_info = self.table_info
        header_df = pd.DataFrame()
        body_df = pd.DataFrame()
        for table in range(len(_table_info)):
            _header_value_list = _table_info[table][0]
            _header_list = [
                {
                    cf.TABLE_HEADER_STRUCTURE[0][0]: _header_value_list[0],
                    cf.TABLE_HEADER_STRUCTURE[1][0]: _header_value_list[1],
                    cf.TABLE_HEADER_STRUCTURE[2][0]: _header_value_list[2],
                    cf.TABLE_HEADER_STRUCTURE[3][0]: _header_value_list[3],
                    cf.TABLE_HEADER_STRUCTURE[4][0]: _header_value_list[4],
                    cf.TABLE_HEADER_STRUCTURE[5][0]: _header_value_list[5],
                    cf.TABLE_HEADER_STRUCTURE[6][0]: _header_value_list[6],
                    cf.TABLE_HEADER_STRUCTURE[7][0]: _header_value_list[7],
                    cf.TABLE_HEADER_STRUCTURE[8][0]: _header_value_list[8],
                    cf.TABLE_HEADER_STRUCTURE[9][0]: _header_value_list[9],
                    cf.TABLE_HEADER_STRUCTURE[10][0]: _header_value_list[10],
                    cf.TABLE_HEADER_STRUCTURE[11][0]: _header_value_list[11],
                    cf.TABLE_HEADER_STRUCTURE[12][0]: _header_value_list[12],
                    cf.TABLE_HEADER_STRUCTURE[13][0]: _header_value_list[13],
                    cf.TABLE_HEADER_STRUCTURE[14][0]: _header_value_list[14]
                }
            ]
            header_df = header_df.append(pd.DataFrame(_header_list))
            _body_df = _table_info[table][1]
            _body_df[cf.TABLE_HEADER_STRUCTURE[0][0]] = _header_value_list[0]
            _body_df[cf.TABLE_HEADER_STRUCTURE[1][0]] = _header_value_list[1]
            body_df = body_df.append(_body_df)
        return header_df, body_df

    def table_info_from_dataframe(self):
        table_info = []
        _header_df, _body_df = self.read_csv()
        for index_1, row_1 in _header_df.iterrows():
            _sub_header_list = row_1.to_list()
            _sub_body_df = _body_df[
                (_body_df[cf.TABLE_HEADER_STRUCTURE[0][0]] == row_1[cf.TABLE_HEADER_STRUCTURE[0][0]]) &
                (_body_df[cf.TABLE_HEADER_STRUCTURE[1][0]] == row_1[cf.TABLE_HEADER_STRUCTURE[1][0]])
            ].drop([cf.TABLE_HEADER_STRUCTURE[0][0], cf.TABLE_HEADER_STRUCTURE[1][0]], axis=1)
            table_info.append([_sub_header_list, _sub_body_df])
        return table_info

    def write_csv(self):
        header_df, body_df = self.table_info_to_dataframe()
        header_df.to_csv(
            self.header_write_csv,
            index=False, mode='w', encoding='utf-8',
        )
        body_df.to_csv(
            self.body_write_csv,
            index=False, mode='w', encoding='utf-8',
        )

    def read_csv(self):
        header_df = pd.read_csv(
            self.header_read_csv
        )
        body_df = pd.read_csv(
            self.body_read_csv
        )
        return header_df, body_df


class Table:
    def __init__(self, info):
        self.info = info

    def database_name(self):
        """

        :param self:
        """
        database_name = str(self.info[cf.TABLE_HEADER_STRUCTURE[0][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[0][0], database_name)
        fe.table_info_miss(check_zip)
        return database_name

    def table_name(self):
        """

        :param self:
        """
        table_name = str(self.info[cf.TABLE_HEADER_STRUCTURE[1][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[1][0], table_name)
        fe.table_info_miss(check_zip)
        return table_name

    def table_comment(self):
        """

        :param self:
        """
        table_comment = str(self.info[cf.TABLE_HEADER_STRUCTURE[2][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[2][0], table_comment)
        fe.table_info_miss(check_zip)
        return table_comment

    def table_layer(self):
        """

        :param self:
        """
        table_layer = str(self.info[cf.TABLE_HEADER_STRUCTURE[3][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[3][0], table_layer)
        fe.table_info_miss(check_zip)
        return table_layer

    def table_type(self):
        """

        :param self:
        """
        table_type = str(self.info[cf.TABLE_HEADER_STRUCTURE[4][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[4][0], table_type)
        fe.table_info_miss(check_zip)
        return table_type

    def row_format_serde(self):
        """

        :param self:
        """
        row_format_delimiter = str(self.info[cf.TABLE_HEADER_STRUCTURE[5][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[5][0], row_format_delimiter)
        fe.table_info_miss(check_zip)
        for i in range(len(cf.ROW_FORMAT_SERDE_LIST)):
            if row_format_delimiter == cf.ROW_FORMAT_SERDE_LIST[i][0]:
                row_format_delimiter = cf.ROW_FORMAT_SERDE_LIST[i][1]
                break
            else:
                pass
        return row_format_delimiter

    def field_delim(self):
        """

        :param self:
        """
        field_delim = str(self.info[cf.TABLE_HEADER_STRUCTURE[6][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[6][0], field_delim)
        fe.table_info_miss(check_zip)
        return field_delim

    def quote_char(self):
        """

        :param self:
        """
        quote_char = str(self.info[cf.TABLE_HEADER_STRUCTURE[7][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[7][0], quote_char)
        fe.table_info_miss(check_zip)
        return quote_char

    def separator_char(self):
        """

        :param self:
        """
        separator_char = str(self.info[cf.TABLE_HEADER_STRUCTURE[8][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[8][0], separator_char)
        fe.table_info_miss(check_zip)
        return separator_char

    def serialization_encoding(self):
        """

        :param self:
        """
        serialization_encoding = str(self.info[cf.TABLE_HEADER_STRUCTURE[9][1][0]]).strip()
        check_zip = zip(cf.TABLE_HEADER_STRUCTURE[9][0], serialization_encoding)
        fe.table_info_miss(check_zip)
        return serialization_encoding

    def data_file_location(self):
        """

        :param self:
        """
        if not pd.isnull(self.info[cf.TABLE_HEADER_STRUCTURE[10][1][0]]):
            data_file_location = str(self.info[cf.TABLE_HEADER_STRUCTURE[10][1][0]]).strip()
        else:
            data_file_location = ""
        if (
                self.table_type() == cf.TABLE_TYPE_LIST[0]
        ):
            _script_format = "/user/hive/warehouse/{}.db/{}"
            data_file_location = _script_format.format(self.database_name(), self.table_name())
        else:
            pass
        return data_file_location

    @staticmethod
    def partitioned_by(partition_key_list):
        """

        :param partition_key_list:
        """
        partitioned_by = ""
        for i in partition_key_list:
            if partitioned_by:
                _script_format = ",\n  `{}` string"
                _partitioned_by = _script_format.format(i)
                partitioned_by = partitioned_by + _partitioned_by
            else:
                _script_format = "  `{}` string"
                _partitioned_by = _script_format.format(i)
                partitioned_by = partitioned_by + _partitioned_by
        return partitioned_by

    def clustered_by(self):
        """

        :param self:
        """
        if not pd.isnull(self.info[cf.TABLE_HEADER_STRUCTURE[11][1][0]]):
            clustered_by = str(self.info[cf.TABLE_HEADER_STRUCTURE[11][1][0]]).strip()
        else:
            clustered_by = ""
        return clustered_by

    def sorted_by(self):
        """

        :param self:
        """
        if not pd.isnull(self.info[cf.TABLE_HEADER_STRUCTURE[12][1][0]]):
            sorted_by = str(self.info[cf.TABLE_HEADER_STRUCTURE[12][1][0]]).strip()
        else:
            sorted_by = ""
        return sorted_by

    def buckets_number(self):
        """

        :param self:
        """
        if not pd.isnull(self.info[cf.TABLE_HEADER_STRUCTURE[13][1][0]]):
            buckets_number = str(self.info[cf.TABLE_HEADER_STRUCTURE[13][1][0]]).strip()
        else:
            buckets_number = ""
        return buckets_number

    def store_as(self):
        """

        :param self:
        """
        if self.table_layer() == cf.TABLE_LAYER_LIST[0]:
            if self.row_format_serde() == cf.ROW_FORMAT_SERDE_LIST[0][1]:
                file = os.path.join(cf.CONF_FILE, 'src_database_table_storeas_csv.txt')
                with open(file, 'r') as f:
                    store_as = f.read()
            elif self.row_format_serde() == cf.ROW_FORMAT_SERDE_LIST[1][1]:
                file = os.path.join(cf.CONF_FILE, 'src_database_table_storeas_excel.txt')
                with open(file, 'r') as f:
                    store_as = f.read()
            elif self.row_format_serde() == cf.ROW_FORMAT_SERDE_LIST[2][1]:
                file = os.path.join(cf.CONF_FILE, 'src_database_table_storeas_text.txt')
                with open(file, 'r') as f:
                    store_as = f.read()
        else:
            file = os.path.join(cf.CONF_FILE, 'src_database_table_storeas_parquet.txt')
            with open(file, 'r') as f:
                store_as = f.read()
        return store_as

    def table_properties(self):
        """

        :param self:
        """
        if self.table_layer() == cf.TABLE_LAYER_LIST[0]:
            if self.row_format_serde() == cf.ROW_FORMAT_SERDE_LIST[0][1]:
                table_properties = ""
            elif self.row_format_serde() == cf.ROW_FORMAT_SERDE_LIST[1][1]:
                file = os.path.join(cf.CONF_FILE, 'src_database_table_tblproperties_excel.txt')
                with open(file, 'r') as f:
                    table_properties = f.read()
        else:
            file = os.path.join(cf.CONF_FILE, 'src_database_table_tblproperties_parquet.txt')
            with open(file, 'r') as f:
                table_properties = f.read()
        return table_properties

    def with_serdeproperties(self):
        """

        :param self:
        """
        if (
                self.table_layer() == cf.TABLE_LAYER_LIST[0] and
                self.table_type() == cf.TABLE_TYPE_LIST[0]
        ):
            file = os.path.join(cf.CONF_FILE, 'src_database_table_withserdeproperties_text.txt')
            with open(file, 'r') as f:
                with_serdeproperties = f.read()
        else:
            with_serdeproperties = "WITH SERDEPROPERTIES\n("
            _script_format = "\n  'field.delim'='{}',"
            _with_serdeproperties = _script_format.format(self.field_delim())
            with_serdeproperties = with_serdeproperties + _with_serdeproperties
            _script_format = "\n  'quoteChar'='{}',"
            _with_serdeproperties = _script_format.format(self.quote_char())
            with_serdeproperties = with_serdeproperties + _with_serdeproperties
            _script_format = "\n  'separatorChar'='{}',"
            _with_serdeproperties = _script_format.format(self.separator_char())
            with_serdeproperties = with_serdeproperties + _with_serdeproperties
            _script_format = "\n  'serialization.encoding'='{}'"
            _with_serdeproperties = _script_format.format(self.serialization_encoding())
            with_serdeproperties = with_serdeproperties + _with_serdeproperties
            with_serdeproperties = with_serdeproperties + "\n)"
        return with_serdeproperties
