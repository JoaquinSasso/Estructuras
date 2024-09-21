from moduloNodo import nodo

class ListaEnlazada:
   __cabeza : nodo
   __cantidad : int
   __siguiente : nodo
   
   def __init__(self):
      self.__cabeza = None
      self.__cantidad = 0
      self.__siguiente = None
   
   def insertar(self, elemento : object, posicion : int) -> None:
      nuevoNodo = nodo(elemento)
      if self.__cabeza == None:
         self.__cabeza = nuevoNodo
         self.__siguiente = nuevoNodo
         self.__cantidad += 1
      elif posicion == 0:
         nuevoNodo.setSiguiente(self.__cabeza)
         self.__cabeza = nuevoNodo
         self.__cantidad += 1
         self.__siguiente = nuevoNodo
      elif posicion <= self.__cantidad:
         nodoActual = self.__cabeza
         i = 0
         while i < posicion-1:
            nodoActual = nodoActual.getSiguiente()
            i += 1
         nuevoNodo.setSiguiente(nodoActual.getSiguiente())
         nodoActual.setSiguiente(nuevoNodo)
         self.__cantidad += 1
      else:
         raise Exception("Posicion fuera de rango")
   
   def suprimir(self, posicion : int) -> object:
      if self.__cantidad == 0:
         raise Exception("Lista vacia")
      elif posicion == 0:
         elemento = self.__cabeza.getSiguiente
         self.__cabeza = elemento
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
   
   def recuperar(self, posicion : int) -> object:
      if self.__cantidad == 0:
         raise Exception("Lista vacia")
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
         return self.__cabeza
      
   def ultimoElemento(self) -> object:
      if self.__cantidad == 0:
         raise Exception("Lista vacia")
      else:
         elemento = self.__cabeza
         i = 0
         while i < self.__cantidad-1:
            elemento = elemento.getSiguiente()
            i += 1
         return elemento
      
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