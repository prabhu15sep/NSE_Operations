import pandas as pd
import datetime
import importlib
import numpy as np


import read_Stock_Data as rd
importlib.reload(rd)                                                #Reload file to cater for any recent changes in the file

import stock_formulae as frm
importlib.reload(frm) 

def find_nlargest(input_list,n):
    test = input_list.copy()
    if sum(~np.isnan(x) for x in test) < 3:
        return np.NaN
    test.sort()
    desc_test = test[::-1]
    return  desc_test[n-3],desc_test[n-2],desc_test[n-1]


def test_run():
    ######Reading Data###################
    df_nse50 = rd.get_list('nse_Top50', 'Symbol')                   #Extract list of Top Nse50 Stcoks
    list_nse50 = df_nse50.index.tolist()                            #Array of Stcok symbols
    
    df_Stock = rd.get_data(list_nse50[0:20],datetime.date.today(),50)        #Extract Data from a given date to past x no of traded days
    #test = find_nlargest(df_Stock.iloc[:,:1])
    #print(df_Stock.iloc[:25,:1])
    nparray = df_Stock.iloc[:15, :1].values
    hist,edges = np.histogram(nparray,bins=4)
    i,j,k = find_nlargest(hist.tolist(),3)
    
    iloc = hist.tolist().index(i)
    
    if j == i:
        hist[iloc] = -1
        
    jloc = hist.tolist().index(j)
    if k == j:
        hist[jloc] = -1
    
    kloc = hist.tolist().index(k)
    
    print(iloc,jloc,kloc)
    
if __name__ == "__main__":
    test_run()