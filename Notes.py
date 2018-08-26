#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 20:43:26 2018

@author: Prabz
"""

    if int(input_list.count()) < 5:
        return np.NaN
    
    
    
    temp_1 = (input_list.apply(lambda x: x.sort_values(ascending=False)).iloc[2:3,:].values)[0,0]
    return  temp_1

temp_1 = (input_list.apply(lambda x: x.sort_values(ascending=False)).iloc[2:3,:].values)[0,0]
   