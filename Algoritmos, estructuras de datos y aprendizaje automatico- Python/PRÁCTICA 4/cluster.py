# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 17:35:54 2022

@author: Laura
"""
###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 4
# Fichero: <cluster.py>
# Autor: <Lidia Penna Morante y Laura Sanchez Garzon>
# Fecha: <16/12/2022>
#
# <Algoritmo de clustering que permite agrupar una serie de genes en familias 
# segun tengan funciones parecidas>
#
###############################################################

import math as m
import Tree as Tree
import numpy as np 
import itertools as it
import math

#ejercicio 1 practica 4
#
# Merge two cluster trees. The roots become the children of the new
# root, and the set of points of the new root is the union of the sets
# of points of the two.
#
# Returns the new tree
#

class Gen:
    def __init__(self, data):
        self.data = data 
    def __str__(self):
        return(self.data)    
        
        
        
def tmerge(t1, t2):
    data1 = t1.root.data
    data2 = t2.root.data
    if type(data1[0])== list and type(data2[0])== list:
        pts = data1+data2
    elif type(data1[0]) == list:
        pts = data1+[data2]
    elif type(data2[0]) == list:
        pts = [data1]+data2
    else:
        pts = [data1, data2]
    T = Tree.Tree()
    T.root = Tree.Node(pts)
    T.root.left = t1
    T.root.right = t2
    return T



def buscarMinimos(matriz):
    minimo = math.inf
    (fila,columna)=(0,0)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if (i != j) and (minimo>matriz[i][j]):
                minimo = matriz[i][j]
                (fila,columna)=(i,j)         
    return (fila,columna)

# Algoritmo de clustering
def clustering(listaGenes,listaArboles,matriz):
    while len(listaArboles)>1:
        # Buscamos los genes con la menor distancia
        (i,j) = buscarMinimos(matriz)    
        # Creamos el arbol con los genes que hay en i y j
        tI=listaArboles[i]
        tJ=listaArboles[j] 
        treeIJ=tmerge(tI,tJ)
        # Quitamos estos arboles de la lista de arboles
        listaArboles.remove(tI)
        listaArboles.remove(tJ)
        # Quitamos esos genes de la matriz
        cluster1=matriz[i]
        cluster2=matriz[j]
        matriz.remove(cluster1) 
        matriz.remove(cluster2)
        maxi=max(i,j)
        mini=min(i,j)
        for ind, fila in enumerate(matriz):
            fila = fila[:maxi] + fila[maxi+1:]
            fila = fila[:mini] + fila[mini+1:]
            matriz[ind] = fila
        # Actualizar matriz
        matriz = actualizarMatriz(matriz,listaArboles,treeIJ)
        # Añadimos el nuevo arbol a la lista de arboles
        listaArboles.append(treeIJ)
    return listaArboles[0]
    
def actualizarMatriz(matriz, listaArboles, nuevoCluster):
    # Nueva fila en la matriz para el nuevo nodo
    distancias=[]
    for arbol in listaArboles:
        if type(arbol.root.data[0])!=list:
            distancias.append(distanciaEntreCluster(arbol.root.data, nuevoCluster))
        else:
            d_aux=[]
            for cluster in arbol.root.data:
                d_aux.append(distanciaEntreCluster(cluster, nuevoCluster))
            distancias.append(min(d_aux))
    for fila in matriz:
        i = matriz.index(fila)
        fila.append(distancias[i])
    distancias.append(0.0)
    matriz.append(distancias)
    
    return matriz


def distanciaEntreCluster(clusterExistente,nuevoCluster):
    # Para calcular la distancia entre dos cluster, 
    # nos quedamos con la distancia minima entre todos los elementos de ambos cluster
    minimo = math.inf
    # ---------------------
    # genesNuevos =   converter(nuevoCluster.root,[])
    # genesNuevos= nuevoCluster.root.data
    # genesExistentes =  converter(clusterExistente.root,[]) 
    # ----------------------
    # if type(clusterExistente[0])!=list:
    #     for genJ in nuevoCluster:
    #         distancia = calcularDistanciaEuclidea(clusterExistente,genJ)
    #         if minimo>distancia:
    #             minimo=distancia
    
    # else:
    #     for genI in clusterExistente:
    #         for genJ in nuevoCluster:
    #             distancia = calcularDistanciaEuclidea(genI,genJ)
    #             if minimo>distancia:
    #                 minimo=distancia
    # return minimo
    genI=clusterExistente
    for genJ in nuevoCluster.root.data:
        distancia = calcularDistanciaEuclidea(genI,genJ)
        if minimo>distancia:
            minimo=distancia
    return minimo

 
def converter(input_list, output_list):
    for elements in input_list:
        if type(elements) == list:
            converter(elements,output_list)
        else:
            output_list.append(elements)
    return output_list

# Metodo para calcular la distancia euclidea entre dos genes
def calcularDistanciaEuclidea(primerGen,segundoGen):
    d = sum([((float(a)-float(b))**2) for (a, b) in zip(primerGen[1:-1], segundoGen[1:-1])])   
    return d

# Metodo para hacer la matriz de distancias recibiendo la lista de genes        
def calcularMatriz(listaGenes):
    # Por cada lista de genes, calcular la distancia euclidea con todos los 
    # otros genes y meterlo en la matriz
    matriz=[]
    # por cada elemento en la lista de genes
    for i in range(len(listaGenes)):
        # creamos una lista para sus distancias
        listaGen = []
        # metemos en la lista la distancia con los otros nodos
        for j in range(len(listaGenes)):
            # calculamos la distancia
            distancia = calcularDistanciaEuclidea(listaGenes[i].data,listaGenes[j].data) 
            # metemos la distancia en la lista de distancias
            listaGen.append(distancia)
        # metemos la lista de distancias en la matriz
        matriz.append(listaGen)
    return matriz

#si un nodo esta vacio, en vez de None, se devuelve una lista vacia
def obtenerSegundoNivel(arbolFinal):
    lista=[]
    try:
        ci=arbolFinal.root.left
        cii=ci.root.left
        clusterIzquierdoIzquierdo=cii.root.data
        lista.append(clusterIzquierdoIzquierdo)
    except:
        clusterIzquierdoIzquierdo=[]
        lista.append(clusterIzquierdoIzquierdo)
    try:
        ci=arbolFinal.root.left
        cid=ci.root.right
        clusterIzquierdoDerecho=cid.root.data
        lista.append(clusterIzquierdoDerecho)
    except:
        clusterIzquierdoDerecho=[]
        lista.append(clusterIzquierdoDerecho)
    try:
        cd=arbolFinal.root.right
        cdi=cd.root.left
        clusterDerechoIzquierdo=cdi.root.data
        lista.append(clusterDerechoIzquierdo)
    except:
        clusterDerechoIzquierdo=[]
        lista.append(clusterDerechoIzquierdo)
    try:
        cd=arbolFinal.root.right
        cdd=cd.root.right
        clusterDerechoDerecho=cdd.root.data
        lista.append(clusterDerechoDerecho)
    except:
        clusterDerechoDerecho=[]
        lista.append(clusterDerechoDerecho)
    # lista=[clusterIzquierdoIzquierdo],[clusterIzquierdoDerecho],[clusterDerechoIzquierdo],[clusterDerechoDerecho]
    listagenes=[]
    for gen in lista:
        if gen==[]:
            listagenes.append(gen)
        elif type(gen[0])!=list:
            listagenes.append(gen[0])
        else:
            lista2 = []
            for x in gen:
                lista2.append(x[0])
            listagenes.append(lista2)
    return listagenes    

# Leemos el fichero de genes y calculamos las distancias
def genegroup(genes):
    #se abre el fichero genes y se leen los datos
    fichero = open(genes, 'r')
    listaGenes = []
    for linea in fichero: 
        gen = Gen(linea.split(","))
        listaGenes.append(gen)
    matriz = calcularMatriz(listaGenes) 
    listaArboles=[]
    for i in range(len(listaGenes)):
        tree = Tree.Tree()
        tree.root = listaGenes[i]
        listaArboles.append(tree)
    arbolFinal= clustering(listaGenes,listaArboles,matriz) 
    genes = obtenerSegundoNivel(arbolFinal)
    return genes
            
if __name__ == '__main__':
    genes = genegroup("./genes.txt") 
    
    print(genes)