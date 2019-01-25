# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import math
import pandas as pd
import nltk
df = pd.read_csv('tenis.csv')
print(df.outlook)
print(df)
def entropy(df,clasa):
    n = []
    l = []
    a = (nltk.FreqDist(df[clasa]).values())
    for i in a:
        n.append(i)
    print(n)
    print(len(n))
#E(s) = -p1log2p1-plog2p
    total = len(df[clasa])
    for i in range(len(n)):
        p = (n[i]/total)
        E = (-p)*(math.log2(p))
        l.append(E)
    su = sum(l) 
 ##entropy       
    print(su)
    