import pandas as pd


def stockAvg(df_Stock,df_result_set):
    df_temp = pd.DataFrame(df_Stock.mean().round(2))    #Calculating Mean of all Stocks
    df_temp.columns =  ['Mean']                         #Naming the column as 'Mean'
    return df_result_set.join(df_temp)                  #Joining Mean data to the given set