# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 22:40:56 2022

@author: Laura
"""
###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 3
# Fichero: diagnosis.py
# Autor: Laura Sanchez Garzon//Lidia Peña Morante
# Fecha: 23/11/2022
#
# El ejercicio nos pide implementar una función en el codigo que se nos aporta como ayuda. 
# Esa funcion es plevel(a,"medium"), lo que hará será devolver una lista de listas con todos los caminos
# del árbol que llevan a una hoja con ese nivel de riego, ese nivel es "medium". 
# Para que la función se ejecute correctamente hemos creado una funcion recursiva, plevel_r, en la que tendremos un caso base,
# el cual será una hoja, entonces no habrá más caminos por recorrer. Y luego, el caso recursivo, en el que vamos añadiendo
# a una lista vacía los nodos que va recorriendo. 
###############################################################

#############################################################################
#
#  Project: Auxiliary code for the ALGED labs
#  File:    diagnosis.py
#  Rev.     1.0
#  Date:    11/16/2021
#
#
#  These are the support functions for the second part of Lab 3,
#  relative to a diagnostic tree. These functions read the tree from a
#  file, define the type of node that is in the tree. It is up to you
#  to use them to implement the function "risk" that returns all the
#  paths that lead to the given risk situation.
#
#
#  The diagnostic is stored in a file with the following format. Each
#  line is a node
#
#  ID, left, right, descl, descr
#
#  ID is the identifier of the node (not used in the program, but I am
#  too much of a programmer to create an entity without giving it an
#  ID. left can be 0 or 1: 0 means that the node has no left sub-tree,
#  1 means that it does; right is the same for the right
#  sub-tree. descl and descr are the descriptions of the conditions
#  that lead to follow the left or right path, respectively. If the
#  node has only one child, one of the two description is empty, if it
#  is a leaf, there is only one description, and is the risk level
#  associated to that path.
#
#  The tree is stored in the file recursively:
#
#  Node
#  |
#  | left sub-tree (if any)
#  |
#  |
#  | right sub-tree (if any)
#  |

#
#  This should work, since you have created a file that is called
#  "Arboles.py"
#
from Tree import *

import sys

#
# Data structure for this exercise. This is what is stored in the data
# field of the tree nodes. Each node contains the following fields:
#
# id:    The id of the node
#  
#  leaf: True if this node is a leaf (it is redundant, since this
#        indication can be obtained from the Node of the tree, but
#        useful.
#
#  cond_l: description of teh condition that leads to the left
#          sub-tree (None if tehre is no left-subtree)
#  cond_r: description of the condition that leads to the right
#          sub-tree (None if tehre is no right sub-tree)
#
#  level: if the node is a leaf, the level of risk associated to this
#         leaf. None if the node is not a leaf
#
class Delem:
    def __init__(self, id):
        self.id = id
        self.leaf = False
        self.cond_l = None
        self.cond_r = None
        self.level = None

#
# Recursive function that reads a tree from an open file. Reads the
# nodes then, if the node is not a leaf, calls itself to read the
# sub-trees. Returns a Node: the unterface function will take care of
# creating a tree with this node as the root.
#
def _read_t(f):
    line = f.readline()
    data = line.split(",")
    n = Delem(int(data[0]))
    lft = int(data[1])
    rgt = int(data[2])
    if lft == 0 and rgt == 0:
        n.leaf = True
        n.level = data[3].strip()
        tn = Node(n)
        return tn
    if lft != 0:
        n.cond_l = data[3].strip()
    if rgt != 0:
        n.cond_r = data[4].strip()
    tn = Node(n)
    if lft != 0:
        tn.left = _read_t(f)
    if rgt != 0:
        tn.right = _read_t(f)
    return tn


#
# reads the data from a given file and returns a tree with those data
#
def t_read(file):
    f = open(file, "r")
    n = _read_t(f)
    t = Tree()
    t.root = n
    return t


###########################################################################
#
# This is the function that you have to implement. It receives a tree
# and a risk level (low, medium, high). It returns a list of paths,
# containing all the paths from the root of the tree to the nodes with
# the given risk level
#
def plevel(a, lev):
    return plevel_r(a.root,lev)
    
    
def plevel_r(node,level):
    d=node.data
    if d.leaf:
        if d.level==level:
            return [[d.level]]
        else:
            return []
    else:
        res= []
        lst=plevel_r(node.left,level)
        for n in lst:
            w=[d.cond_l]+n
            res=res+[w]
        lst=plevel_r(node.right,level)
        for n in lst:
            w=[d.cond_r]+n
            res=res+[w]
        return res
    
#
###########################################################################


if __name__ == "__main__":
    a = t_read("./cholesterol.dat")
    lsts = plevel(a, "medium")

    print(lsts)