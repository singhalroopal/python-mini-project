#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 09:09:39 2018

@author: roopal
"""
import itertools
import collections
import nltk
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
treshhold_value = 50
no_of_transction = len(df)
min_support = (treshhold_value/100)*no_of_transction
print(min_support)

col = df.columns
print(col)
b = {}
for i in col:
     count = (collections.Counter(df[i]))
     
     b.update(count)
     
print(b)

def support(list_sub):
    dele = []
   
    for i in b.keys():
        if b[i] < min_support:
            dele.append(i)
    print(dele)       
    for i in dele:
        del b[i]
    return(b)




lit = []
def combination():
   
    for i in range(0,len(b.keys())+1):
        lit.append(list(itertools.combinations(b.keys(),i)))
    return lit[2]

def combination1():
   
    for i in range(0,len(b.keys())+1):
        lit.append(list(itertools.combinations(b.keys(),i)))
    return lit[3]


    



                








