#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option('display.max_columns', None)  
#import numpy as np
from sklearn.preprocessing import StandardScaler
#from datetime import datetime
#date_format = "%d/%m/%Y"

d = 6
#prefix ='datafull'

df = pd.read_csv('shuffled_total.csv')

#drop first column
df = df.drop(df.columns[0], axis=1)

print(df.shape)
#(14400, 7)

print(df.head())

print(df.describe())

numerical_cols = list(df.columns.values)
#numerical_cols.remove('Occupancy')
numerical_cols.remove('activity')
print(numerical_cols)

df[numerical_cols] = StandardScaler().fit_transform(df[numerical_cols])

#df = df.drop(labels='date', axis=1) # axis 1 drops columns

# Symmetry breaking
df['var_rss12']+=1
df['avg_rss13']+=2
df['var_rss13']+=3
df['avg_rss23']+=4
df['var_rss23']+=5

print(df.head())

print(df.describe())

df.to_csv('totaldata_processed.csv')