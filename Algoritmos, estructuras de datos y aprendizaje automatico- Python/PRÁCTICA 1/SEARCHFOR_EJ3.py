# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:13:52 2022

@author: Laura
"""

import time
import math
import random
import matplotlib.pyplot as plt

def search_comprh(lst,val):
    if lst:
        lst_comprh= [x for x in lst if val==x]
        return lst_comprh != []

    
def basic_time(array, val):
    Nrep = 100
    t1 = time.process_time()
    for k in range(Nrep):
    #val= lambda x: x==val
        search_comprh(array, val)
    t2 = time.process_time()
    return (t2-t1)/float(Nrep)


def generate_random_input(n):
    Mx = 1000.0
    array = [random.uniform(-Mx, Mx) for _ in range(n)]
    val = max(array)+1
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

N = range(100, 10100 , 100)
x=[]
y=[]
z=[]
for n in N:
    (m, v) = stat_measure(n) 
    x+=[n]
    y+=[m]
    z+=[v]
    print ("%5d, %12.5f, %12.5f" % (n, m, v))

plt.title("search_comprh")
plt.plot(x,y,x,z)
plt.xlabel("Longitud de la lista")
plt.ylabel("Tiempo que tarda en ejecutarse el programa")
plt.plot(x,y, label="Tiempo medio")
plt.plot(x,z, label="Varianza")
plt.xlabel("Longitud de la lista")
plt.legend()
plt.show()