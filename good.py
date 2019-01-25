#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:02:31 2018

@author: roopal
"""

import pandas as pd
import numpy as np
import sklearn
data = pd.read_csv('/home/roopal/income.dat',sep = ' ')
column = [' ANNUAL INCOME ','SEX','MARITAL STATUS','AGE','EDUCATION',' OCCUPATION','LIVED','DUAL INCOMES','HOUSEHOLD','HOUSEHOLD UNDER 18','HOUSEHOLDER STATUS','TYPE OF HOME','CLASSIFICATION','MOST LANGUAGE']
data.columns = column
print(data.head())
from sklearn.model_selection import train_test_split
#%%

##for na values
for j in list(np.mean(data)):
    for i in data:
        data[i] = data[i].fillna((j))
        
        
 #%% df.fillna(df.mode().iloc[0])   
#%%
y = data[' ANNUAL INCOME ']
df = data[['SEX','MARITAL STATUS','AGE','EDUCATION',' OCCUPATION','LIVED','DUAL INCOMES','HOUSEHOLD','HOUSEHOLD UNDER 18','HOUSEHOLDER STATUS','TYPE OF HOME','CLASSIFICATION','MOST LANGUAGE']]

#%%
train_x,test_x,train_y,test_y =  train_test_split(df,y,test_size = 0.2)
#%%
from sklearn import metrics
from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion='gini',random_state=0)
clf.fit(train_x,train_y)
pred = clf.predict(test_x)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(pred,test_y))
from sklearn.metrics import classification_report 
print(classification_report(pred,test_y))
metrics.accuracy_score(pred,test_y)
#%%
from sklearn.ensemble import AdaBoostClassifier
clf1 = AdaBoostClassifier()
clf1.fit(train_x,train_y)
pred1 = clf.predict(test_x)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(pred1,test_y))
from sklearn.metrics import classification_report 
print(classification_report(pred1,test_y))
metrics.accuracy_score(pred1,test_y)
#%%
from sklearn.linear_model import LinearRegression
clf2 = LinearRegression()
clf2.fit(train_x,train_y)
pred2 = clf2.predict(test_x)
a = pd.DataFrame({'actual':test_y,'pred':pred2})

mse=metrics.mean_squared_error(pred2,test_y)
np.sqrt(mse)
#%%
from sklearn.ensemble import RandomForestRegressor
clf4 = RandomForestRegressor()
clf4.fit(train_x,train_y)
pred3 = clf4.predict(test_x)
a = pd.DataFrame({'actual':test_y,'pred':pred3})

mse=metrics.mean_squared_error(pred3,test_y)
np.sqrt(mse)
#%%
from sklearn.ensemble import GradientBoostingRegressor
clf5 = RandomForestRegressor()
clf5.fit(train_x,train_y)
pred5 = clf5.predict(test_x)
a = pd.DataFrame({'actual':test_y,'pred':pred5})

mse=metrics.mean_squared_error(pred5,test_y)
np.sqrt(mse)
#%%%
pred6 = (pred2+pred3+pred5)/3
mse=metrics.mean_squared_error(pred6,test_y)
np.sqrt(mse)
#%%%
from sklearn.feature_selection import SelectFromModel
sfm = SelectFromModel(clf,threshold = 0.1,prefit=False)
sfm.fit(train_x,train_y)
lis = []
ls = []
for feature_list_index in sfm.get_support(indices=False):
    lis.append(feature_list_index)
for i in range(0,13):
    if lis[i] == True:
        ls.append(data.columns[i])
df1 = data[ls]
    #%%
train_x1,test_x1,train_y1,test_y1 =  train_test_split(df1,y,test_size = 0.2)
clf = tree.DecisionTreeClassifier(random_state=0)
clf.fit(train_x1,train_y1)
pred7 = clf.predict(test_x1)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(pred7,test_y1))
from sklearn.metrics import classification_report 
print(classification_report(pred7,test_y))
metrics.accuracy_score(pred7,test_y1)