#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Created by: Philroc Chen
Created on: 2020-03-21
Purpose:
    Save transform to exp
"""

import os
import conf.configuration as cf


class Save2Exp:

    def __init__(
            self,
            file_type,
            name,
            text
    ):
        self.file_type = file_type
        self.name = name
        self.text = text

    def file_save(self):
        if self.file_type == cf.SAVE2EXP_FILE_TYPE_LIST[0]:
            file = os.path.join(cf.EXP, '{}.hql'.format(self.name))
            with open(file, 'w') as f:
                f.write('\n' + str(self.text))
        elif self.file_type == cf.SAVE2EXP_FILE_TYPE_LIST[1]:
            file = os.path.join(cf.EXP, '{}.txt'.format(self.name))
            with open(file, 'w') as f:
                f.write('\n' + str(self.text))
