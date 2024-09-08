import numpy as np
class pilaSecuencial:
   __pila : np.ndarray
   __maximo : int
   __tope : int
   
   def __init__(self, tope = 5):
      self.__maximo = tope
      self.__pila = np.empty(self.__maximo, dtype=object)
      self.__tope = -1
      self.__indice = 0
   
   def insertar(self, elemento):
      try:
         if self.__tope + 1 < self.__maximo:
            self.__tope += 1
            self.__pila[self.__tope] = elemento
         else:
            raise Exception("La pila está llena")
      except Exception as e:
         print(e)
   
   def vacia(self):
      return self.__tope == -1
   
   def suprimir(self):
      elemento : object
      if self.__tope == -1:
         elemento = None
      else:
         elemento = self.__pila[self.__tope - 1]
         self.__pila[self.__tope] = None
         self.__tope -= 1
      return elemento
   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__tope == self.__indice:
         self.__indice = 0
         raise StopIteration
      else:
         elemento = self.__pila[self.__indice]
         self.__indice += 1
         return elemento
   
   def llena(self):
      return self.__tope == self.__maximo - 1