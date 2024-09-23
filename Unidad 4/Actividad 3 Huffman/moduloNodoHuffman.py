class NodoHuffman:
   __str : str
   __frecuencia : int
   __izquierda : 'NodoHuffman'
   __derecha : 'NodoHuffman'
   
   def __init__(self, str, frecuencia):
      self.__str = str
      self.__frecuencia = frecuencia
      self.__izquierda = None
      self.__derecha = None
      
   def getStr(self):
      return self.__str
   
   def getFrecuencia(self):
      return self.__frecuencia
   
   def getIzquierda(self):
      return self.__izquierda
   
   def getDerecha(self):
      return self.__derecha
   
   def setIzquierda(self, izquierda):
      self.__izquierda = izquierda
   
   def setDerecha(self, derecha):
      self.__derecha = derecha