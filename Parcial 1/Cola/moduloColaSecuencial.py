import numpy as np

class ColaSecuencial:
   __items : np.ndarray
   __ultimo: int
   __primero : int
   __cantidad : int
   __tope : int
   
   def __init__(self, tope):
      self.__items = np.empty(tope)
      self.__cantidad = 0
      self.__primero = 0
      self.__ultimo = -1
      self.__tope = tope
      
   def insertar(self, elemento):
      if self.__cantidad == self.__tope:
         print("No hay espcacio")
      else:
         i = (self.__ultimo+1) % self.__tope
         self.__items[i] = elemento
         self.__ultimo = i
         self.__cantidad += 1
   
   def suprimir(self):
      if self.__cantidad == 0:
         print("La cola esta vacia")
      else:
         elemento = self.__items[self.__primero]
         if self.__cantidad > 1:
            self.__primero = (self.__primero + 1) % self.__tope
         self.__cantidad -= 1
         return elemento
   
   
   def mostrar(self):
      print("Los elementos de la cola son:")
      i = self.__primero
      while i != self.__ultimo:
         print(self.__items[i], end=", ")
         i += 1
         if i >= self.__cantidad:
            i = 0
      print(self.__items[i])