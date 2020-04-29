#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

import random
random.seed(1)
#print(random.random())

df1 = pd.read_csv('cycling_total.csv')
print(df1.shape)
#(7200, 7)
print(df1.head())
df1length = df1.shape[0]

df0 = pd.read_csv('standing_total.csv')
print(df0.shape)
print(df0.head())
df0length = df0.shape[0]

cyclingindex=0
class0index=0

dftotal = pd.DataFrame(columns = df1.columns)
#print(dftotal.head())

while (cyclingindex+5<=df1length) and (class0index+5<=df0length):
    rnd = random.random()
    #print(rnd)
    if (rnd<0.5):
        rowrange = [i for i in range(cyclingindex,cyclingindex+5)]
        dftotal = dftotal.append(df1.iloc[rowrange]) 
        cyclingindex=cyclingindex+5
    else:
        rowrange = [i for i in range(class0index,class0index+5)]
        dftotal = dftotal.append(df0.iloc[rowrange]) 
        class0index=class0index+5

print(cyclingindex)
#6905
print(class0index)
#7200

if cyclingindex+5==df1length:
    remaining = [i for i in range(class0index,df0length)]
    dftotal = dftotal.append(df0.iloc[remaining])
else:
    remaining = [i for i in range(cyclingindex,df1length)]
    dftotal = dftotal.append(df1.iloc[remaining])
    
print(dftotal.shape)   
#(14400, 7) 
print(dftotal.head())    
    
dftotal.to_csv('shuffled_total.csv')
