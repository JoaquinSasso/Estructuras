from moduloNodoCursor import NodoCursor
import numpy as np

class ListaCursor:
   __lista : np.ndarray
   __cabeza : int
   __libre : int
   __cantidad : int
   __actual : int
   __tope : int
   
   def __init__(self, tope : int):
      self.__lista = np.empty(tope, dtype=ListaCursor)
      self.__cabeza = 0
      self.__libre = 0
      self.__cantidad = 0
      self.__actual = 0
      self.__tope = tope
      self.inicializar()
   
   
   def inicializar(self) -> None:
      for i in range(self.__tope-1):
         self.__lista[i] = NodoCursor(None, i + 1)
      self.__lista[self.__tope-1] = NodoCursor(None, -1)
      
   
   def insertar(self, dato : object):
      nodo = self.__lista[self.__libre]
      if self.__cantidad == self.__tope:
         raise Exception("Lista llena")
      elif self.__cantidad == 0:
         self.__cabeza = self.__libre
         self.__libre = nodo.getSiguiente()
         nodo.setDato(dato)
         nodo.setSiguiente(-1)
         self.__actual = self.__cabeza
         self.__cantidad += 1
      else:
         actual = self.__cabeza
         anterior = self.__cabeza
         while actual != -1 and self.__lista[actual].getDato() < dato:
            anterior = actual
            actual = self.__lista[actual].getSiguiente()  
         if self.__cabeza == actual:
            self.__cabeza = self.__libre
            self.__actual = self.__cabeza
         else:
            self.__lista[anterior].setSiguiente(self.__libre)
         self.__cantidad += 1
         self.__libre = nodo.getSiguiente()
         nodo.setDato(dato)
         nodo.setSiguiente(actual)


   def suprimir(self, indice : int) -> object:
      if indice >= self.__cantidad or indice < -1:
         raise Exception("Indice fuera de rango")
      elif indice == self.__cabeza:
         self.__lista[self.__cabeza].setDato(None)
         self.__cabeza = self.__lista[self.__cabeza].getSiguiente()
         self.__lista[indice].setSiguiente(self.__libre)
         self.__libre = indice
         self.__cantidad -= 1
      else:
         i = self.__cabeza
         while i != indice:
            anterior = i
            i = self.__lista[i].getSiguiente()
         dato = self.__lista[i].getDato()
         self.__lista[anterior].setSiguiente(self.__lista[i].getSiguiente())
         self.__lista[i].setDato(None)
         self.__lista[i].setSiguiente(self.__libre)
         self.__libre = indice
         self.__cantidad -= 1
         return dato
      
   
   def recuperar(self, indice : int) -> object:
      if indice >= self.__cantidad or indice < 0:
         raise Exception("Indice fuera de rango")
      i = self.__cabeza
      while i != -1 and i != indice:
         i = self.__lista[i].getSiguiente()
      if i == -1:
         return None
      else:
         return self.__lista[i].getDato()
   
   
   def siguienteElemento(self, indice : int) -> object:
      if indice >= self.__cantidad or indice < 0:
         raise Exception("Indice fuera de rango")
      i = self.__cabeza
      while i != -1 and i != indice:
         i = self.__lista[i].getSiguiente()
      if i == -1:
         return None
      else:
         return self.__lista[i].getSiguiente()
      
   
   def anteriorElemento(self, indice : int) -> object:
      if indice >= self.__cantidad or indice < 0:
         raise Exception("Indice fuera de rango")
      i = self.__cabeza
      while i != -1 and self.__lista[i].getSiguiente() != indice:
         i = self.__lista[i].getSiguiente()
      if i == -1:
         return None
      else:
         return i
   
   
   def primerElemento(self) -> object:
      return self.__lista[self.__cabeza].getDato()
   
   
   def ultimoElemento(self) -> object:
      i = self.__cabeza
      while self.__lista[i].getSiguiente() != -1:
         i = self.__lista[i].getSiguiente()
      return self.__lista[i].getDato()
   
   
   def buscar(self, dato : object) -> int:
      i = self.__cabeza
      while i != -1 and self.__lista[i].getDato() != dato:
         i = self.__lista[i].getSiguiente()
      return i
   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__actual == -1:
         self.__actual = self.__cabeza
         raise StopIteration
      else:
         dato = self.__lista[self.__actual].getDato()
         self.__actual = self.__lista[self.__actual].getSiguiente()
         return dato
