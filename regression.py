#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 00:23:49 2019

@author: roopal
"""
import numpy as np
import matplotlib.pyplot as plt
#linear regression
x = np.array([0,1,2,3,5])
y = np.array([2,7,5,4,4])
#evaluate the intercept
def evaluate(x,y):
    n = np.size(x)
    m_x,m_y = np.mean(x),np.mean(y)
    ss_xy = np.sum(x*y) - n*m_x*m_y
    ss_xx = np.sum(x*x) - n*m_x*m_x
    global b1
    global b2
    b1 = ss_xy/ss_xx
    b2 = m_y - b1*m_x
    return (b1,b2)
evaluate(x,y)
def equ(x,y):
    global y1
    y1 = b1 + (b2*x)
    return y1
def main():
    print(evaluate(x,y))
    print(equ(x,y))
main()

def draw(x,y1):
    plt.scatter(x,y1,color = 'm')
    plt.plot(x,y1,color = 'g')
    plt.show()


#%%
echo "# python-mini-project" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/singhalroopal/python-mini-project.git
git push -u origin master
