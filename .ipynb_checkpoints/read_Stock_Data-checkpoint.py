
"""Reads the Stocks symbols and return Dataframe"""

import os
import pandas as pd

def list_to_path(list_name, base_dir="D:\\ppadayac\\PraChin\\db"):    #"D:\\ppadayac\\PraChin\\db"  "/Volumes/2/PyD/"
    """Return CSV file p  ath given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(list_name)))
    
def get_list(list_name,ind_key):
    df = pd.read_csv(list_to_path(list_name), index_col=ind_key,
            parse_dates=True, usecols=['Symbol', 'Series','ISIN Code'], na_values=['nan']) # Extract Symbol,EQ series and Stock Code
    return df

def get_data(symbols,end_date,days):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    dates = pd.date_range(end=end_date, periods=365)                                      #Extract data of 90 days
    df = pd.DataFrame(index=dates)
    for symbol in symbols:
        df_temp = pd.read_csv(list_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Close Price'], na_values=['nan'])    #Extract date and price
        df_temp = df_temp.rename(columns={'Close Price': symbol})                        #Rename Column name with Symbol
        df = df.join(df_temp)
        df = df.dropna(subset=[symbol])                                                  #Remove any blank records
    return df                                                                  #Return last 20 traded days record

    