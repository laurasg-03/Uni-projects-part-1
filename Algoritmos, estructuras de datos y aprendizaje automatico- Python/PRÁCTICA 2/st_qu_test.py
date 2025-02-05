###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 2
# Fichero: st_qu_test.py
# Autor: Laura Sánchez Garzón//Lidia Peña Morante
# Fecha: 01/11/2022
#
# Crear un fichero st_qu_test.py que, cuando se ejecute con una lista de enteros:
# python st_qu_test.py <n1> <n2> .... <nk>
# implemente las siguientes operaciones:
# a) Crea una pila para contener enteros.
# b) Crea una cola para contener enteros.
# c) Inserta en la pila y en la cola los elementos <n1> .... <nk>
# d) Extraer uno a uno los elementos de la pila y de la cola, imprimiendolos en pantalla.
#
###############################################################

import sys
import stack as s
import queue as q

if __name__ == '__main__':
    # Creamos la pila
    stack=s.Stack()
    #Creamos la cola
    queue = q.queue()
    # Rellenamos la pila y la cola
    for i in range(1,len(sys.argv)):
        # Metemos los datos
        stack.push(int(sys.argv[i]))
        queue.enqueue(int(sys.argv[i]))
    # Vaciamos la pila e imprimimos
    print("PILA:")
    while (not stack.empty()):
        data = stack.pop()
        print(data)
    print("----------------")    
    # Vaciamos la cola e imprimimos
    print("COLA:")
    while (not queue.empty()):
        data = queue.dequeue()
        print(data)
    print("----------------\n")     