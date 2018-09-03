#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 21:19:53 2018

@author: Prabz
"""
import pandas as pd
import numpy as np

def to_file(pframe,fname,fileformat,str_trade_date,x_writer=np.nan):
    if(pd.notna(x_writer)):
        writer = x_writer
    else:
        writer = pd.ExcelWriter("Strat1_{}.xlsx".format(str_trade_date))
    if fileformat == "CSV":
        #pframe.dropna(how='all')
        pframe.to_csv("{}_{}.csv".format(fname,str_trade_date))
        writer = np.nan
        
    if fileformat == "EXCEL":
        pframe.to_excel(writer,fname)
        pframe.to_excel(writer,"here")
        writer.save()
    
    return writer   