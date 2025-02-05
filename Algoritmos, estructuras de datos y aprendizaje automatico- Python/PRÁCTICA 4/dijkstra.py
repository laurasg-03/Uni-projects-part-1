# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 15:38:50 2022

@author: Laura
"""

#############################################################################
#
#  Project: Auxiliary code for the ALGED labs
#  File:    dijkstra.py
#  Rev.     1.1
#  Date:    11/20/2022
#
#  This is the auxiliaty code for the implementation of the Dijkstra
#  algorithm.
#
#  The parts where you are supposed to intervene are marked as
#  TO-DO. The auxiliary functions that you might (and probably will)
#  need should be placed in the marked area. The rest will stay as it
#  is, but we urge you to have a look at it, as it contains useful
#  examples of programming techniques.
#
#  (C) ALGED Lecturers, 2021, 2022
#
import sys
import math

####################################################################
#
#  Reads a graph from a file and returns an adjacency list in the
#  format specified in the lab statement. This should work fine with
#  all the files that we give you but, should you create your own file
#  be aware that error control is far from perfect.
#
def gload(fname):
    f = open(fname, "r")
    lines = [l for l in f.readlines() if len(l) > 2 and l[0] != '#']  # Read and remove comment and empty lines
    for l in lines:
        q = l.find('#')                                               # remove comments at the end of the line
        if q >= 0:
            l = l[:q]
            
    g = []
    for l in lines:
        g += [eval(l)]
    return g


####################################################################
#
#  PUT YOUR AUXILIARY FUNCTIONS HERE
#
class Nodo: #define los nodos que hay en la grafica
	def __init__(self, i):
		self.id = i
		self.vecinos = []
		self.visitado = False
		self.predecesor = None
		self.peso = float('inf')

	def agregarVecino(self, v, p):
		if v not in self.vecinos:
			self.vecinos.append([v, p])

class Grafo:
	def __init__(self):
		self.vertices = {}

	def agregarVertice(self, id):
		if id not in self.vertices:
			self.vertices[id] = Nodo(id)

	def agregarArista(self, src, dst, p):
		if src in self.vertices and dst in self.vertices:
			self.vertices[src].agregarVecino(dst, p)
			
	
	def camino(self, src, dst):
		camino = []
		actual = dst
		while actual != None:
			camino.insert(0, actual)
			actual = self.vertices[actual].predecesor
		return camino

	def minim(self, l):

		if len(l) > 0:
			m = self.vertices[l[0]].peso
			v = l[0]
			for e in l:
				if m > self.vertices[e].peso:
					m = self.vertices[e].peso
					v = e
			return v
		return None

####################################################################


###################################################################

def minpath(fname, src, dst):
    g1 = gload(fname)
    g = Grafo()
    for m in range(len(g1)):
        g.agregarVertice(m)
    for k in range(len(g1)):
        l = g1[k]
        for p in l:
            g.agregarArista(k, p[0], p[1])

    if src in g.vertices:
			
        g.vertices[src].peso = 0
        actual = src
        noVisitados = []
			
        for v in g.vertices:
            if v != src:
                g.vertices[v].peso = float('inf')
            g.vertices[v].predecesor = None
            noVisitados.append(v)

        while len(noVisitados) > 0:
				
                for vec in g.vertices[actual].vecinos:
                    if g.vertices[vec[0]].visitado == False:
						
                        if g.vertices[actual].peso + vec[1] < g.vertices[vec[0]].peso:
                            g.vertices[vec[0]].peso = g.vertices[actual].peso + vec[1]
                            g.vertices[vec[0]].predecesor = actual

				
                g.vertices[actual].visitado = True
                noVisitados.remove(actual)

				
                actual = g.minim(noVisitados)
        return g.camino(src,dst)
    else:
        return False

        # TODO: implment Dijkstra here

#
# Test script, should not be evaluated when the file is imported
#

if __name__ == "__main__":
    print(minpath("cien.dat", 98, 10))