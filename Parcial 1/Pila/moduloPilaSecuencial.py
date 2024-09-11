import numpy as np

class PilaSecuencial:
   __cantidad: int
   __items : np.ndarray
   
   def __init__(self, cantidad):
      self.__cantidad = 0
      self.__items = np.empty(cantidad, dtype= object)
   
   def insertar(self, elemento):
      if self.__cantidad < len(self.__items):
         self.__items[self.__cantidad] = elemento
         self.__cantidad += 1
      else:
         print("No hay espacio suficiente")
   
   def suprimir(self) -> object:
      if self.__cantidad > 0:
         self.__cantidad -= 1
         elemento = self.__items[self.__cantidad]
      else:
         elemento = None
         print("La pila esta vacia")
      return elemento
      
   
   
   def mostrar(self):
      print("En la pila hay: ")
      for i in range(0, self.__cantidad):
         print(self.__items[i], end=", ")
      print()