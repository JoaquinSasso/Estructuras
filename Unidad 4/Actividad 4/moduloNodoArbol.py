class NodoArbol:
   __izquierda : object
   __derecha : object
   __dato : object
   __balance : int

   def __init__(self, dato):
      self.__izquierda = None
      self.__derecha = None
      self.__dato = dato
      self.__balance = 0
   
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

   def actualizarBalance(self, balance):
      self.__balance = balance
   
   def getBalance(self):
      return self.__balance
   