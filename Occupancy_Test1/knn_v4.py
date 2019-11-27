#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import math
from sklearn.metrics import classification_report

# Value of k
k = 50
prefix = 'datafull'

distmatrix = pd.read_csv('WassersteinDistMatrix.csv')
distmatrix = distmatrix.drop(distmatrix.columns[[0]], axis=1) 
#print(distmatrix.head())
#print(distmatrix.describe())
print(distmatrix.shape)
#(1000, 1000)
totaln = distmatrix.shape[0]

adjmat = distmatrix.values #convert to numpy array

#print(adjmat)

##make adjmat symmetric

for j in range(0,totaln):

    for i in range(0,j):

        adjmat[i][j] = adjmat[j][i]

##now adjmat is symmetric matrix

#print(adjmat)



# Train: 80%
trainnum = 800
#math.floor(0.8*totaln)
print(trainnum)
# 800
trainlist = [i for i in range(0,trainnum)]

# Test: 20%
testnum = totaln-trainnum
print(testnum)
# 200
testlist = [i for i in range(trainnum,totaln)]

df = pd.read_csv(prefix+'occupied.csv')
y_true = df['Occupied'].iloc[testlist]
y_true = y_true.values.tolist()


### k-nn algorithm
knn = [[] for i in range(testnum)]

for i in range(0,testnum):
    index = testlist[i]
    # We only use training data for k-nn prediction
    coltobesort = adjmat[0:trainnum,index]
    indexsorted = np.argsort(coltobesort)

    indexsorted = indexsorted[indexsorted != index] #remove testlist[i] as its own nearest neighbor

    #print(len(indexsorted))

    #len(indexsorted)=684



    knn[i] = indexsorted[0:k]

print(len(knn))
# len(knn)=171

#print(knn[170])

    
###


### y_pred
y_pred=[]
for i in range(0,len(knn)):
    knnclass = df['Occupied'].iloc[knn[i]]
    #print(knnclass)
    # sum over the column axis.
    totalsum = knnclass.sum()
    average = totalsum/k
    if (average<0.5):
        y_pred.append(0)
    else:
        y_pred.append(1)

###
print('y_pred:')
print(y_pred)
# print(len(y_pred))
# 171
print('y_true:')
print(y_true)

target_names =['class 0', 'class 1']
print(classification_report(y_true, y_pred, labels=[0,1],
                            target_names=target_names))
