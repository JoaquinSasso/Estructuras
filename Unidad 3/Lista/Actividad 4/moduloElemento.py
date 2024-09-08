class Elemento:
   __fila : int
   __columna : int
   __valor : int
   
   def __init__(self, fila = 0, columna = 0, valor = 0):
      self.__fila = fila
      self.__columna = columna
      self.__valor = valor
   
   def setFila(self, fila):
      self.__fila = fila
   
   def setColumna(self, columna):
      self.__columna = columna
   
   def setValor(self, valor):
      self.__valor = valor
   
   def getFila(self):
      return self.__fila
   
   def getColumna(self):
      return self.__columna
   
   def getValor(self):
      return self.__valor
   
   def __lt__(self, otro):
      if self.__fila < otro.getFila() and self.__columna < otro.getColumna():
         return True
      else:
         return False
   
   def __eq__(self, otro):
      if self.__fila == otro.getFila() and self.__columna == otro.getColumna():
         return True
      else:
         return False
   
   def __le__(self, otro):
      filaOtro = otro.getFila()
      columnaOtro = otro.getColumna()
      if self.__fila < filaOtro:
         return True
      elif self.__fila == filaOtro:
         if self.__columna <= columnaOtro:
            return True
         else:
            return False
      else:
         return False
         
   def __str__(self):
      return "Fila: " +str(self.__fila) + ", Columna: " + str(self.__columna) + ", Valor: " + str(self.__valor)