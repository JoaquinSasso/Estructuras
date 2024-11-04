from hasheos import *
class bucket:
   __matriz : list[list[object]]
   __colisiones : list[int]
   __cantidad : int
   __overflow : int
   
   def __init__(self, cantidad):
      self.__cantidad = cantidad
      self.__overflow = int(cantidad * 1.2)
      self.__colisiones = [0] * self.__cantidad
      self.__matriz = [[None] * 5 for _ in range(self.__overflow)]
   
   def insertar(self, clave):
      h = modulo(clave, self.__cantidad)
      i = 0
      while(i < 5 and self.__matriz[h][i] != None):
         i += 1
      if i < 5:
         self.__matriz[h][i] = clave
         self.__colisiones[h] += 1
      else:
         i = self.__cantidad
         j = 0
         while(i < self.__overflow and self.__matriz[i][j] != None):
            j += 1
            if j == 5:
               i += 1
               j = 0
         if i < self.__overflow:
            self.__matriz[i][j] = clave
            self.__colisiones[h] += 1
   
   def buscar(self, clave):
      h = modulo(clave, self.__cantidad)
      i = 0
      while(i < 5 and self.__matriz[h][i] != clave):
         i += 1
      if i < 5:
         print(f"Se encontro en el hash {h} columna {i}")
         return id(self.__matriz[h][i])
      elif self.__colisiones[h] >= 5:
         i = self.__cantidad
         j = 0
         while(i < self.__overflow and self.__matriz[i][j] != None):
            j += 1
            if j == 5:
               i += 1
               j = 0
         if i < self.__overflow:
            print(f"Se encontro en zona de overflow, fila:{i} columna:{j}")
            return id(self.__matriz[i][j])
      print("No se encontro la clave")
      return None