# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 16:16:40 2022

@author: Laura
"""

import time
import math
import random
import matplotlib.pyplot as plt

def search_comprh(lst, f):
    return [True if f(i) else False for i in lst]

def linsearch(array, val):
    for k in range(len(array)):
        if array[k] == val:
            return k
    return None
    
def basic_time(array, val):
    Nrep = 100
    t1 = time.process_time()
    val= lambda x: x==val
    search_comprh(array, val)
    t2 = time.process_time()
    return (t2-t1)/float(Nrep)


def generate_random_input(n):
    
    array = [random.uniform(0, 1) for _ in range(n)]
    k=random.randint(0,n-1) #-1 pq sino sale list index out of range
    val = array[k]
    return (array, val) #devuelve la lista y el valor que ha encontraddo, dada la k random

def stat_measure(n):
    Nstat = 10 # Number of repetitions for statistics
    t = Nstat*[0.0]
    for k in range(Nstat):
        (array, val) = generate_random_input(n)
        t[k] = basic_time(array, val)
    m = sum(t)/float(Nstat) # Calculate average
    v = math.sqrt(sum([(x-m)**2 for x in t])/float(Nstat)) # Calculate std dev
    return (m, v)

N = range(100,  10100 , 100)
x=[]
y=[]
z=[]
for n in N:
    (m, v) = stat_measure(n) 
    x+=[n]
    y+=[m]
    z+=[v]
    print ("%5d, %12.5f, %12.5f" % (n, m, v))

plt.title("Hola")
plt.subplot(2,1,1)
plt.plot(x,y)
plt.xlabel("List size")
plt.ylabel("Average (s)")
