###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 2
# Fichero: listatest.py
# Autor: Laura Sánchez Garzón//Lidia Peña Morante
# Fecha: 01/11/2022
#
# Crear un fichero listatest.py que, cuando ejecute con python listatest.py
# implemente las siguientes operaciones: 
# a) Crea una lista para contener números enteros
# b) Inserta en la lista los elementos
# c) Imprime el contenido de la lista
# d) Elimina de la lista el primer elemento 
# e) Imprime el contenido de la lista
# f) Busca en la lista todos los elementos mayores o iguales al ultimo elemento
# g) Imprime el resultado de la búsqueda
#
###############################################################

import sys
import list as lst

if __name__ == '__main__':
    #creamos la lista
    lst=lst.List()
    for i in range(1,len(sys.argv)):
        data=(sys.argv[i]) 
        lst.insert_at_tail(int(data))

    lst.print_lst()
    # eliminamos de la lista el primer elemento
    primero = int(sys.argv[1])
    lst.delete(lambda x: x==primero)
    lst.print_lst() 
    #definimos cual es el ultimo elemento de la lista
    #para imprimir una lista cuyos elementos sean mayores que el ultimo elemento
    ultimo = int(sys.argv[-1])
    mayores = lst.search(lambda x: x>=ultimo)
    mayores.print_lst()
    
    

    