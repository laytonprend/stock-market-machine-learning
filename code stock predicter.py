# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 20:06:38 2021

@author: layto
"""

#stock market price predicter
import numpy as np
#import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
f=open('dataset.txt','r')
a=f.readline()
arr=[['day']]
a=a.split(',')
#arr=[]

for i in range(1,len(a)):
    arr.append([a[i]])
print(a)
#print(arr)   
g=0
for line in f:
    g=g+1
    line=line.split(',')
    #print(line)
    if g%1==0:
        arr[0].append(g)
        for i in range(1,len(line)-1):
        #print(i,line[i])
            arr[i].append(float(line[i]))
#print(arr[0])
#plt.plot(arr[0][0:],arr[1][0:])#data on the means across the measures
#plt.show()       
#print(arr[:3][:5])
#for i in range(0,len(arr)):
plt.plot(arr[0][1:],arr[1][1:])#data on the means across the measures
plt.show()
#linear regression
a=arr[0][1:]
b=arr[1][1:]
x = np.array(a)
#generate data
print(x)
y = np.array(b)
plt.plot(x, y, 'o')
#create scatter plot


m, b = np.polyfit(x, y, 1)
#m = slope, b=intercept
plt.plot(x, m*x + b)
plt.show()
#https://www.askpython.com/python/examples/python-predict-function#:~:text=Python%20predict()%20function%20enables,basis%20of%20the%20trained%20model.&text=The%20predict()%20function%20accepts,the%20data%20to%20be%20tested.
#algorithm, trials how good prediction is based on x days of training data before, repeats finds optimum