#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 23:16:25 2018

@author: roopal
"""
arr = [2,3,43,2,3,2]
def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i -1
    while arr[j] > 0 and key > arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[j])        