import numpy as np

class ColaSecuencial():
   __cantidad : int
   __primero : int
   __ultimo : int
   __cola : np.ndarray
   __inidce : int
   __maximo : int
   
   def __init__(self, maximo):
      self.__cola = np.empty(maximo, dtype=int)
      self.__maximo = maximo 
      self.__cantidad = 0
      self.__primero = 0
      self.__ultimo = -1
      self.__inidce = 0
   
   def insertar(self, elemento):
      if self.__cantidad == self.__maximo:
         raise Exception("Cola llena")
      else:
         indice = (self.__ultimo + 1)%self.__maximo
         self.__cola[indice] = elemento
         self.__ultimo += 1
         self.__cantidad += 1
   
   def eliminar(self):
      if self.__cantidad == 0:
         raise Exception("Cola vacia")
      else:
         elemento = self.__cola[self.__primero]
         self.__cantidad -= 1
         self.__primero += 1
         return elemento

   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__inidce == self.__maximo:
         self.__inidce = 0
         raise StopIteration
      else:
         elemento = self.__cola[self.__inidce]
         self.__inidce += 1
         return elemento