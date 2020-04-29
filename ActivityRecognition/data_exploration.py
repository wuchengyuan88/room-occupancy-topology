#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None) 

df = pd.read_csv('cyclinglist.csv')
print(df.describe())
print(df.shape)
#(2880, 2)

#train set
df2 = df.loc[0:1727]
print(df2.describe())

#validation set
df3 = df.loc[1728:2303]
print(df3.describe())


#test set
df4 = df.loc[2304:2880]
print(df4.describe())

dftotal = pd.read_csv('totaldata_processed.csv')
print(dftotal.describe())
