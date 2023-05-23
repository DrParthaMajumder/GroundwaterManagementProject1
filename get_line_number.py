# -*- coding: utf-8 -*-
"""
Created on Tue May  1 01:01:21 2018

@author: partha
"""

def get_line_number(phrase, file_name):
    with open(file_name) as f:
        for i, line in enumerate(f, 1):
            if phrase in line:
                return i
           