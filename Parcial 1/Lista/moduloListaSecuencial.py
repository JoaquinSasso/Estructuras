import numpy as np

class ListaSecuencial:
   __tope :int
   __ultimo : int
   __items : np.ndarray
   
   def __init__(self, tope) -> None:
      self.__tope = tope
      self.__ultimo = 0
      self.__items = np.zeros(tope, dtype=int)
   
   
   def insertarIndice(self, dato, indice):
      if 0 <= indice and indice <= self.__ultimo:
         if self.__ultimo+1 > self.__tope:
            print("La lista esta llena")
         elif indice != self.__ultimo+1:
            for i in range(self.__ultimo, indice, -1):
               self.__items[i] = self.__items[i-1]
            self.__items[indice] = dato
            self.__ultimo += 1
      else:
         print("Indice fuera de rango")
   
   
   def insertarOrdenado(self,dato):
      if self.__ultimo + 1 <= self.__tope:
         i = 0
         while i < self.__ultimo and self.__items[i] <= dato:
            i += 1
         for j in range(self.__ultimo, i, -1):
            self.__items[j] = self.__items[j-1]
         self.__items[i] = dato
         self.__ultimo += 1
      else:
         print("La lista esta llena")
      
      
   def suprimirIndice(self, indice):
      if 0 <= indice and indice <= self.__ultimo:
         dato = self.__items[indice]
         for i in range(indice,self.__ultimo-1):
            self.__items[i] = self.__items[i+1]
         self.__ultimo -= 1
         return dato
      else:
         print("El indice esta fuera de rango")
   
   def mostrar(self):
      print("El estado de la lista es: ")
      for i in range(self.__ultimo):
         print(self.__items[i], end=", ")
      print()
      
   
   def busquedaBinaria(self, elemento):
      piso = 0
      techo = self.__ultimo
      medio = int((piso - techo) / 2)
      while piso <= techo and self.__items[medio] != elemento:
         if self.__items[medio] < elemento:
            techo = medio - 1
         else:
            piso = medio + 1
         medio = int((piso - techo) / 2)