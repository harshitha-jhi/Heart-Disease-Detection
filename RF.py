import numpy as np
from numpy import array 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix,roc_auc_score,roc_curve
from sklearn.ensemble import RandomForestClassifier

dataset=pd.read_csv('./Heart.csv')
#print(dataset.iloc[:,0])

X = dataset.iloc[:,0:13].values
print(dataset.head())
print(X)

y = dataset.iloc[:,-1].values

#print(dataset.cardio.value_counts())

#for i in range(1,200):
    
X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.20,random_state=65)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

filename = './RF_st_model.pkl'
with open(filename,'wb')as f:
    pickle.dump(sc,f)

sns.countplot(x='num',data=dataset)
dataset.num.value_counts()
plt.show()

classifier = RandomForestClassifier()
classifier.fit(X_train, Y_train)

filename = './RF_model.pkl'
with open(filename,'wb')as f:
    pickle.dump(classifier,f)

y_pred = classifier.predict(X_test)

acc = accuracy_score(Y_test,y_pred)
print(f'Accuracy: {acc}')

cm=confusion_matrix(Y_test, y_pred) 
print(cm)

fig1, ax1 = plt.subplots()
ax1 = sns.heatmap(cm/np.sum(cm), annot=True, 
            fmt='.2%', cmap='Blues')

ax1.set_title('Seaborn Confusion Matrix with labels\n\n');
ax1.set_xlabel('\nPredicted Values')
ax1.set_ylabel('Actual Values ')
plt.savefig("RF_Confusion_matrix.png")
plt.show()
print(classification_report(Y_test, y_pred))

