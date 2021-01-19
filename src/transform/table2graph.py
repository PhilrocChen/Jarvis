#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2021-01-07
Purpose:
    Get table information and save to graph
"""

import datetime
import conf.configuration as cf
import conf.graphviz.graph as gf
import conf.graphviz.node as nd
import conf.graphviz.edge as eg
import pandas as pd
from src.parser.table import Table
from src.generator.save2exp import Save2Exp


class Table2Graph:

    def __init__(
            self,
            table_info
    ):
        self.table_info = table_info

    def get_tables(self, database_table_name=None, depth=1, with_name=None, without_name=None):
        graph = gf.Graph()
        node = nd.Node()
        edge = eg.Edge()
        # Generate header
        file_name = "JavisGraphDot"
        file_header = f"//  Description: Jarvis auto generation" \
                      f"\n//  Author: Jarvi" \
                      f"\n//  Last Modified: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        # Generate graph
        file_header += f"\n\ndigraph models_diagram""{" \
                       f"\n    graph[" \
                       f"layout={graph.set_layout()}, " \
                       f"rankdir={graph.set_rankdir()}, " \
                       f"overlap={graph.set_overlap()}, " \
                       f"splines={graph.set_splines()}];" \
                       f"\n    node [" \
                       f"shape={node.set_shape()}, " \
                       f"fontsize={node.set_fontsize()}, " \
                       f"fontname=\"{node.set_fontname()}\"];" \
                       f"\n    edge [" \
                       f"style={edge.set_style()}" \
                       f"];"
        file_body, relation_script, relation_df = self.get_file_body()
        if database_table_name:
            # Filter on specific tables and reprocess
            database_table_name_list = [database_table_name]
            dp = 0
            while dp < depth:
                database_table_name_list = self.get_database_table_name_list(database_table_name_list, relation_df)
                dp = dp + 1
            if with_name:
                database_table_name_list = self.get_list_with_name(database_table_name_list, with_name)
            else:
                pass
            if without_name:
                database_table_name_list = self.get_list_without_name(database_table_name_list, without_name)
            else:
                pass
            file_body, relation_script, relation_df = self.get_file_body(database_table_name_list)
        else:
            pass
        file_body = file_body + relation_script
        file_tail = "}"
        script = f"{file_header}\n{file_body}\n{file_tail}"
        file_save = Save2Exp(cf.SAVE2EXP_FILE_TYPE_LIST[1], file_name, script)
        file_save.file_save()
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: Script generated successfully: {file_name}")

    @staticmethod
    def get_database_table_name_list(database_table_name_list, relation_df):
        # Filter on specific tables and reprocess
        _filter_relation_df = pd.DataFrame()
        for database_table_name in database_table_name_list:
            _sub_filter_relation_df = relation_df[
                (relation_df['table_name_from'] == database_table_name) |
                (relation_df['table_name_to'] == database_table_name)
                ]
            _filter_relation_df = pd.concat([_filter_relation_df, _sub_filter_relation_df])
        _from_table_list = list(set(_filter_relation_df['table_name_from']))
        _to_table_list = list(set(_filter_relation_df['table_name_to']))
        database_table_name_list = list(set(_from_table_list + _to_table_list))
        return database_table_name_list

    @staticmethod
    def get_list_with_name(database_table_name_list, with_name):
        _database_table_name_list = []
        for database_table_name in database_table_name_list:
            if with_name in database_table_name:
                _database_table_name_list.append(database_table_name)
            else:
                pass
        database_table_name_list = _database_table_name_list
        return database_table_name_list

    @staticmethod
    def get_list_without_name(database_table_name_list, without_name):
        _database_table_name_list = []
        for database_table_name in database_table_name_list:
            if without_name not in database_table_name:
                _database_table_name_list.append(database_table_name)
            else:
                pass
        database_table_name_list = _database_table_name_list
        return database_table_name_list

    def get_file_body(self, database_table_name_list=None):
        file_body = ""
        table_id = 0
        table_df = pd.DataFrame(
            columns=(
                'table',
                'column',
                'table_name',
                'column_name',
                'foreign_key'
            )
        )
        for table in self.table_info:
            # transform body
            table_id, _entity_script, table_df = self.create_entity(
                table_id, table[0], table[1], table_df, database_table_name_list)
            file_body = file_body + _entity_script
        relation_script, relation_df = self.create_relation(table_df)
        return file_body, relation_script, relation_df

    @staticmethod
    def create_entity(table_id, table_header, table_body, table_df, database_table_name_list=None):
        entity_script = ""
        _table = Table(table_header)
        _database_name = _table.database_name()
        _table_name = _table.table_name()
        if (
                (
                        database_table_name_list and
                        (_database_name + '.' + _table_name) in database_table_name_list
                ) or
                not database_table_name_list
        ):
            entity_script += f"\n  table{table_id} [shape=none, margin=0, label=<" \
                             f"\n    " \
                             f"<table border=\"0\" " \
                             f"cellborder=\"1\" " \
                             f"cellspacing=\"0\" " \
                             f"cellpadding=\"4\">"
            if (
                    "_fact_" in _table_name or
                    "rpt_" in _table_name
            ):
                entity_script += f"\n        <tr><td bgcolor=\"#FCE6C9\">{_database_name}.{_table_name}</td></tr>"
            elif "_dim_" in _table_name:
                entity_script += f"\n        <tr><td bgcolor=\"#F0FFF0\">{_database_name}.{_table_name}</td></tr>"
            else:
                entity_script += f"\n        <tr><td bgcolor=\"#C0C0C0\">{_database_name}.{_table_name}</td></tr>"
            _port = 0
            for index, row in table_body.iterrows():
                _column_physical_name = str(row[cf.TABLE_BODY_STRUCTURE[1]]).strip()
                _column_type = str(row[cf.TABLE_BODY_STRUCTURE[2]]).strip()
                _foreign_key = str(row[cf.TABLE_BODY_STRUCTURE[4]]).strip()
                entity_script += f"\n        <tr><td port=\"{_port}\" align=\"left\">" \
                                 f"{_column_physical_name}: {_column_type}</td></tr>"
                if _foreign_key != "nan":
                    table_df = table_df.append(pd.DataFrame(
                        {
                            'table': ["table" + str(table_id)],
                            'column': [_port],
                            'table_name': [_database_name + "." + str(_table_name)],
                            'column_name': [_column_physical_name],
                            'foreign_key': [_foreign_key]
                        }
                    ))
                _port = _port + 1
            entity_script = entity_script + "\n    </table>>];"
            table_id = table_id + 1
        else:
            pass
        return table_id, entity_script, table_df

    @staticmethod
    def create_relation(table_df):
        relation_script = ""
        relation_df = pd.DataFrame(
            columns=(
                'table_from',
                'table_to',
                'column_from',
                'column_to',
                'table_name_from',
                'table_name_to',
                'column_name_from',
                'column_name_to',
                'foreign_key'
            )
        )
        _tables = set(table_df['table'])
        for table in _tables:
            _table_df = table_df[
                (table_df['table'] == table)
            ]
            for index_1, row_1 in _table_df.iterrows():
                _table_from = row_1['table']
                _column_from = row_1['column']
                _table_name_from = row_1['table_name']
                _column_name_from = row_1['column_name']
                _foreign_key_from = row_1['foreign_key']
                for index_2, row_2 in table_df.iterrows():
                    _table_to = row_2['table']
                    _column_to = row_2['column']
                    _table_name_to = row_2['table_name']
                    _column_name_to = row_2['column_name']
                    _foreign_key_to = row_2['foreign_key']
                    if (
                            _table_from != _table_to and
                            _foreign_key_from == _foreign_key_to and
                            "_dim_" in _table_name_to
                    ):
                        relation_df = relation_df.append(pd.DataFrame(
                            {
                                'table_from': [_table_from],
                                'table_to': [_table_to],
                                'column_from': [_column_from],
                                'column_to': [_column_to],
                                'table_name_from': [_table_name_from],
                                'table_name_to': [_table_name_to],
                                'column_name_from': [_column_name_from],
                                'column_name_to': [_column_name_to],
                                'foreign_key': [_foreign_key_from]
                            }
                        ))
                    else:
                        pass
        relation_df = relation_df.sort_values(
            ascending=True, by=['table_from', 'table_to', 'column_from', 'column_to'])
        for index, row in relation_df.iterrows():
            _table_from = row['table_from']
            _table_to = row['table_to']
            _column_from = row['column_from']
            _column_to = row['column_to']
            relation_script += f"\n  {_table_from}:{_column_from} -> {_table_to}:{_column_to};"
        return relation_script, relation_df
