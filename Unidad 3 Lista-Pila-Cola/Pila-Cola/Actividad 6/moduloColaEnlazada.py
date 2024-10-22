from moduloNodo import nodo

class ColaEnlazada():
   __primero : nodo
   __ultimo : nodo
   __actual : nodo

   def __init__(self):
      self.__primero = None
      self.__actual = None
      self.__ultimo = None

   def insertar(self, elemento):
      nuevo = nodo(elemento)
      if self.__primero == None:
         self.__primero = nuevo
         self.__ultimo = nuevo
         self.__actual = nuevo
      else: 
         self.__ultimo.setSiguiente(nuevo)
         self.__ultimo = nuevo
   
   def eliminar(self):
      if self.__primero != None:
         elemento = self.__primero.getDato()
         self.__primero = self.__primero.getSiguiente()
         self.__actual = self.__primero
         return elemento
      
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__actual == None:
         self.__actual = self.__primero
         raise StopIteration
      else:
         elemento = self.__actual.getDato()
         self.__actual = self.__actual.getSiguiente()
         return elemento