# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"


#%%
import pandas as pd
data = pd.read_csv('bike_sharing.csv')
print(data)
import numpy as np
data1 = data.iloc[0:10]

#print(data1)
dataframe = pd.DataFrame(data1)
dataframe
m1 = dataframe.mean(axis = 0,numeric_only = True)
#print(m1)
v1 = dataframe.std(axis = 0,numeric_only = True)
#print(v1)
m1_dataframe = pd.DataFrame(m1)
m1_dataframe
v1_dataframe = pd.DataFrame(v1)
v1_dataframe
df = dataframe.drop(['datetime','holiday','workingday','weather','season'],axis = 1)
#print(df)
df.transpose()

#%%
for i in range(len(data1)):
     for j in range(10):
         data2 = (data1[i][j]  - m1_dataframe[i][j])/v1_dataframe[i][j]
         print(data1)
#%%
for i in range(len(df)):
    for j in range(10):
        df1[i][j] =    (df.iloc[i,j]-m1_dataframe.iloc[0,j]) /v1_dataframe.iloc[0,j] 
        print(df[i][j])
#%%
df.apply(lambda x :(df - m1_dataframe)/v1_dataframe )   

#%%
df.iloc[1:9] - m1_dataframe.iloc[1]





#%%
import pandas as pd
data = pd.read_csv('bike_sharing.csv')
print(data)
import numpy as np
data1 = data.iloc[0:10]

print(data1)
dataframe = pd.DataFrame(data1)
dataframe
#m1 = dataframe.mean(axis = 0,numeric_only = True)
#print(m1)
#v1 = dataframe.std(axis = 0,numeric_only = True)
#print(v1)
#m1_dataframe = pd.DataFrame(m1)
#m1_dataframe
#v1_dataframe = pd.DataFrame(v1)
#v1_dataframe
df = dataframe.drop(['datetime','holiday','workingday','weather','season'],axis = 1)
df = df.T
print(df)
m1 = df.mean(axis = 0,numeric_only = True)
print(m1)
v1 = df.std(axis = 0,numeric_only = True)
print(v1)


for i in range(10):
    for j in range(7):
        df[i][j] = (df[i][j] - m1[j])/v1[j]
        
print(df)

print(df.cov())
#%%        
np.linalg.eigvals(df.apply(pd.to_numeric,errors = 'coerce').fillna(0))
#%%
from numpy. linalg import solve
print("Eiganvalues:",np.linalg.eigvals(df))

#%%

eigval=np.linalg.eigvals(df.cov().fillna(0))
#print(eigval)
eigval,eigv=np.linalg.eig(df.cov())

print(eigv)
idx=eigval.argsort()[::-1]
eigval=eigval[idx]
eigv=eigv[:,idx]
print(eigv)

 #%%

#pca_main_axis = np.mat(eigv[:,0]  )     
#print(pca_main_axis)
##x = eigv
##print(eigv)
#trans = pca_main_axis.T
#print(trans)
df1 = np.mat(df)
print(df1)
p = []
for i in range(10):
    pca_main_axis = np.mat(eigv[:,0:i])     
    print(pca_main_axis)
    trans = pca_main_axis.T
    k = np.matmul(pca_main_axis,trans)
    r = np.square(df1 - np.float(k[0,0])*df1)
    p.append(np.sum(r))
print(p,"error in pca")

import matplotlib.pyplot as plt   
plt.plot(p)
plt.show()    