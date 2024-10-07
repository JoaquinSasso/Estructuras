import time
def modulo(dato, tamano):
   return dato % tamano

def extraccion(dato, inicio, fin):
   dato = str(dato)
   dato = dato[inicio:fin]
   dato = int(dato)
   return dato

def cuadradoMedio(dato, longitudClave):
   dato = dato ** 2
   longitud = len(str(dato))
   medio = longitud // 2
   diferencial = longitudClave // 2
   if longitudClave % 2 != 0:
      dato = extraccion(dato, medio - diferencial, medio + diferencial +1)
   else:
      dato = extraccion(dato, medio - diferencial, medio + diferencial)
   return dato

def plegamiento(dato, longitudClave):
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

def alfanumerico(dato, longitudClave):
   dato = str(dato)
   longitud = len(dato)
   suma = 0
   i = 0
   while i < longitud:
      suma += ord(dato[i])
      i += 1
   return suma

def primo(x):
   i = 2
   while ((i < x) and (x % i != 0)):
      i += 1
   if (i == x):
      return x
   else:
      return primo(x+1)