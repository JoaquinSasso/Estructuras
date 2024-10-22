class NodoArbol:
   __izquierda : object
   __derecha : object
   __dato : object

   def __init__(self, dato):
      self.__izquierda = None
      self.__derecha = None
      self.__dato = dato
   
   def getDato(self):
      return self.__dato
   
   def setDato(self, dato):
      self.__dato = dato
   
   def getIzquierda(self):
      return self.__izquierda
   
   def setIzquierda(self, nodo):
      self.__izquierda = nodo
   
   def getDerecha(self):
      return self.__derecha
   
   def setDerecha(self, nodo):
      self.__derecha = nodo