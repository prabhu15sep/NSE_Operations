#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 20:43:26 2018

@author: Prabz
"""
*************************
    if int(input_list.count()) < 5:
        return np.NaN
    
    
    
    temp_1 = (input_list.apply(lambda x: x.sort_values(ascending=False)).iloc[2:3,:].values)[0,0]
    return  temp_1

temp_1 = (input_list.apply(lambda x: x.sort_values(ascending=False)).iloc[2:3,:].values)[0,0]
   ******************
   
   import pandas as pd
import datetime
import importlib
import numpy as np


import read_Stock_Data as rd
importlib.reload(rd)                                                #Reload file to cater for any recent changes in the file

import stock_formulae as frm
importlib.reload(frm) 

def find_nlargest(input_list):
    test = input_list.copy()
    if sum(~np.isnan(x) for x in test) < 5:
        return np.NaN
    test[::-1].sort()   
    return  test[2]


def test_run():
    ######Reading Data###################
    df_nse50 = rd.get_list('nse_Top50', 'Symbol')                   #Extract list of Top Nse50 Stcoks
    list_nse50 = df_nse50.index.tolist()                            #Array of Stcok symbols
    
    df_Stock = rd.get_data(list_nse50[0:20],datetime.date.today(),50)        #Extract Data from a given date to past x no of traded days
    #test = find_nlargest(df_Stock.iloc[:,:1])
    #print(df_Stock.iloc[:25,:1])
    
    hello_1 = df_Stock.rolling(window=5, min_periods=5, center=False).apply(lambda x: find_nlargest(x))
    print(df_Stock.iloc[:50,:1])
    print(hello_1)
    
if __name__ == "__main__":
    test_run()
    ***********************************************
    
    list_set = fnmatch.filter(os.listdir(yahoo_files_path), '{}*.csv'.format(symbol)) 