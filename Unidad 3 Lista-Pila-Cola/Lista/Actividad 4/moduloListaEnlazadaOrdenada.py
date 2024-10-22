from moduloNodo import nodo

class ListaEnlazada:
   __cabeza : nodo
   __cantidad : int
   __siguiente : nodo
   
   def __init__(self):
      self.__cabeza = None
      self.__cantidad = 0
      self.__siguiente = None
   
   def insertar(self, elemento : object) -> None:
      nuevo_nodo = nodo(elemento)
      self.__cantidad += 1
      if self.__cabeza is None:
         self.__cabeza = nuevo_nodo
         self.__siguiente = self.__cabeza
      elif elemento <= self.__cabeza.getDato():
         nuevo_nodo.setSiguiente(self.__cabeza)
         self.__cabeza = nuevo_nodo
         self.__siguiente = self.__cabeza
      else:
         actual = self.__cabeza
         while actual.getSiguiente() is not None and actual.getSiguiente().getDato() <= elemento:
               actual = actual.getSiguiente()
         nuevo_nodo.setSiguiente(actual.getSiguiente())
         actual.setSiguiente(nuevo_nodo)
            
   def suprimir(self, posicion : int) -> None:
      if self.__cantidad == 0:
         raise Exception("Lista vacia")
      elif posicion == 0:
         elemento = self.__cabeza
         self.__cabeza = self.__cabeza.getSiguiente()
         self.__cantidad -= 1
      elif posicion <= self.__cantidad:
         i = 0
         nodoActual = self.__cabeza
         while i < posicion:
            anterior = nodoActual
            nodoActual = nodoActual.getSiguiente()
            i += 1
         elemento = nodoActual.getDato()
         anterior.setSiguiente(nodoActual.getSiguiente())
         self.__cantidad -= 1
         return elemento
   
   def recuperar(self, posicion : int) -> object:
      if self.__cantidad == 0:
         raise Exception("Lista vacia")
      if posicion < 0 or posicion > self.__cantidad:
         raise Exception("Posicion fuera de rango")
      else:
         elemento = self.__cabeza
         i = 0
         while i < posicion-1:
            elemento = elemento.getSiguiente()
            i += 1
         return elemento.getDato()
   
   def primerElemento(self) -> object:
      if self.__cantidad == 0:
         raise Exception("Lista vacia")
      else:
         return self.__cabeza.getDato()
      
   def ultimoElemento(self) -> object:
      if self.__cantidad == 0:
         raise Exception("Lista vacia")
      else:
         elemento = self.__cabeza
         i = 0
         while i < self.__cantidad-1:
            elemento = elemento.getSiguiente()
            i += 1
         return elemento.getDato()
      
   def buscar(self, elemento : object) -> int:
      if self.__cantidad == 0:
         raise Exception("Lista vacia")
      else:
         i = 0
         nodoActual = self.__cabeza
         while ((i < self.__cantidad) and (nodoActual.getDato() != elemento)):
            nodoActual = nodoActual.getSiguiente()
            i += 1
         if i == self.__cantidad:
            raise Exception("Elemento no encontrado")
         else:
            return i
   
   def siguienteElemento(self, posicion : int) -> object:
      if posicion < 0 or posicion+1 > self.__cantidad:
         raise Exception("Posicion fuera de rango")
      else:
         return posicion + 1
   
   def anteriorElemento(self, posicion : int) -> object:
      if posicion-1 < 0 or posicion > self.__cantidad:
         raise Exception("Posicion fuera de rango")
      else:
         return posicion - 1
   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__siguiente == None:
         self.__siguiente = self.__cabeza
         raise StopIteration
      else:
         elemento = self.__siguiente.getDato()
         self.__siguiente = self.__siguiente.getSiguiente()
         return elemento
   
   def vacia(self) -> bool:
      return self.__cantidad == 0
   
   def getCantidad(self):
      return self.__cantidad