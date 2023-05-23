# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:20:15 2018

@author: partha
"""

# FUNCTION
import os
import subprocess 
import numpy as np
import linecache
import time
from get_line_number import get_line_number
            
def objfunction (x):


    #x=[-41181.8984, -2.1, 433813.0702, 50933.3099]
    #x=[-41180.8984, -3.1, 433815.0702, 50935.3099];

    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    PF=200000  # Penalty Factor         
    MQ=np.matrix([[2,  0,  0,  0,  0], [2,  0,  0,  0,  0] , [1, 2, 2,  x1, 0], [1,  4,  5,  x2,  0]])
    np.savetxt('EX2a-Sce1a-RevisedForQUAL2KW.WEL', MQ, fmt='%0.0f', delimiter=',')
    ##############################################################################       
    Mr1=np.array((14,5,2,2,1,86400,-1,0,0,0), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<i4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr2=np.array((14,0,0,0,0,0,0,0,0,0), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<i4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr3=np.array((1,3,1,1,1,624000,53.07,80,49.7,50.1), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])

    Mr4=np.array((1,3,2,1,2,0,53.05,40000,49.5,49.9), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr5=np.array((1,3,2,1,3,0,53.05,0,49.5,50), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr6=np.array((1,3,2,2,1,x3,53.05,800,49.5,49.9), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])

    Mr7=np.array((1,3,2,3,1,-1,53.05,0,49.5,49.9), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr8=np.array((1,3,2,3,2,0,53.05,40000,49.4,49.8), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr9=np.array((1,3,3,3,3,0,53.05,0,49,49.8), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])

    Mr10=np.array((1,3,4,3,4,0,53.04,40000,49.3,49.7), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr11=np.array((1,3,4,3,5,0,53.04,0,49.2,49.6), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr12=np.array((1,3,4,4,1,x4,53.04,800,49.3,49.7), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])

    Mr13=np.array((1,3,4,5,1,-1,53.02,0,49.1,49.5), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr14=np.array((1,3,4,5,2,0,53.04,40000,49.2,49.6), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr15=np.array((1,3,5,5,3,0,53.02,80000,49.2,49.6), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])
    Mr16=np.array((1,3,6,5,4,0,53.01,0,49.1,49.5), dtype=[('f0', '<i4'), ('f1', '<i4'), ('f2', '<i4'),('f3', '<i4'),('f4', '<i4'),('f5', '<i4'),('f6', '<f4'),('f7', '<i4'),('f8', '<f4'),('f9', '<f4')])

    Nr1=np.array_str(Mr1)
    Nr2=np.array_str(Mr2)
    Nr3=np.array_str(Mr3)

    Nr4=np.array_str(Mr4)
    Nr5=np.array_str(Mr5)
    Nr6=np.array_str(Mr6)

    Nr7=np.array_str(Mr7)
    Nr8=np.array_str(Mr8)
    Nr9=np.array_str(Mr9)

    Nr10=np.array_str(Mr10)
    Nr11=np.array_str(Mr11)
    Nr12=np.array_str(Mr12)

    Nr13=np.array_str(Mr13)
    Nr14=np.array_str(Mr14)
    Nr15=np.array_str(Mr15)
    Nr16=np.array_str(Mr16)

    Nr1=Nr1[1:-1]
    Nr2=Nr2[1:-1]
    Nr3=Nr3[1:-1]

    Nr4=Nr4[1:-1]
    Nr5=Nr5[1:-1]
    Nr6=Nr6[1:-1]

    Nr7=Nr7[1:-1]
    Nr8=Nr8[1:-1]
    Nr9=Nr9[1:-1]


    Nr10=Nr10[1:-1]
    Nr11=Nr11[1:-1]
    Nr12=Nr12[1:-1]

    Nr13=Nr13[1:-1]
    Nr14=Nr14[1:-1]
    Nr15=Nr15[1:-1]
    Nr16=Nr16[1:-1]

    #N1=np.array_str(M1)
    #np.savetxt('EX2a-Sce1a-RevisedForQUAL2KW.STR',M1,fmt='%d, %d, %d, %d, %d, %d, %d, %d, %0.1f, %0.1f')
    fid=open('EX2a-Sce1a-RevisedForQUAL2KW.STR','w')
    fid.writelines(Nr1)
    fid.writelines('\n')
    fid.writelines(Nr2)
    fid.writelines('\n')
    fid.writelines(Nr3)
    fid.writelines('\n')


    fid.writelines(Nr4)
    fid.writelines('\n')
    fid.writelines(Nr5)
    fid.writelines('\n')
    fid.writelines(Nr6)
    fid.writelines('\n')

    fid.writelines(Nr7)
    fid.writelines('\n')
    fid.writelines(Nr8)
    fid.writelines('\n')
    fid.writelines(Nr9)
    fid.writelines('\n')

    fid.writelines(Nr10)
    fid.writelines('\n')
    fid.writelines(Nr11)
    fid.writelines('\n')
    fid.writelines(Nr12)
    fid.writelines('\n')

    fid.writelines(Nr13)
    fid.writelines('\n')
    fid.writelines(Nr14)
    fid.writelines('\n')
    fid.writelines(Nr15)
    fid.writelines('\n')
    fid.writelines(Nr16)
    fid.writelines('\n')

#############################################
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('10,0.002,0.03,0,0,0,0,0,0,0\n')
    fid.writelines('0,0,0,0,0,0,0,0,0,0\n')
    fid.writelines('0,0,0,0,0,0,0,0,0,0\n')
    fid.writelines('1,0,0,0,0,0,0,0,0,0\n')
    fid.writelines('0,0,0,0,0,0,0,0,0,0\n')
    fid.writelines('3,0,0,0,0,0,0,0,0,0\n')
    fid.writelines('0,0,0,0,0,0,0,0,0,0\n')
    fid.writelines('1,0,0,0,0,0,0,0,0,0\n')
    fid.writelines('0,0,0,0,0,0,0,0,0,0\n')
    fid.writelines('3,0,0,0,0,0,0,0,0,0\n')
    fid.writelines('0,0,0,0,0,0,0,0,0,0\n')
    fid.close()
    #dtype=np.int32;
    #os.system("cmd /k mf2005 EX2a-Sce1a-RevisedForQUAL2KW.nam ")        
    subprocess.run("mf2005 EX2a-Sce1a-RevisedForQUAL2KW.nam")
    break_point=1
#########################################################################################################################################################################
    head_matrix=np.loadtxt('EX2a-Sce1a-RevisedForQUAL2KW.fhd',skiprows=1,usecols=range(0,6))
    head_response1=head_matrix.item(1,1)
    head_response2=head_matrix.item(3,4)
    head_response=[head_response1, head_response2]



    penlt_head=np.zeros(2)

    for ii in range(2): 
        if head_response[ii]<=46 or head_response[ii]>=55:
            penlt_head[ii]=1
        else:
            penlt_head[ii]=0
        penlt_head_sum=np.sum(penlt_head)
        ###############################################################################
    linenumber1=get_line_number('1         3         2         3         1','EX2a-Sce1a-RevisedForQUAL2KW-STR.LST') 
    linenumber3=get_line_number('1         3         3         3         3','EX2a-Sce1a-RevisedForQUAL2KW-STR.LST') 
    linenumber2=get_line_number('1         3         4         5         1','EX2a-Sce1a-RevisedForQUAL2KW-STR.LST') 
    linenumber4=get_line_number('1         3         6         5         4','EX2a-Sce1a-RevisedForQUAL2KW-STR.LST') 
#   linenumber5=get_line_number('STREAM LEAKAGE','EX2a-Sce1a-RevisedForQUAL2KW-STR.LST')+10  # #add +10 with it, There are two occurance of the string in this file. we need the 2nd one.



    line_Ex1=linecache.getline('EX2a-Sce1a-RevisedForQUAL2KW-STR.LST', linenumber1)
    line_Ex2=linecache.getline('EX2a-Sce1a-RevisedForQUAL2KW-STR.LST', linenumber2)
    line_Ex3=linecache.getline('EX2a-Sce1a-RevisedForQUAL2KW-STR.LST', linenumber3)
    line_Ex4=linecache.getline('EX2a-Sce1a-RevisedForQUAL2KW-STR.LST', linenumber4)
#    line_Ex5=linecache.getline('EX2a-Sce1a-RevisedForQUAL2KW-STR.LST', linenumber5)

    line_Str1=line_Ex1[88:104]
    line_Str2=line_Ex2[88:104]
    line_Str3=line_Ex3[88:104]
    line_Str4=line_Ex4[88:104]
#    line_Str5=line_Ex5[26:45]


    linestr_float1=float(line_Str1)
    linestr_float2=float(line_Str2)
    linestr_float3=float(line_Str3)
    linestr_float4=float(line_Str4)
#    linestr_float5=float(line_Str5)

    linestr_float=np.array([linestr_float1,linestr_float2,linestr_float3,linestr_float4])


    if linestr_float1<=0:
        penlt_str1=1
    else:
        penlt_str1=0  
   
    if linestr_float2<=0:
        penlt_str2=1
    else:
        penlt_str2=0

    if linestr_float3<=150000:
        penlt_str3=1
    else:
        penlt_str3=0 

    if linestr_float4<=100000:
        penlt_str4=1
    else:
        penlt_str4=0

    penlt_str_sum=penlt_str1+penlt_str2+penlt_str3+penlt_str4  

    ############################################################################################################################################      
 
#    stream_leakage=linestr_float5
#    if stream_leakage<7500:
#        Penalty=stream_leakage*PF
#    else:
#        Penalty=0   
    
    F=x1+x2-(x3+x4)+PF*(penlt_head_sum+penlt_str_sum)
    linecache.clearcache()   # This Line is important  
    return F      

#################################################################################################################################################
#Optimization Starts From Here
#        
#from pyswarm import pso
#lb=[-50000, -50000, 0,  0] 
#ub=[0, 0, 500000, 100000] 
#xopt, fopt = pso(objfunction, lb, ub)  

#xopt, fopt=pso(objfunction, lb, ub, ieqcons=[], f_ieqcons=None, args=(), kwargs={},
#    swarmsize=20, omega=0.5, phip=0.5, phig=0.5, maxiter=20, minstep=1e-2,
#    minfunc=1e-2, debug=False)     
  