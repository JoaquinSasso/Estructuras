from moduloNodo import Nodo

class ListaEnlazada:
   __cabeza : Nodo
   __cantidad : Nodo
   
   def __init__(self):
      self.__cabeza = None
      self.__cantidad = 0
      
   
   def insertar(self, elemento, indice):
      if indice < 0 and indice > self.__cantidad:
         return print("Indice fuera de rango")
      nuevoNodo = Nodo()
      self.__cantidad += 1
      if self.__cabeza == None:
         nuevoNodo.setSig(self.__cabeza)
         self.__cabeza = nuevoNodo
      else:
         
         