# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 23:49:10 2022

@author: Laura
"""
###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 1
# Fichero: <listas.py>
# Autor: <Lidia Peña, Laura Sánchez>
# Fecha: <5/10/2022>
#
# <Entrega de la primera parte de la práctica 1. Ejercicios de listas.>
# <En todas las funciones se buscan los elementos de la lista que cumplen 
# ciertas condiciones. En los casos de no ser así, devuelve una lista vacía.> 
#
###############################################################

def myzip_loop (lst1,lst2):
    lista_nueva=[]
    n=min(len(lst1),len(lst2))
    for i in range(n):
        lista_nueva += [(lst1[i],lst2[i])]
    return lista_nueva


def mult3_loop(lst):
    l=[]
    for i in lst:     
        if (i%3) == 0:
            l.append(i)
    return l


def mult3_comprh(lst):
    return [i for i in lst if i%3 == 0]