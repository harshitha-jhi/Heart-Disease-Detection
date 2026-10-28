import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
import csv

import numpy as np

dataset=np.loadtxt('Feature.csv', delimiter=',', dtype='float32', usecols=list(range(0, (63) + 1)))

dataset=np.array(dataset)

from sklearn import tree

import joblib
final_data=[]
final_label=[]
xc=0
xc1=1
acc=[]
f1=[]
prec=[]
reca=[]
for i in range(32):
        print(xc)
        data=dataset[:,xc]
        final_data=data
        print(np.max(data))
        
        label=dataset[:,xc+1]
        final_label=label
        print(np.max(label))


        vb=np.array(final_label)
        
        labels1=vb.astype(np.uint8)

        y_train=labels1.reshape(-1, 1)
        X_train=final_data.reshape(-1, 1)   

        X_test=X_train
        y_test=labels1
        knncl = KNeighborsClassifier(n_neighbors=2)
        knncl.fit(X_train, y_train)
        preds = knncl.predict(X_test)


        acc.append(accuracy_score(y_test, preds))


        from sklearn.metrics import f1_score


        f1.append(f1_score(y_test, preds, average='weighted'))
        from sklearn.metrics import classification_report



        from sklearn.metrics import recall_score
        reca.append(recall_score(y_test, preds, average='weighted'))

        from sklearn.metrics import average_precision_score
        prec.append(average_precision_score(y_test>70, preds>70))
                      
        joblib.dump(knncl, "models/"+str(xc1)+"pipe_KNN.joblib")
        xc=xc+2
        xc1=xc1+1


acc=np.array(acc)
prec=np.array(prec)
f1=np.array(f1)
reca=np.array(reca)
nan_indices = np.isnan(acc)
xc=len([i for i, x in enumerate(nan_indices) if x])
if xc>0:
        acc[nan_indices]=.5

nan_indices = np.isnan(f1)
xc=len([i for i, x in enumerate(nan_indices) if x])
if xc>0:
        f1[nan_indices]=.5

nan_indices = np.isnan(reca)
xc=len([i for i, x in enumerate(nan_indices) if x])
if xc>0:
        reca[nan_indices]=.5
        
nan_indices = np.isnan(prec)
xc=len([i for i, x in enumerate(nan_indices) if x])
if xc>0:
        prec[nan_indices]=.5


print("KNN Best score on test set (accuracy) = {:.4f}".format(np.mean(acc)))
print("KNN F1 score  = {:.4f}".format(np.mean(f1)))
print("KNN Recall score  = {:.4f}".format(np.mean(reca)))
print("KNN Precision score  = {:.4f}".format(np.mean(prec)))
