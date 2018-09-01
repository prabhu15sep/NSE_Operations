# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 17:39:40 2018
Load the Database with NSE Fifty stocks
@author: ppadayac
"""
import pandas as pd
import importlib
from datetime import date
from nsepy import get_history

import read_Stock_Data as rd
importlib.reload(rd)  

df_nse50 = rd.get_list('nse_Top50', 'Symbol')                   #Extract list of Top Nse50 Stcoks
list_nse50 = df_nse50.index.tolist() 

start_date = date(2013,1,1)

#sbin = get_history(symbol="NIFTY",start=start_date,end=date.today(),index=True)
#sbin.to_csv("/Volumes/2/PyD/nsedb/NIFTY.csv") 

#list_nse50 = ['EICHERMOT']

for symbl in list_nse50:
    sbin = get_history(symbol=symbl, start=start_date,end=date.today())
    sbin.to_csv("/Volumes/2/PyD/nsedb/{}.csv".format(str(symbl)))    #D:\\ppadayac\\PraChin\\db\\new\\


#sbin.to_csv("D:\\ppadayac\\PraChin\\db\\SBIN.csv")