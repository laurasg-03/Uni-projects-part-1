# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:43:12 2022

@author: Laura
"""
###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 3
# Fichero: tmeasure.py
# Autor: Laura Sanchez Garzon//Lidia Peña Morante
# Fecha: 23/11/2022
#
# fichero que mide la altura media y la variacion de una serie de arboles binarios 
# 
# memoria adjunta en un informe.pdf
# un fichero tdata.dat sera creado automaticamente tras la ejecucion del programa
# 
###############################################################

import math
import random
import matplotlib.pyplot as plt
import Tree as tr

def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0
    
def measure_height(n, m):
    arb = tr.Tree()
    for l in n:
        arb.insert(l, compare)
    return arb.height()

    
def generate_random_input(n):
    Mx = 1000.0
    array = [random.uniform(0, Mx) for _ in range(n)]
    k=random.randint(0,n-1)
    val = array[k]
    return (array, val) #devuelve la lista y el valor que ha encontraddo, dada la k random

def stat_measure(n):
    Nstat = 10 # Number of repetitions for statistics
    t = Nstat*[0.0]
    for k in range(Nstat):
        arbol=tr.Tree()
        (array, val) = generate_random_input(n)
        for i in array:
            arbol.insert(i, compare)
        t[k] = measure_height(array, val)
    m = sum(t)/float(Nstat) # Calculate average
    v = math.sqrt(sum([(x-m)**2 for x in t])/float(Nstat)) # Calculate std dev
    return (m, v)

Nvals = [int(2**(x/10.0+4)) for x in range(110)]
x=[]
y=[]
z=[]
fichero = open("./tdata.data","w")
fichero.write("    n       media         varianza" + "\n")

for n in Nvals:
    (m, v) = stat_measure(n) 
    x+=[n]
    y+=[m]
    z+=[v]
    line = ("%5d, %12.5f, %12.5f" % (n, m, v))
    print (line)
    fichero.write(line + "\n")

fichero.close()

plt.title("measure_height")
plt.plot(x,y,x,z)
plt.xlabel("Longitud de la lista")
plt.ylabel("Altura")
plt.plot(x,y, label="Altura media (10 repeticiones)")
plt.plot(x,z, label="Varianza")
plt.xlabel("Longitud de la lista")
plt.legend()
plt.show()
