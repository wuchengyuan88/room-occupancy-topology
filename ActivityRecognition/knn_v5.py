#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import math
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Value of k
k = 40


distmatrix = pd.read_csv('WassersteinDistMatrix.csv')
distmatrix = distmatrix.drop(distmatrix.columns[[0]], axis=1) 
#print(distmatrix.head())
#print(distmatrix.describe())
print(distmatrix.shape)
#(2880, 2880)
totaln = distmatrix.shape[0]

adjmat = distmatrix.values #convert to numpy array

#print(adjmat)

##make adjmat symmetric

for j in range(0,totaln):

    for i in range(0,j):

        adjmat[i][j] = adjmat[j][i]

##now adjmat is symmetric matrix

#print(adjmat)



# Train: 60%
trainnum = 1728
#math.floor(0.8*totaln)
print(trainnum)
# 800
trainlist = [i for i in range(0,trainnum)]

# Validation: 20%
validnum = 576
validlist = [i for i in range(trainnum,trainnum+validnum)]



# Test: 20%
testnum = 576
print(testnum)
# 200
testlist = [i for i in range(trainnum+validnum,totaln)]

df = pd.read_csv('cyclinglist.csv')


### (Validation)
y_true = df['activity'].iloc[validlist]
y_true = y_true.values.tolist()


### k-nn algorithm 
knn = [[] for i in range(validnum)]

for i in range(0,validnum):
    index = validlist[i]
    # We only use training data for k-nn prediction
    coltobesort = adjmat[0:trainnum,index]
    indexsorted = np.argsort(coltobesort)

    indexsorted = indexsorted[indexsorted != index] #remove testlist[i] as its own nearest neighbor

    #print(len(indexsorted))

    #len(indexsorted)=684



    knn[i] = indexsorted[0:k]

#print(len(knn))
# len(knn)=576

#print(knn[0])

    
###


### y_pred
y_pred=[]
for i in range(0,len(knn)):
    knnclass = df['activity'].iloc[knn[i]]
    #print(knnclass)
    # sum over the column axis.
    totalsum = knnclass.sum()
    average = totalsum/k
    if (average<0.5):
        y_pred.append(0)
    else:
        y_pred.append(1)

###
print('Validation Results:')
print('y_pred:')
print(y_pred)
# print(len(y_pred))
# 171
print('y_true:')
print(y_true)

target_names =['class 0', 'class 1']
print(classification_report(y_true, y_pred, labels=[0,1],
                            target_names=target_names,digits=4))
print(confusion_matrix(y_true, y_pred))
print('--------')


### Test Set
y_true = df['activity'].iloc[testlist]
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

#print(len(knn))
# len(knn)=576

print(knn[0])
    
###


### y_pred
y_pred=[]
for i in range(0,len(knn)):
    knnclass = df['activity'].iloc[knn[i]]
    #print(knnclass)
    # sum over the column axis.
    totalsum = knnclass.sum()
    average = totalsum/k
    if (average<0.5):
        y_pred.append(0)
    else:
        y_pred.append(1)

###
print('Test Results:')
print('y_pred:')
print(y_pred)
# print(len(y_pred))
# 171
print('y_true:')
print(y_true)

target_names =['class 0', 'class 1']
print(classification_report(y_true, y_pred, labels=[0,1],
                            target_names=target_names,digits=4))
print(confusion_matrix(y_true, y_pred))