def modulo(clave, cantidad):
   return clave % cantidad

def extraccion(clave, cantidad):
   clave = str(clave)
   clave = clave[-3:]
   clave = int(clave)
   return modulo(clave, cantidad)

def cuadradoMedio(clave, cantidad):
   clave = clave * clave
   print(f"El cuadrado es: {clave}")
   clave = str(clave)
   medio = len(clave) // 2
   clave = clave[medio-1:medio+2]
   clave = int(clave)
   return modulo(clave, cantidad)

def alfanumerico(clave, cantidad):
   sumador = 0
   for char in clave:
      sumador += ord(char)
   return modulo(sumador, cantidad)


def plegamiento(clave, cantidad):
   clave = str(clave)
   half = len(clave) // 2
   first = int(clave[0 : half])
   second = int(clave[half :])
   return modulo(first + second, cantidad)