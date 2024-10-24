class Nodo:
   __peso : int
   __arista : int
   __siguiente : object
   
   def __init__(self, arista, peso, siguiente) -> None:
      self.__peso = peso
      self.__arista = arista
      self.__siguiente = siguiente
   
   def getPeso(self) -> int:
      return self.__peso
   
   def getArista(self) -> int:
      return self.__arista
   
   def getSiguiente(self) -> object:
      return self.__siguiente
   
   def setSiguiente(self, siguiente) -> None:
      self.__siguiente = siguiente