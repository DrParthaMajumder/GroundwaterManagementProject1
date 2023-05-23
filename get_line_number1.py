# -*- coding: utf-8 -*-
"""
Created on Tue May  1 01:01:21 2018

@author: partha
"""

def get_line_number1(phrase, file_name):
    with open(file_name) as f:
        for i, line in enumerate(f, 11):
            if phrase in line:
                return i
           
            
linenumber5=get_line_number1('STREAM LEAKAGE','EX2a-Sce1a-RevisedForQUAL2KW-STR.LST') 














        
        
        
        
  
        
        