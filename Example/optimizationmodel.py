# -*- coding: utf-8 -*-
"""
Created on Tue May  1 03:14:42 2018

@author: partha
"""
#import os
#import subprocess 
#import numpy as np
#import linecache
#import time


from pyswarm import pso
from get_line_number import get_line_number  #from file import function
from objfunction import objfunction

print("Optimization Starts from Here: Wait for the Result**************")        
from pyswarm import pso
lb=[-50000, -50000, 0,  0] 
ub=[0, 0, 500000, 100000] 
#xopt, fopt = pso(objfunction, lb, ub) 

xopt, fopt=pso(objfunction, lb, ub, ieqcons=[], f_ieqcons=None, args=(), kwargs={},
    swarmsize=30, omega=0.5, phip=0.5, phig=0.5, maxiter=150, minstep=1e-8,
    minfunc=1e-8, debug=False) 