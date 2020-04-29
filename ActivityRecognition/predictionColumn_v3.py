#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
pd.set_option('display.max_columns', None)  
import numpy as np
from sklearn.preprocessing import StandardScaler
import math


d = 6
w = 5
stride = 5
#prefix = 'datafull'



df = pd.read_csv('totaldata_processed.csv',index_col=0)

print(df.shape)
# (14400, 7)
totalrows = df.shape[0]

print(df.head())

print(df.describe())

totalpointclouds = math.floor((totalrows-w+1)/stride)+1
print(totalpointclouds)
# 2880 (0 to 2879)

cyclinglist=[]

for i in range(0,totalpointclouds):
    cycling=0
    cyclingsum=0
    for j in range(0,w):
        currindex = i*stride+j
        #slide by stride no. of frames
        if df['activity'].iat[currindex]==1:
            cyclingsum+=1
    if cyclingsum>0:
        cycling=1
    cyclinglist.append(cycling)
    
dictionary={'activity':cyclinglist}
newdf = pd.DataFrame(dictionary)

print(newdf.head())

print(newdf.describe())

newdf.to_csv('cyclinglist.csv')
    
