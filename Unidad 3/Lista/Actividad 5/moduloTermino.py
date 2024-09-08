class Termino:
   __coeficiente : int
   __grado : int
   
   def __init__(self, coeficiente : int, grado : int):
      self.__coeficiente = coeficiente
      self.__grado = grado
   
   def setGrado(self, grado : int) -> None:
      self.__grado = grado
   
   def setCoeficiente(self, coeficiente : int) -> None:
      self.__coeficiente = coeficiente
   
   def getGrado(self) -> int:
      return self.__grado
   
   def getCoeficiente(self) -> int: 
      return self.__coeficiente
   
   def __str__(self) -> str:
      return str(self.__coeficiente) + "x^" + str(self.__grado)
   
   def __eq__(self, otro : object) -> bool:
      if self.__grado == otro.getGrado():
         return True
      else:
         return False
   
   def __gt__(self, otro : object) -> bool:
      if self.__grado > otro.getGrado():
         return True
      else:
         return False
   
   def __ge__(self, otro : object) -> bool:
      if self.__grado >= otro.getGrado():
         return True
      else:
         return False