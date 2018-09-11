# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 15:21:08 2018

@author: ppadayac
"""
import numpy as np
import datetime
import importlib
import read_Stock_Data as rd
importlib.reload(rd)  
import pandas as pd
excel_file = 'D:\\ppadayac\\PraChin\\InvestValue.xlsx'

movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
Dates = movies_sheet1.index

df_nse50 = rd.get_list('nse_Top50', 'Symbol')                   #Extract list of Top Nse50 Stcoks
list_nse50 = df_nse50.index.tolist() 
df_Stock = rd.get_data(list_nse50[0:50],datetime.date.today(),365)  

columns_buy = movies_sheet1['Buy'].tolist()
columns_sell = movies_sheet1['Sell'].tolist()
buy_size = movies_sheet1['BuySize'].tolist()
sell_size = movies_sheet1['Sell Size'].tolist()

date_range = pd.date_range(start= Dates[1],end=Dates[2])    
new_df = df_Stock.loc[np.concatenate((Dates.tolist(),date_range.tolist()),axis=0),np.concatenate((columns_buy,columns_sell),axis=0)]
one = np.concatenate((buy_size,sell_size),axis=0)
new_df * one
print(df_Stock)