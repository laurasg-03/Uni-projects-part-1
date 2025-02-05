# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:46:59 2022

@author: Laura
"""

###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 1
# Fichero: <ficheros.py>
# Autor: <Lidia Peña, Laura Sánchez>
# Fecha: <5/10/2022>
#
# <Entrega de la segunda parte de la práctica 1. Ejercicios de funciones.>
# <En todas las funciones se buscan los elementos de la lista que cumplen 
# ciertas condiciones. En los casos de no ser así, devuelve una lista vacía 
# (o booleano, en los casos en los que se exige).>
# <Los ejercicios no pueden economizarse (utilizando, por ejemplo, la búsqueda 
# binaria, debido a que debe recorrer una lista ordenada, y si se ha entragado 
# una lista con caracteres alfanuméricos, no sería posible ordenarla > 
#
###############################################################

def filter_loop(lst, f):
    l=[]
    for i in lst:
        if f(i) == True:
            l.append(i)
    return l


def filter_comprh(lst, f):
    return [i for i in lst if f(i) == True]


def search_loop(lst, f):
    for i in lst:
        if f(i) in lst:
            return True
    return False


def search_comprh(lst,f):
    if lst:
        lst_comprh= [x for x in lst if f(x)]
        return lst_comprh != []
