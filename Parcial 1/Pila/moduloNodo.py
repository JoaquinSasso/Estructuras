class Nodo:
   __dato : object
   __siguiente : object
   
   def __init__(self, dato, sig = None) -> None:
      self.__dato = dato
      self.__siguiente = sig
   
   def getDato(self):
      return self.__dato
   
   def getSig(self):
      return self.__siguiente
   
   def setSig(self, sig):
      self.__siguiente = sig
      
   def setDato(self, dato):
      self.__dato = dato
   