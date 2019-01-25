#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:29:40 2018

@author: roopal
"""
import numpy as np
matrix = []
n = int(input('enter size of row:'))
m = int(input('enter no of columns:'))
  
for j in range(0,n):
    arr = []
    for i in range(0,m):
        arr.append(int(input("enter element in arr:")))
    matrix.append(arr)    
print(matrix)
mat = np.array(matrix)
print(mat)  
m,n = mat.shape
print(m)
matrix2 = []
n = int(input('enter size of row:'))
m = int(input('enter no of columns:'))
  
for j in range(0,n):
    arr = []
    for i in range(0,m):
        arr.append(int(input("enter element in arr:")))
    matrix2.append(arr)    
print(matrix)
mat2 = np.array(matrix)
print(mat)  
m2,n2= mat2.shape
print(m)

#%%
def matrix():
    print("enter the even dimension of matrix below:")
    m = int(input("enter the no of the row in mult of 2:"))
    n = int (input("enter the no of the col mul of 2:"))
    matrix1 = np.zeros((m,n))
#%%
def convert(a):
    a = np.matrix([[1,2,3],[2,3,4]])
    m = int(input("enter the no of the row in mult of 2:"))
    n = int (input("enter the no of the col mul of 2:"))
    matrix = np.zeros((m,n))
    m1, n1 = a.shape
    for i in range(m1):
        for j in range(n1):
            matrix[i][j] = a[i][j]
            print(matrix)
    return matrix
    
#%%

if mat.shape <= (2,2):
    for i in range(len(matrix)):
        
        