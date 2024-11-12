from hasheos import *
class direccionamientoAbierto:
   __arreglo : list
   __tamano : int
   
   def __init__(self, tamano):
      self.__tamano = tamano
      self.__arreglo = [None] * tamano
   
   def insertar(self, clave):
      h = modulo(clave, self.__tamano)
      if self.__arreglo[h] == None:
         self.__arreglo[h] = clave
      else:
         i = h + 1
         while(i != h and self.__arreglo[i] != None):
            i = (i + 1) % self.__tamano
         if i != h:
            self.__arreglo[i] = clave
         else:
            print("No se pudo insertar la clave")