from moduloNodo import Nodo

class PilaEnlazada:
   __cabeza: Nodo
   __cantidad : int
   
   def __init__(self):
      self.__cabeza = None
      self.__cantidad = 0
      
   def insertar(self, dato):
      nuevoNodo = Nodo(dato, self.__cabeza)
      self.__cabeza = nuevoNodo
      self.__cantidad += 1
   
   def suprimir(self):
      dato = self.__cabeza.getDato()
      self.__cabeza = self.__cabeza.getSig()
      self.__cantidad -= 1
      return dato
   
   def mostrar(self):
      print("Los elementos de la pila son:")
      actual = self.__cabeza
      while actual != None:
         print(actual.getDato(), end=", ")
         actual = actual.getSig()
      print()