class TablaHash:
   __tamano : int
   __tabla : list
   __colisiones : list
   def __init__(self, tamano):
      self.__tamano = self.primo(tamano)
      self.__tabla = [None] * self.__tamano
      self.__colisiones = [0] * self.__tamano
   
   def hash(self, clave):
      return clave % self.__tamano
   
   def insertar(self, valor):
      pos = self.hash(valor)
      colisiones = 0
      if self.__tabla[pos] == None:
         self.__tabla[pos] = valor
      else:
         while self.__tabla[pos] != None:
            colisiones += 1
            pos = (pos + 7) % self.__tamano
         if self.__tabla[pos] == None:
            self.__tabla[pos] = valor
         else:
            print("Tabla llena")
      self.__colisiones[colisiones] += 1
   
   def buscar(self, valor):
      pos = self.hash(valor)
      if self.__tabla[pos] == valor:
         return pos
      else:
         while self.__tabla[pos] != valor:
            pos = (pos + 1) % self.__tamano
            if pos == self.hash(valor):
               return -1
         return pos
   
   def suprimir(self, valor):
      pos = self.buscar(valor)
      if pos != -1:
         self.__tabla[pos] = None
      else:
         print("Valor no encontrado")
   
   def mostrar(self):
      i = 0
      while i < self.__tamano:
         if self.__tabla[i] != None:
            print(f"{i} -> {self.__tabla[i]}")
         i += 1
   
   def mostrarCantidadColisiones(self):
      i = 0
      print("Cantidad de colisiones:")
      for i in range(len(self.__colisiones)):
         if self.__colisiones[i] != 0:
            print(f"{i} colisiones: {self.__colisiones[i]}")
      print("Fin de la lista")
   
   def primo(self, x):
      i = 2
      while ((i < x) and (x % i != 0)):
         i += 1
      if (i == x):
         return x
      else:
         return self.primo(x+1)