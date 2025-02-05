###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 2
# Fichero: queue.py
# Autor: Laura Sánchez Garzón//Lidia Peña Morante
# Fecha: 01/11/2022
#
# Crear un fichero queue.py con la definición de la clase Queue que incluya todos los métodos:
# dequeue(): elimina el primer elemento de la cola
# enqueue(): inserta el elemento data en la cola
# empty(): devuelve True si la cola está vacía, False en caso contrario
#
###############################################################

import list as l

class queue(l.List):
    
    def enqueue(self,data):
        self.insert_at_tail(data)
        
    def dequeue(self):
        if self.head:
            data = self.head.data
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return data
        else:
            return None
        
    def empty(self):
        if self.head == None:
            return True
        else:
            return False