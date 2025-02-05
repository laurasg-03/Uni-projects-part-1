
###############################################################
#
# Algoritmos y Estructura de datos 2022-23
#
# Practica: 2
# Fichero: list.py
# Autor: Laura Sánchez Garzón//Lidia Peña Morante
# Fecha: 01/11/2022
#
# clase List para manejar listas usando la estructura Node
# implementando los siguientes métodos: 
# insert_at_tail//insert_at_head//delete//search//print_lst
# La función extra, buscar, será de utilizada para el ejercicio 4
###############################################################

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None


class List:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size=0
   
    def print_lst(self):
        if self.head==None:
            return
        nodo = self.head
        while nodo.next:
            print(nodo.data, end=" ")
            nodo=nodo.next
        print(nodo.data)    
        
        
    def search(self,pred):
            # Creamos la lista vacia donde se meteran los elementos que cumplan la condicion pred
            res = List()
            # Apuntamos a la cabeza
            elemento = self.head
            # Mientras el elemento no sea none (llegamos hasta el final)
            while elemento != None:
                if pred(elemento.data):
                    res.insert_at_tail(elemento.data)
                elemento = elemento.next
            return res  
        
    def insert_at_tail(self, data):
        # Creamos el nodo
        node= Node(data)
        # Si la lista esta vacia
        if self.head == None:
            self.head = node
        # Si la lista no está vacía lo añadimos al final
        else:
            # tail es el ultimo elemento de la lista
            # y su next está vacio, entonces al next, del último
            # elemento, que es tail, le metes el nodo
            self.tail.next = node
        # ahora el nodo ya está metido y hay que hacer, que tail
        # apunte al último elemento, ya que todavía apunta al penúltimo,
        self.tail = node    
        self.size+=1
    
    def insert_at_head(self, data):
        # Creamos el nodo
        node= Node(data)
        # Si la lista esta vacia
        if self.head == None: 
            # Metemos el nodo como head y como tail
            self.tail = node
        # Si no esta vacia    
        else:
            # Metemos en el next del nodo la cabeza de la lista
            node.next = self.head
        # actualizamos la cabeza
        self.head = node    
     
    def delete(self, pred):
        # Empezamos por la cabeza por eso le igualamos a head
        elementoAnterior = self.head
        elemento = self.head.next
        # Comprobamos que no se cumple la condicion en la cabeza, entonces empezamos el bucle
        if(not pred(elementoAnterior.data)):
            # Mientras el elemento no sea none Y el predicado no sea true, avanza
            while ((elemento!= None) and (not pred(elemento.data)) ):
                # Avanza el elemento (mirar los dibujos) y el anterior
                elementoAnterior = elemento
                elemento = elemento.next
            # Fuera de este bucle pueden pasar dos cosas
            # Se ha encontrado un elemento que cumpla la condicion,
            #entonces el elemento sera lo que haya que borrar
            # O hemos recorrido toda la lista sin exito y hemos llegado al final,
            # por lo que el elemento será None
            # entonces basta con mirar si el elemento se ha encontrado ( que no sea None)
            if (elemento!=None):
                # Antes de borrarlo comprobamos si es el últimpo
                if elemento == self.tail:
                    self.tail= elementoAnterior
                elementoAnterior.next=elemento.next    
                elemento.next=None
        # Pero si se cumple, tenemos que borrar la cabeza
        else:
            # Para borrar la cabeza hacemos que la cabeza de la lista, apunte al siguiente del nodo a borrar, en este caso es elemento
            self.head=elemento
            # para que el nodo que acabamos de borrar no apunte a nada apuntamos a none
            elementoAnterior.next = None


    def buscar(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        else:
            return False