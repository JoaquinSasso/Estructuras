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
   dato = extraccion(dato, medio - diferencial, medio + diferencial)
   return dato

def plegamiento(dato, longitudClave):
   dato = str(dato)
   longitud = len(dato)
   partes = longitud // longitudClave
   suma = 0
   i = 0
   while i < partes:
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

print(alfanumerico("papa", 3))