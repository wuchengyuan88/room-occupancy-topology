#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
pd.set_option('display.max_columns', None)  
import numpy as np
from sklearn.preprocessing import StandardScaler
import math


d = 5
w = 10
stride = 10
prefix = 'datafull'



df = pd.read_csv(prefix+'clean.csv')

print(df.shape)
# (10000, 7)
totalrows = df.shape[0]

print(df.head())

print(df.describe())

totalpointclouds = math.floor((totalrows-w+1)/stride)+1
print(totalpointclouds)
# 1000 (0 to 999)

occupiedlist=[]

for i in range(0,totalpointclouds):
    occupied=0
    occupiedsum=0
    for j in range(0,w):
        currindex = i*stride+j
        #slide by stride no. of frames
        if df['Occupancy'].iat[currindex]==1:
            occupiedsum+=1
    if occupiedsum>0:
        occupied=1
    occupiedlist.append(occupied)
    
dictionary={'Occupied':occupiedlist}
newdf = pd.DataFrame(dictionary)

print(newdf.head())

print(newdf.describe())

newdf.to_csv(prefix+'occupied.csv')
    
