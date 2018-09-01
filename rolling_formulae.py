#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 19:47:14 2018

@author: Prabz
"""
import os
import numpy as np
import pandas as pd


def get_rolling_mean(df, window):
    """Return rolling mean of given values, using specified window size."""
    #return pd.rolling_mean(values, window=window)
    columns = df.columns.values.tolist()
    df_temp = df.copy()
    for x in columns:
        df_temp[x] = pd.Series(df[x]).rolling(window=window).mean()
        
    return df_temp

def compute_daily_returns(df,n=1):
    """Compute and return the daily return values."""
    df_daily_ret = (df/df.shift(n)) -1
    # Note: Returned DataFrame must have the same number of rows
    #df_daily_ret.ix[0,:] = 0
    df_daily_ret.loc[df_daily_ret.index[0:(n-1)],:]= 0
    return df_daily_ret