from moduloNodo import nodo
class pilaEnlazada:
   __cabeza : nodo
   __tope : int
   
   def __init__(self, tope = 0):
      self.__tope = tope
      self.__cabeza = None
   
   def vacia(self):
      return self.__cabeza == None
   
   def insertar(self, elemento):
      nuevoNodo = nodo(elemento)
      nuevoNodo.setSiguiente(self.__cabeza)
      self.__cabeza = nuevoNodo
      self.__tope += 1
   
   def suprimir(self):
      if self.__cabeza == None:
         elemento = None
      else:
         elemento = self.__cabeza.getDato()
         self.__cabeza = self.__cabeza.getSiguiente()
         self.__tope -= 1
      return elemento