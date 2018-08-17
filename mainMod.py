import pandas as pd
import datetime
import importlib
import numpy as np

 
    
    df_filter = (frm.stockAvg(df_Stock.tail(200),df_filter)).round(2)        # 2nd Filter of calculating 200 Day Mean by less than 5 percent
    df_filter = df_filter.rename(columns={'Mean': 'C~200DA'}) 
    
    df_filter = frm.stockRet(df_Stock,df_filter,10)                          # 3rd Filter of calculating 10 Day Return
    df_filter = df_filter.rename(columns={'Return': 'D~10DR'}) 
    
    df_filter_temp = frm.modstockRet(df_Stock,1)                             # 4th Filter of calculating Absolute Return of 50 days
    df_filter = frm.stockAvg(df_filter_temp,df_filter) 
    df_filter = df_filter.rename(columns={'Mean': 'E~AR50D'})           
    
    df_filter = (frm.RSI(df_Stock.tail(15),df_filter)).round(2)              # 5th Filter of calculating RSI of 14 days    
    df_filter = df_filter.rename(columns={'RSI': 'F~RSI'}) 
    
    #####################Setting Criteria#######
    
    ########################Citeria 1 to Buy###########
    df_filter['A<(B/C) '] = np.where(((df_filter[CP_Col_name] <= df_filter['B~50DA']) & \
                                      (df_filter[CP_Col_name] >= (df_filter['B~50DA'])*0.95)) \
                                    |((df_filter[CP_Col_name] <= df_filter['C~200DA']) & \
                                      (df_filter[CP_Col_name] >= (df_filter['C~200DA'])*0.95)), 1 , 0)
    
    ########################Criteria 2 to Buy##########
    df_filter['D<-8%'] = np.where(df_filter['D~10DR'] < -0.08, 1 , 0)
    
    ########################Criteria 3 to Buy ##########
    df_filter['E<1.5%'] = np.where(df_filter['E~AR50D'] < 0.015, 1 , 0)   

    ########################Criteria 4 to Buy ##########
    df_filter['F<30%'] = np.where(df_filter['F~RSI'] < 30, 1 , 0)   
    
    ########################Citeria to Sell###########
    df_filter['A>(B/C) '] = np.where(((df_filter[CP_Col_name] >= df_filter['B~50DA']) & \
                                      (df_filter[CP_Col_name] <= (df_filter['B~50DA'])*1.05)) \
                                    |((df_filter[CP_Col_name] >= df_filter['C~200DA']) & \
                                      (df_filter[CP_Col_name] <= (df_filter['C~200DA'])*1.05)), 1 , 0)
    
    ########################Criteria 2 to Sell ##########
    df_filter['D>8%'] = np.where(df_filter['D~10DR'] > 0.08, 1 , 0)
    
    ########################Criteria 3 to Sell##########
    df_filter['E>1.5%'] = np.where(df_filter['E~AR50D'] > 0.015, 1 , 0) 
    
    ########################Criteria 4 to Sell ##########
    df_filter['F>70%'] = np.where(df_filter['F~RSI'] > 70, 1 , 0) 
    
    ####################Ranking to Buy/Sell#####
    df_filter['BuyS']   =  df_filter['A<(B/C) '] + df_filter['D<-8%'] + df_filter['E<1.5%'] + df_filter['F<30%']
    
    df_filter['SellS']  =  df_filter['A>(B/C) '] + df_filter['D>8%'] + df_filter['E>1.5%'] + df_filter['F>70%']
    
    print(df_filter) 
    
    df_filter.to_csv('TradingCalls.csv')                                  #File
    
if __name__ == "__main__":
    test_run()