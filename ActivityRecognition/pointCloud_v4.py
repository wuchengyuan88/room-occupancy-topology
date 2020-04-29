#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Set working directory ###
###

import pandas as pd
pd.set_option('display.max_columns', None)  
import numpy as np
import math
#from sklearn.preprocessing import StandardScaler


d = 6
w = 5
stride = 5


df = pd.read_csv('totaldata_processed.csv',index_col=0)
df = df.drop(labels='activity', axis=1) # axis 1 drops columns
print(df.shape)
# (14400, 6)
totalrows = df.shape[0]

print(df.head())

print(df.describe())

totalpointclouds = math.floor((totalrows-w+1)/stride) +1
print(totalpointclouds)
# 2880

for i in range(0,totalpointclouds):
    #create txtfiles folder manually
    filename = './txtfiles/'+'pc'+str(i)+'.txt'
    array = np.zeros((w+1,d))
        
    for j in range(0,w):
        currindex = i*stride+j
        #slide by stride no. of frames
        array[j][0]=df.iat[currindex,0]
        array[j][1]=df.iat[currindex,1]
        array[j][2]=df.iat[currindex,2]
        array[j][3]=df.iat[currindex,3]
        array[j][4]=df.iat[currindex,4]
        array[j][5]=df.iat[currindex,5]
        
    #anchor point
    array[w][0]=0
    array[w][1]=0
    array[w][2]=0
    array[w][3]=0
    array[w][4]=0
    array[w][5]=0
    
    np.savetxt(filename, array, fmt='%f')
        

