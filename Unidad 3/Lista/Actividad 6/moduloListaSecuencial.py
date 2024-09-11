import numpy as np

class ListaSecuencial:
   __arreglo : np.ndarray
   __ultimo : int
   __indice : int
   
   def __init__(self, tope : int):
      self.__arreglo = np.empty(tope, dtype=object)
      self.__ultimo = 0
      self.__indice = 0
   
   def insertar(self, elemento : object, posicion : int) -> None:
      if posicion < 0 or posicion >= len(self.__arreglo):
         raise Exception("Posicion fuera de rango")
      elif self.__ultimo + 1 > len(self.__arreglo):
         raise Exception("Lista llena")
      elif posicion == self.__ultimo:
         self.__arreglo[self.__ultimo] = elemento
         self.__ultimo += 1
      else:
         for i in range(self.__ultimo-1, posicion-1, -1):
            self.__arreglo[i+1] = self.__arreglo[i]
         self.__arreglo[posicion] = elemento
         self.__ultimo += 1
   
   def recuperar(self, posicion : int) -> object:
      if posicion < 0 or posicion > self.__ultimo:
         raise Exception("Posicion fuera de rango")
      else:
         return self.__arreglo[posicion]
   
   def suprimir(self, posicion : int) -> object:
      if posicion < 0 or posicion > self.__ultimo:
         raise Exception("Posicion fuera de rango")
      else:
         if posicion == self.__ultimo:
            self.__ultimo -= 1
            elemento = self.__arreglo[posicion]
         else:
            elemento = self.__arreglo[posicion]
            for i in range(posicion, self.__ultimo-1):
               self.__arreglo[i] = self.__arreglo[i+1]
            self.__ultimo -= 1
         return elemento
   
   def vacia(self) -> bool:
      return self.__ultimo == 0
   
   def primerElemento(self) -> object:
      if self.__ultimo == 0:
         raise Exception("Lista vacia")
      else:
         return self.__arreglo[0]
   
   def ultimoElemento(self) -> object:
      if self.__ultimo == 0:
         raise Exception("Lista vacia")
      else:
         return self.__arreglo[self.__ultimo-1]
      
   def buscar(self, elemento : object) -> int:
      i = 0
      while ((i < self.__ultimo) and (self.__arreglo[i] != elemento)):
         i += 1
      if i == self.__ultimo:
         raise Exception("Elemento no encontrado")
      else:
         return i
   
   def siguienteElemento(self, posicion : int) -> object:
      if posicion < 0 or posicion+1 > self.__ultimo:
         raise Exception("Posicion fuera de rango")
      else:
         return posicion + 1
   
   def anteriorElemento(self, posicion : int) -> object:
      if posicion-1 < 0 or posicion > self.__ultimo:
         raise Exception("Posicion fuera de rango")
      else:
         return posicion - 1
   
   def cantidadElementos(self) -> int:
      return self.__ultimo
   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__indice == self.__ultimo:
         self.__indice = 0
         raise StopIteration
      else:
         elemento = self.__arreglo[self.__indice]
         self.__indice += 1
         return elemento