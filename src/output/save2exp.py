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
            name,
            text
    ):
        self.name = name
        self.text = text

    def file_save(self):
        file = os.path.join(cf.EXP, '{}.hql'.format(self.name))
        with open(file, 'w') as f:
            f.write('\n' + str(self.text))
