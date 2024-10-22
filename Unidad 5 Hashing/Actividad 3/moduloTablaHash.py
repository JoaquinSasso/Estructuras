class TablaHash:
   __tamano : int
   __tabla : list[list]
   __colisiones : list
   def __init__(self, tamano):
      self.__tamano = self.primo(tamano)
      self.__tabla = []
      self.__longitudClave = len(str(self.__tamano))
      self.inicializar()
      
   def inicializar(self):
      for i in range(self.__tamano):
         self.__tabla.append([])
   
   def hash(self, clave):
      clave = self.plegamiento(clave, self.__longitudClave)
      return clave % self.__tamano
   
   def insertar(self, valor):
      pos = self.hash(valor)
      self.__tabla[pos].append(valor)
         
   def buscar(self, valor):
      pos = self.hash(valor)
      i = 0
      while i < len(self.__tabla[pos]) and self.__tabla[pos][i] != valor:
         i += 1
      if i < len(self.__tabla[pos]):
         print(f"El valor se encontro despues de {i} iteraciones")
         return pos, i
      else:
         print(f"El valor no se encontro despues de {i} iteraciones")
         return -1, -1
   
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

   def plegamiento(self, dato, longitudClave):
      dato = str(dato)
      longitud = len(dato)
      partes = (longitud // longitudClave)
      if longitud % longitudClave != 0:
         partes += 1
      suma = 0
      i = 0
      while i < partes:
         if i * longitudClave + longitudClave > longitud:
            suma += int(dato[i * longitudClave:longitud])
         else:
            suma += int(dato[i * longitudClave:(i + 1) * longitudClave])
         i += 1
      return suma
   
   def getElemento(self, hashValue):
      return self.__tabla[hashValue]

   def calcularPromedioColisiones(self):
      total = 0
      for lista in self.__tabla:
         total += len(lista)
      return total / self.__tamano

   def cantidadFueraPromedio(self):
      rango = 3
      promedio = self.calcularPromedioColisiones()
      cantidad = 0
      for lista in self.__tabla:
         if len(lista) >= promedio + rango or len(lista) <= promedio - rango:
            cantidad += 1
      return cantidad

   def mostrarCantidadColisiones(self):
      i = 0
      print("Cantidad de colisiones:")
      for i in range(self.__tamano):
         cantidad = len(self.__tabla[i])
         if cantidad != 0:
            print(f"{i} colisiones: {cantidad}")
      print("Fin de la lista")