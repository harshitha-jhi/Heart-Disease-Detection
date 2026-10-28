# potentiometer.py

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

from sklearn.tree import DecisionTreeClassifier
import time

os.getcwd()

import requests


import csv

import numpy as np

import time

import joblib





dataset=np.loadtxt('test.csv', delimiter=',', dtype='float32', usecols=list(range(0, (1))))

dataset=np.array(dataset)

final_data=dataset


csv_path = 'Results.csv'


final=np.zeros((len(final_data),3))
fd=np.array(final_data)
#fd=fd.reshape(-1, 1)

final[:,0]=fd


        


final_data=final_data.reshape(-1, 1)
res=[]

for i in range(len(final_data)):
    clfKNN=joblib.load("models/"+str(i+1)+"pipe_KNN.joblib")

    preds = clfKNN.predict(final_data[i].reshape(-1, 1))
    res.append(preds[0])


final[:,1]=res



for i in range(len(final)):
    with open(csv_path, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(final[i,:])


        
