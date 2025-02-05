###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 2
# Fichero: stack.py
# Autor: Laura Sánchez Garzón//Lidia Peña Morante
# Fecha: 01/11/2022
#
# Crear un fichero stack.py con la definición de la clase Stack que incluya todos los métodos:
# pop(): elimina el primer elemento data de la pila
# push(data): inserta el elemento data en la pila
# empty(): devuelve True si la pila está vacía, False en caso contrario
#
###############################################################

import list as l 
       
class Stack(l.List):
    
    def push(self, data):
        self.insert_at_head(data)
    
    def pop(self):
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