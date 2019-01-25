#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 00:03:07 2018

@author: roopal
"""

import pandas as pd
import nltk
import math
import operator
df = pd.read_csv('tenis.csv')
print(df)
def entropy(df,lable):
    n = []
    l = []
    a = (nltk.FreqDist(df[lable]).values())
    for i in a:
        n.append(i)
    #print(n)
    
#E(s) = -p1log2p1-plog2p
    total = len(df[lable])
    for i in range(len(n)):
        p = (n[i]/total)
        E = (-p)*(math.log2(p))
        l.append(E)
    su = sum(l) 
 ##entropy       
    return su
  
def Gain(df,subclass,lable):
    
# firstly find the entopy of zoner in particular columns
    nltk.FreqDist(df[subclass])
    # n is list of total of each zoner
    n = []
    # l is the list of unique zoner
    l = []
    #z is the list for each zoner entropy
    z = []
    a = (nltk.FreqDist(df[subclass]).values())
    for i in a:
        n.append(i)
  
    #print(n)
    #print(l)
    #y is the list of total of each zonar
    y = []
    #r is the list of data of zoners of particular colmn
    r = []
   
    b = (nltk.FreqDist(df[subclass]).keys())
    for i in b:
        l.append(i)
        s = df.loc[df[subclass] == i ]
       # print(s)
        r.append(s)
   
        y.append(s[subclass].count())
       # y.append((nltk.FreqDist(s.play)).values())
   # print(r)   
   # print(y)
    gain = []
    total = sum(y)
    for i in range(len(l)):
        j = entropy(r[i],lable)
        
        gain.append(j)
   # print (gain[0])
    for i in range(len(l)):
       p = (n[i]/(total))*gain[i]
       z.append(p)
    Y = sum(z)
 # GA is the total gain of particular colmn         
    GA = entropy(df,'play') - Y
    return GA


j = []     
def data(df,subclass):
  
    b = (nltk.FreqDist(df[subclass]).keys())
    for i in  b:
        s = df.loc[df[subclass] == i ]
        j.append(s)
   
    return j

def tree():
    
    h = []    
    for i in range(1,(len(df.columns)-1)):
        h.append (df.columns[i])     
    root = []
    print('h:',h)
    for i in range(1,(len(df.columns)-1)):
        root.append(Gain(df,df.columns[i],'play'))
    print(root)
    print(max(root))    
    AD = {}
#AD is a dict of gains for each zonar
    for i in range(len(h)):
        AD[h[i]] = root[i]
    print(AD)
#sort_AD = sorted(AD.items(),key=operator.itemgetter(1))
#print(sort_AD)
#root_node = print(sort_AD[-1])

    sort = sorted(AD.items(),key = lambda AD:AD[1])
    print(sort)

    sort_AD = (dict(sort))
    print(sort_AD)
    print(sort_AD.keys())
    foo = []
    for key in sort_AD.keys():
        foo.append(key)
    print(foo)
    root_node = foo[-1]
    print(root_node)
    print(data(df,root_node)) 
    l = []
    b = (nltk.FreqDist(df[root_node]).keys())
    for i in b:
        l.append(i)
    print(l)
    lis=[]
    for i in range(len(l)):
        #roop[k]=[]
        for k in h:
            gain=(Gain(j[i],k,'play'))
            lis.append(gain)
    
    print(max(lis))
    dit = {}
    for i in l:
        dit[i] = []
        for b in range(len(h)):
            dit[i].append(lis[b])
        print(dit)

