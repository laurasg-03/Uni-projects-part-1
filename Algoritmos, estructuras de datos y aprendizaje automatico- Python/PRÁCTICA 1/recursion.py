# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 00:26:57 2022

@author: Laura
"""

###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 1
# Fichero: <recursion.py>
# Autor: <Lidia Peña, Laura Sánchez>
# Fecha: <5/10/2022>
#
# <Entrega de la tercera parte de la práctica 1. Ejercicios de recursión.>
# <En todas las funciones se buscan los elementos de la lista que cumplen 
# ciertas condiciones. En los casos de no ser así, devuelve una lista vacía 
# (o booleano, en los casos en los que se exige).>
#
###############################################################

def reverse_rec(lst):
    if lst==[]:
        return []
    else:
        return [lst[-1]] + reverse_rec(lst[:-1])
       
        
def search_rec(lst, f):
    if lst==[]:
        return False
    elif f(lst[0])==True:
        return True
    else:
        return search_rec(lst[1:],f)


def filter_rec(lst, f):
    if lst==[]:
        return []
    elif f(lst[0])==True:
        return [lst[0]]+filter_rec(lst[1:],f)
    else:
        return filter_rec(lst[1:],f) 
    



