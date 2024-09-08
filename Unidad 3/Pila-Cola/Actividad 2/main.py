from moduloPilaEnlazada import pilaEnlazada
def main():
   pila = pilaEnlazada()
   numero = int(input("Ingrese un numero: "))
   bandera = True
   while bandera:
      division = numero // 2
      resto = numero % 2
      pila.insertar(resto)
      numero = division
      if division < 2:
         print(numero, end=" ")
         bandera = False
   while not pila.vacia():
      print(pila.suprimir(), end=" ")

if __name__ == "__main__":
   main()