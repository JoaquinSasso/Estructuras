from moduloListaEnlazada import ListaEnlazada
class TablaHash:
   __tamano : int
   __tabla : list[ListaEnlazada]
   __colisiones : list
   def __init__(self, tamano):
      self.__tamano = self.primo(tamano)
      self.__tabla = [ListaEnlazada()] * self.__tamano
      self.__longitudClave = len(str(self.__tamano))
   
   def hash(self, clave):
      clave = self.plegamiento(clave, self.__longitudClave)
      return clave % self.__tamano
   
   def insertar(self, valor):
      pos = self.hash(valor)
      self.__tabla[pos].insertar(valor)
         
   def buscar(self, valor):
      pos = self.hash(valor)
      if self.__tabla[pos] == valor:
         return hash, self.__tabla[pos].buscar(valor)
      else:
         return -1
   
   def suprimir(self, valor):
      pos = self.buscar(valor)
      if pos != -1:
         self.__tabla[pos].suprimir(valor)
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
         total += lista.getCantidad()
      return total / self.__tamano

   def cantidadFueraPromedio(self):
      promedio = self.calcularPromedioColisiones()
      cantidad = 0
      for lista in self.__tabla:
         if lista.getCantidad() >= promedio + 3 or lista.getCantidad() <= promedio - 3:
            cantidad += 1
      return cantidad

   def mostrarCantidadColisiones(self):
      i = 0
      print("Cantidad de colisiones:")
      for i in self.__tamano:
         print(f"{i} colisiones: {self.__tabla[i].getCantidad()}")
      print("Fin de la lista")