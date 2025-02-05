# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:43:12 2022

@author: Laura
"""
# Ejercicio 2: Altura
# Crear una gr´afica donde se represente la altura media del ´arbol y la varianza como funci´on de n
# para los valores de n
# Nvals = [int(2**(x/10.0+4)) for x in range(110)]


import time
import math
import random
import matplotlib.pyplot as plt
import Tree as tr

tr=tr.Tree()

def mycomp(x, y):
    return x - y

    
def generate_random_input(n):
    Mx = 1000.0
    array = [random.uniform(-Mx, Mx) for _ in range(n)]
    val = max(array)+1
    return (array, val) #devuelve la lista y el valor que ha encontraddo, dada la k random

def stat_measure(n):
    Nvals = [int(2**(x/10.0+4)) for x in range(110)]
    
    t = Nvals*[0.0]
    for k in range(Nvals):
        (array, val) = generate_random_input(n)
        for i in array:
            tr.insert(i)
        t[i] = tr.measure_height(array, val)
        
    m = sum(t)/float(Nvals) # Calculate average
    v = math.sqrt(sum([(x-m)**2 for x in t])/float(Nvals)) # Calculate std dev
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

plt.title("measure_height")
plt.plot(x,y,x,z)
plt.xlabel("Longitud de la lista")
plt.ylabel("Longitud")
plt.plot(x,y, label="Longitud media")
plt.plot(x,z, label="Varianza")
plt.xlabel("Longitud de la lista")
plt.legend()
plt.show()