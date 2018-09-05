import pandas as pd
import datetime
import importlib
import numpy as np


import read_Stock_Data as rd
importlib.reload(rd)                                                #Reload file to cater for any recent changes in the file

import stock_formulae as frm
importlib.reload(frm) 

import common as cmn
importlib.reload(cmn)

import rolling_formulae as rf
importlib.reload(rf)



def test_run():
    ######Reading Data###################
    df_nse50 = rd.get_list('nse_Top50', 'Symbol')                   #Extract list of Top Nse50 Stcoks
    list_nse50 = df_nse50.index.tolist()                            #Array of Stcok symbols

    csv = "CSV"
    excel = "EXCEL"
    start_date = datetime.date(2013,1,1)
    end_date = datetime.date.today()      #date.today() datetime.date(2013,12,31)
    
    df_Stock = rd.get_data(list_nse50[0:51],end_date,2000)        #Extract Data from a given date to past x no of traded days
    df_Stock = df_Stock.dropna(how='all') 
        #Formate date to DD/MM/YYYY formate
    df_Stock.index.name = 'Date'
    str_trade_date = ''.join(df_Stock.iloc[-1:,:0].index.strftime('%d.%m.%Y')) 

    #writer = cmn.to_file(df_Stock.sort_index(ascending=False, inplace=False) ,"1_StockPrice",csv,str_trade_date)
    #writer = cmn.to_file(df_Stock.iloc[:2,:2],"StockPrice2",excel,str_trade_date,writer)  

    '''
    rm_200 = rf.get_rolling_mean(df_Stock, window=200)
    #writer = cmn.to_file(rm_200.sort_index(ascending=False, inplace=False),"2_RollMean200",csv,str_trade_date)
    
    rm_50 = rf.get_rolling_mean(df_Stock, window=50)
    #writer = cmn.to_file(rm_50.sort_index(ascending=False, inplace=False),"3_RollMean50",csv,str_trade_date)
    
    day_1_returns = rf.compute_daily_returns(df_Stock,1)
    #writer = cmn.to_file(day_1_returns.sort_index(ascending=False, inplace=False),"4_OneDayRet",csv,str_trade_date)
    
    abs_day_1_returns = day_1_returns.abs()
    #writer = cmn.to_file(abs_day_1_returns.sort_index(ascending=False, inplace=False),"5_OneDayAbsRet",csv,str_trade_date)
    
    rm_abs1day_50 = rf.get_rolling_mean(abs_day_1_returns, window=50)
    
    counter_rm_abs1day_50 = rm_abs1day_50 < 2
    #writer = cmn.to_file(counter_rm_abs1day_50.sort_index(ascending=False, inplace=False),"6_Counter50DayAbsRet",csv,str_trade_date)
    
    
    rd_10DRet = rf.get_rolling_std(day_10_returns, window=1200)
    #writer = cmn.to_file(rd_10DRet.sort_index(ascending=False, inplace=False),"8_10DayRetStdDev",csv,str_trade_date)
    
    day_10_returns = rf.compute_daily_returns(df_Stock,10)
    writer = cmn.to_file(day_10_returns.sort_index(ascending=False, inplace=False),"7_10DayRet",csv,str_trade_date)
    
    ra_10plarge = rf.get_rolling_nAvg(df_Stock,1200,120,120,40)
    writer = cmn.to_file(ra_10plarge.sort_index(ascending=False, inplace=False),"9_10PCLarge",csv,str_trade_date)
    
    ra_10psmall = rf.get_rolling_nAvg(df_Stock,1200,1080,1080,1160)
    writer = cmn.to_file(ra_10psmall.sort_index(ascending=False, inplace=False),"10_10PCSmall",csv,str_trade_date)
 
    ra_3plarge = rf.get_rolling_nAvg(df_Stock,1200,40,40,13)
    writer = cmn.to_file(ra_3plarge.sort_index(ascending=False, inplace=False),"11_3PCLarge",csv,str_trade_date)
 
    ra_3psmall = rf.get_rolling_nAvg(df_Stock,1200,1140,1160,1147)
    writer = cmn.to_file(ra_3psmall.sort_index(ascending=False, inplace=False),"12_3PCSmall",csv,str_trade_date)
 
    ra_15plarge = rf.get_rolling_nAvg(df_Stock,1200,120,180,180)
    writer = cmn.to_file(ra_15plarge.sort_index(ascending=False, inplace=False),"13_15PCLarge",csv,str_trade_date)
 
    ra_15psmall = rf.get_rolling_nAvg(df_Stock,1200,1080,1020,1120)
    writer = cmn.to_file(ra_15psmall.sort_index(ascending=False, inplace=False),"14_15PCSmall",csv,str_trade_date)
 
    array_cntr = np.where(ra_3psmall.isnull() ,np.nan,
                      np.where(day_10_returns*100 <= ra_3psmall/100,3,
                      np.where(day_10_returns*100 <= ra_10psmall/100,2,
                      np.where(day_10_returns*100 <= ra_15psmall/100,1,0))))
    
    indx = ra_15psmall.index.values
    Cntr_10D_Buy = pd.DataFrame(array_cntr,index=indx ,columns=list_nse50)
    writer = cmn.to_file(Cntr_10D_Buy.sort_index(ascending=False, inplace=False),"15_10DCounterBuy",csv,str_trade_date)
    
    
    array_cntr = np.where(ra_3plarge.isnull() ,np.nan,
                      np.where(day_10_returns*100 > ra_3plarge/100,3,
                      np.where(day_10_returns*100 > ra_10plarge/100,2,
                      np.where(day_10_returns*100 > ra_15plarge/100,1,0))))
    
    indx = ra_15plarge.index.values
    Cntr_10D_Sell = pd.DataFrame(array_cntr,index=indx ,columns=list_nse50)
    writer = cmn.to_file(Cntr_10D_Sell.sort_index(ascending=False, inplace=False),"16_10DCounterSell",csv,str_trade_date)
    '''
    rRSI_13 = rf.get_Rolling_RSI(df_Stock,13)
    writer = cmn.to_file(rRSI_13.sort_index(ascending=False, inplace=False),"17_13DRSI",csv,str_trade_date)
    
    array_cntr = np.where(rRSI_13.isnull() ,np.nan,
                      np.where(rRSI_13 <= 15,3,
                      np.where(rRSI_13 <= 25,2,
                      np.where(rRSI_13 <= 35,1,0))))
    
    indx = rRSI_13.index.values
    Cntr_RSI_Buy = pd.DataFrame(array_cntr,index=indx ,columns=list_nse50)
    writer = cmn.to_file(Cntr_RSI_Buy.sort_index(ascending=False, inplace=False),"18_RSICounterBuy",csv,str_trade_date)
   
    array_cntr = np.where(rRSI_13.isnull() ,np.nan,
                      np.where(rRSI_13 > 85,3,
                      np.where(rRSI_13 > 75,2,
                      np.where(rRSI_13 > 65,1,0))))
    
    indx = rRSI_13.index.values
    Cntr_RSI_Sell = pd.DataFrame(array_cntr,index=indx ,columns=list_nse50)
    writer = cmn.to_file(Cntr_RSI_Sell.sort_index(ascending=False, inplace=False),"19_RSICounterSell",csv,str_trade_date)
      
    test_1 = np.where(abs_day_1_returns == day_1_returns,1,0)
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
    df_filter['A<(B/C) '] = np.where(((df_filter[col_A] <= df_filter['B~50DA']) & \
                                      (df_filter[col_A] >= (df_filter['B~50DA'])*0.95)) \
                                    |((df_filter[col_A] <= df_filter['C~200DA']) & \
                                      (df_filter[col_A] >= (df_filter['C~200DA'])*0.95)), 1 , 0)
    
    ########################Criteria 2 to Buy##########
    df_filter['D<-8%'] = np.where(df_filter['D~10DR'] < -0.08, 1 , 0)
    
    ########################Criteria 3 to Buy ##########
    df_filter['E<1.5%'] = np.where(df_filter['E~AR50D'] < 0.015, 1 , 0)   

    ########################Criteria 4 to Buy ##########
    df_filter['F<30%'] = np.where(df_filter['F~RSI'] < 30, 1 , 0)   
    
    ########################Citeria to Sell###########
    df_filter['A>(B/C) '] = np.where(((df_filter[col_A] >= df_filter['B~50DA']) & \
                                      (df_filter[col_A] <= (df_filter['B~50DA'])*1.05)) \
                                    |((df_filter[col_A] >= df_filter['C~200DA']) & \
                                      (df_filter[col_A] <= (df_filter['C~200DA'])*1.05)), 1 , 0)
    
    ########################Criteria 2 to Sell ##########
    df_filter['D>8%'] = np.where(df_filter['D~10DR'] > 0.08, 1 , 0)
    
    ########################Criteria 3 to Sell##########
    df_filter['E>1.5%'] = np.where(df_filter['E~AR50D'] > 0.015, 1 , 0) 
    
    ########################Criteria 4 to Sell ##########
    df_filter['F>70%'] = np.where(df_filter['F~RSI'] > 70, 1 , 0) 
    
    ####################Ranking to Buy/Sell#####
    df_filter['BuyS']   =  df_filter['A<(B/C) '] + df_filter['D<-8%'] + df_filter['E<1.5%'] + df_filter['F<30%']
    
    df_filter['SellS']  =  df_filter['A>(B/C) '] + df_filter['D>8%'] + df_filter['E>1.5%'] + df_filter['F>70%']
    
    pd.set_option('display.max_rows', 500)
    print(df_filter)  
    df_filter.to_csv("TradeCall_{}.csv".format(str_trade_date))
    
if __name__ == "__main__":
    test_run()
    
    test_2 = np.where(ra_3psmall.isnull() ,0,
                      np.where(day_10_returns <= ra_3psmall/100,3,
                      np.where(day_10_returns <= ra_10psmall/100,2,
                      np.where(day_10_returns <= ra_15psmall/100,1,0))))