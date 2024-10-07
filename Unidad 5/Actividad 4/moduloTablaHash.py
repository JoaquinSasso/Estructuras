class TablaHash:
   __tamano : int
   __tabla : list[list]
   __colisiones : int
   __indiceLlenado : list
   __original : int
   def __init__(self, tamano):
      self.__original = tamano
      self.__tamano = self.primo(int(tamano * 1.2))
      self.__tabla = []
      self.__longitudClave = len(str(self.__tamano))
      self.__indiceLlenado = [0] * self.__tamano
      self.__colisiones = 3
      self.inicializar()
      
   def inicializar(self):
      for i in range(self.__tamano):
         self.__tabla.append([])
      for i in range(self.__tamano):
         for j in range(self.__colisiones):
            self.__tabla[i].append(None)
   
   def hash(self, clave):
      clave = self.extraccion(clave, 4, 8)
      return clave % self.__tamano
   
   def insertar(self, valor):
      pos = self.hash(valor)
      i = 0
      while i < self.__colisiones and self.__tabla[pos][i] != None:
         i += 1
      if i < self.__colisiones:
         self.__tabla[pos][i] = valor
         self.__indiceLlenado[pos] += 1
      else:
         i = self.__original
         j = 0
         while i < self.__tamano and self.__tabla[i][j] != None:
            j+=1
            if j == 3:
               i += 1
               j = 0
         if i < self.__tamano:
            self.__tabla[i][j] = valor
            self.__indiceLlenado[i] += 1
         else:
            print("Tabla llena")
            
         
         
   def buscar(self, valor):
      pos = self.hash(valor)
      iteraciones = 0
      i = 0
      while i < self.__colisiones and self.__tabla[pos][i] != valor:
         i += 1
         iteraciones += 1
      if i < self.__colisiones:
         print(f"El valor se encontro despues de {iteraciones} iteraciones")
         return pos, i
      else:
         pos = self.__original
         i = 0
         while pos < self.__tamano and self.__tabla[pos][i] != valor:
            i += 1
            if i == 3:
               pos += 1
               i = 0
            iteraciones += 1
      if pos < self.__tamano:
         print(f"El valor se encontro despues de {iteraciones} iteraciones")
         return pos, i
      else:
         print(f"El valor no se encontro despues de {iteraciones} iteraciones")
         return -1, -1
   
   def mostrar(self):
      i = 0
      for i in range(self.__tamano):
         for j in range(self.__colisiones):
            if self.__tabla[i][j] != None:
               print(f"{i} -> {self.__tabla[i][j]}, ", end="")
            print()
         
         
   def primo(self, x):
      i = 2
      while ((i < x) and (x % i != 0)):
         i += 1
      if (i == x):
         return x
      else:
         return self.primo(x+1)

   def extraccion(self, dato, inicio, fin):
      dato = str(dato)
      dato = dato[inicio:fin]
      dato = int(dato)
      return dato
   
   def getElemento(self, hashValue):
      return self.__tabla[hashValue]

   def mostrarCantidadColisiones(self):
      i = 0
      print("Cantidad de colisiones:")
      for i in range(self.__tamano):
         cantidad = self.__indiceLlenado[i]
         if cantidad != 0:
            print(f"{i} colisiones: {cantidad}")
      print("Fin de la lista")