#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option('display.max_columns', None)  
#import numpy as np
from sklearn.preprocessing import StandardScaler
#from datetime import datetime
#date_format = "%d/%m/%Y"

d = 5
prefix ='datafull'

df = pd.read_csv(prefix+'.csv',index_col=False)

#drop first column
df = df.drop(df.columns[0], axis=1)

print(df.shape)
#(10000, 7)

print(df.head())

print(df.describe())

numerical_cols = list(df.columns.values)
numerical_cols.remove('Occupancy')
numerical_cols.remove('date')
print(numerical_cols)

df[numerical_cols] = StandardScaler().fit_transform(df[numerical_cols])

df = df.drop(labels='date', axis=1) # axis 1 drops columns

# Make Coordinate dependent
df['Humidity']+=1
df['Light']+=2
df['CO2']+=3
df['HumidityRatio']+=4

print(df.head())

print(df.describe())

df.to_csv(prefix+'clean.csv')