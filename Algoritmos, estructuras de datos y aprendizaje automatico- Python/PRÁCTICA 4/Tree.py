# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 23:27:31 2022

@author: Laura
"""
###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 3
# Fichero: Tree.py
# Autor: Laura Sanchez Garzon//Lidia Peña Morante
# Fecha: 23/11/2022
#
# clase Tree para manejar arboles binarios usando funciones auxiliares y la 
# estructura Node, implementando los siguientes métodos: 
# insert//search//in_traverse//pre_traverse//post_traverse//height
# 
###############################################################

def n_insert(node, data, comp):
    if comp(data, node.data) < 0:
        if node.left == None:
            node.left = Node(data)
        else: 
            return n_insert(node.left, data, comp)
            
    elif comp(data, node.data) == 0:
        return None
    else: 
        if node.right == None:
            node.right = Node(data)
        else: 
            return n_insert(node.right, data, comp)
            
def n_search(node, data, comp):
    if node == None:
        return None
    q = comp(data, node.data)
    if q == 0:
        return node.data
    elif q<0:
        return n_search(node.left, data, comp)
    
    else: 
        return n_search(node.right, data, comp)

def n_in_traverse(node):
    if node == None:
        return []
    else:
        return n_in_traverse(node.left) + [node.data] + n_in_traverse(node.right) 

def n_pre_traverse(node):
    if node == None:
        return []
    else:
        return [node.data] + n_pre_traverse(node.left) + n_pre_traverse(node.right) 

def n_post_traverse(node):
    if node == None:
        return []
    else:
        return n_post_traverse(node.left) + n_post_traverse(node.right) + [node.data]
    
def n_height(node):
    if node == None:
        return 0
    else: 
        derecha=n_height(node.left)
        izquierda=n_height(node.right)
    return max(izquierda, derecha)+1

class Node:
    def __init__(self, tdata):
        self.data = tdata
        self.left= None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
    
    
    def insert(self, data, comp):
        if self.root == None: 
            nodo = Node(data)
            self.root = nodo
            
        else: 
            return n_insert(self.root, data, comp)
    
    def search (self, data, comp):
        if self.root == None:
            return None
        else: 
            return n_search(self.root, data, comp)
            
    def in_traverse (self):
        if self.root == None:
            return []
        else:
            return n_in_traverse(self.root)
    
    def pre_traverse (self):
        if self.root == None:
            return []
        else:
            return n_pre_traverse(self.root)
    
    def post_traverse (self):
        if self.root == None:
            return []
        else:
            return n_post_traverse(self.root)
            
    def height(self):
        if self.root == None:
            return 0
        else: 
            return n_height(self.root)
        

    
if __name__ == "__main__":

    def mycomp(x, y):
        return x - y
    t = Tree()
    t.insert(1, mycomp)
    t.insert(-2, mycomp)
    t.insert(43, mycomp)
    t.insert(6, mycomp)
    t.insert(-5, mycomp)

    
    m=t.search(6, mycomp)
    n=t.height()
    
    print (t.in_traverse())
    print (t.pre_traverse())
    print (t.post_traverse())
    print (m)
    print (n)
    



    

