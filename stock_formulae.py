import pandas as pd


def stockAvg(df_Stock,df_result_set):
    df_temp = pd.DataFrame(df_Stock.mean().round(3))    #Calculating Mean of all Stocks
    df_temp.columns =  ['Mean']                         #Naming the column as 'Mean'
    return df_result_set.join(df_temp)                  #Joining Mean data to the given set

def stockRet(df_Stock,df_result_set,day):
    df_temp =(df_Stock/df_Stock.shift(day)) -1                       #Calculating Return of all Stocks
    df_temp = df_temp.round(3)
    df_temp = (df_temp[-1:]).T                                       #Transpose
    df_temp.columns =  ['Return']                                    #Naming the column as 'Return'
    return df_result_set.join(df_temp)                               #Joining Mean data to the given set

def modstockRet(df_Stock,day):
    df_temp =(df_Stock/df_Stock.shift(day)) -1                       #Calculating Return of all Stocks
    df_temp = df_temp.tail(50).abs()                                     #Transpose
    return df_temp
