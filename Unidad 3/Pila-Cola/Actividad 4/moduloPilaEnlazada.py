from moduloNodo import nodo
class pilaEnlazada:
   __cabeza : nodo
   __tope : int
   __siguiente : nodo
   
   def __init__(self, tope = 0):
      self.__tope = tope
      self.__cabeza = None
      self.__siguiente = None
   
   def vacia(self):
      return self.__cabeza == None
   
   def insertar(self, elemento):
      nuevoNodo = nodo(elemento)
      nuevoNodo.setSiguiente(self.__cabeza)
      self.__cabeza = nuevoNodo
      self.__siguiente = nuevoNodo
      self.__tope += 1
   
   def suprimir(self):
      if self.__cabeza == None:
         elemento = None
      else:
         elemento = self.__cabeza.getDato()
         self.__cabeza = self.__cabeza.getSiguiente()
         self.__siguiente = self.__cabeza
         self.__tope -= 1
      return elemento
   
   def llena(self, tope):
      return self.__tope == tope
   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__siguiente == None:
         if self.__cabeza != None:
            self.__siguiente = self.__cabeza
         raise StopIteration
      else:
         elemento = self.__siguiente.getDato()
         self.__siguiente = self.__siguiente.getSiguiente()
         return elemento