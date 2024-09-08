class NodoCursor:
   __dato : object
   __siguiente : int
   
   def __init__(self, dato : object, siguiente : int = -2):
      self.__dato = dato
      self.__siguiente = siguiente
   
   def getSiguiente(self) -> int:
      return self.__siguiente
   
   def setSiguiente(self, siguiente : int) -> None:
      self.__siguiente = siguiente
   
   def getDato(self) -> object:
      return self.__dato
   
   def setDato(self, dato : object) -> None:
      self.__dato = dato
   
   def __str__(self) -> str:
      return str(self.__dato)