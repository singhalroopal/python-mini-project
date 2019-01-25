#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:28:29 2019

@author: roopal
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('/home/roopal/datareg')
x = data['size in feet square']
y = data['prize in 1000$']
Q0 = 0.1
Q1 = 0.5
n = 100
e = 0.004
alpha = 0.01
l = 0
for i in range(n+1):
      l =  l + 1
      predict = Q0 + Q1*x
      #print(predict)
      cost = (1/2*n)*(np.sum(np.square(predict - y)))
      #print(cost)
      Q0 = Q0 - alpha*(np.sum(Q1*x + Q0 - y)*(1/n))
      Q1 = Q1 - alpha*(np.sum(Q1*x + Q0 - y)*(1/n)*x)
      print(f"{Q0}")
      plt.scatter(x,predict,color = 'm')
      plt.plot(x,predict,color = 'g')
      plt.show()
  
      if cost < e:
          
          print(cost)
          print(l)
        
          break
        
      else :
          continue
    
    