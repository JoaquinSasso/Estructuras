from moduloNodo import Nodo

class ListaEnlazada:
   __cabeza : Nodo
   __cantidad : Nodo
   
   def __init__(self):
      self.__cabeza = None
      self.__cantidad = 0
      self.__actual = None
      
   
   def insertarIndice(self, elemento, indice):
      if indice < 0 and indice > self.__cantidad:
         return print("Indice fuera de rango")
      nuevoNodo = Nodo(elemento)
      self.__cantidad += 1
      if self.__cabeza == None:
         nuevoNodo.setSig(self.__cabeza)
         self.__cabeza = nuevoNodo
         self.__actual = self.__cabeza
      else:
         i = 0
         actual = self.__cabeza
         anterior = actual
         while actual != None and  i != indice:
            i += 1
            anterior = actual
            actual = actual.getSig()
         if actual == self.__cabeza:
            nuevoNodo.setSig(self.__cabeza)
            self.__cabeza = nuevoNodo
            self.__actual = self.__cabeza
         else:
            anterior.setSig(nuevoNodo)
            nuevoNodo.setSig(actual)
      
   def suprimirIndice(self, indice: int):
      if 0 <= indice and indice <= self.__cantidad:
         i = 0
         actual = self.__cabeza
         while i + 1 != indice and actual.getSig() != None:
            i += 1
            actual = actual.getSig()
         dato : Nodo = actual.getSig()
         actual.setSig(dato.getSig())
         return dato.getDato()
      else:
         print("Indice fuera de rango")
      
      
   def mostrar(self):
      print("El estado de la lista es:")
      actual = self.__cabeza
      while actual != None:
         print(actual.getDato(), end=", ")
         actual = actual.getSig()
      print()
            