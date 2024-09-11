import numpy as np

class ListaSecuencial:
   __arreglo : np.ndarray
   __ultimo : int
   __indice : int
   
   def __init__(self, tope : int):
      self.__arreglo = np.empty(tope, dtype=object)
      self.__ultimo = 0
      self.__indice = 0
   
   def insertar(self, elemento : object) -> None:
      if self.__ultimo == len(self.__arreglo):
        print("Lista llena")
      elif self.__ultimo == 0:
         self.__arreglo[0] = elemento
         self.__ultimo += 1
      else:
         i = 0
         while((i < self.__ultimo) and (self.__arreglo[i] <= elemento)):
            i += 1
         if i < len(self.__arreglo):
            for j in range(self.__ultimo, i, -1):
               self.__arreglo[j] = self.__arreglo[j-1]
            self.__arreglo[i] = elemento
            self.__ultimo += 1
         else:
           print("Lista llena")
   
   def recuperar(self, posicion : int) -> object:
      if posicion < 0 or posicion > self.__ultimo:
        print("Posicion fuera de rango")
      else:
         return self.__arreglo[posicion]
   
   def suprimir(self, posicion : int) -> object:
      if posicion < 0 or posicion > self.__ultimo:
        print("Posicion fuera de rango")
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
        print("Lista vacia")
      else:
         return self.__arreglo[0]
   
   def ultimoElemento(self) -> object:
      if self.__ultimo == 0:
         print("Lista vacia")
      else:
         return self.__arreglo[self.__ultimo-1]
      
   def buscar(self, elemento : object) -> int:
      piso = 0
      techo = self.__ultimo
      medio = int((piso + techo) / 2)
      while piso <= techo and self.__arreglo[medio] != elemento:
         if self.__arreglo[medio] < elemento:
            piso = medio +1
         else:
            techo = medio -1
         medio = int((piso + techo) / 2)
      if self.__arreglo[medio] == elemento:
         indice = medio
      else:
         indice = -1
      return indice
   
   def siguienteElemento(self, posicion : int) -> object:
      if posicion < 0 or posicion+1 > self.__ultimo:
        print("Posicion fuera de rango")
      else:
         return posicion + 1
   
   def anteriorElemento(self, posicion : int) -> object:
      if posicion-1 < 0 or posicion > self.__ultimo:
        print("Posicion fuera de rango")
      else:
         return posicion - 1
   
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