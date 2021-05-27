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
plt.plot(arr[0][1004:1104],arr[1][1002:1102])#data on the means across the measures
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


m, q = np.polyfit(x, y, 1)
#m = slope, b=intercept
plt.plot(x, m*x + q)
plt.show()
#
#algorithm, trials how good prediction is based on x days of training data before, repeats finds optimum
#reformat data to % return a day

percent=[]
#print(b)
for i in range(2,len(arr[1][0:])):
    percent.append(100*arr[1][i]/arr[1][i-1]-100)
#plt.plot(arr[0][2:],percent)#data on the means across the measures# 2 values lost
#plt.show()
x=np.array(arr[0][2:])
y=percent
plt.plot(x,y,'o')
m, q = np.polyfit(x, y, 1)
#m = slope, b=intercept
plt.plot(x, m*x + q)
plt.show()
print((m/100+1)**250,(q/100+1)**250)

plt.plot(arr[0][1004:1104],percent[1002:1102])#data on the means across the measures# 2 values lost
plt.show()

#datasets modelling is % change a day and time then predict next value
#proof of concept build for first 500 then test next 50 and see accuracy by plotting graph of multiplying by predicted % and showing next to real graph
#print(percent[:5], '--',arr[0][:5])
'''for i in range(0,50):
    x=np.array(arr[0][2+i:2+i+5])
    y=percent[i:i+5]
    plt.plot(x,y,'o')
    m, q = np.polyfit(x, y, 1)
    #m = slope, b=intercept
    plt.plot(x, m*x + q)
    plt.show()
    predictedvalue=(i+1)*m+q
    print(predictedvalue,percent[i+1])
    #repeat at different sizes and lengths to find appropriate modlelength
    '''
#actual code
sd=[]
summed=[]
for f in range(0,int(len(percent)/2)):#doing half as whole data is not accurate
    a=[f]
    b=[f]
    diff=[]
    for i in range(0,len(percent)-f):
        bb=[]
        #first value is length of data inputted
        x=np.array(arr[0][2+i:2+i+2+f])
        y=percent[i:i+f]
        plt.plot(x,y,'o')
        m, q = np.polyfit(x, y, 1)
        #m = slope, b=intercept
        plt.plot(x, m*x + q)
        plt.show()
        predictedvalue=(i+1)*m+q
        print(predictedvalue,percent[i+1])
        dif=(predictedvalue-percent[i-1])/100+1
        diff.append(dif)
        bb.append((predictedvalue-percent))
        
    diff=np.array(diff)
    a.append(np.std(diff))#lowest sd best# std not good s different sies of data
    b.append(sum(bb)/len(bb))#how much each value is away in%
    sd.append(a)
    summed.append(b)
    
        
        


