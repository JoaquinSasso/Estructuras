from moduloPilaSecuencial import pilaSecuencial

def main():
   pila = pilaSecuencial(5)
   print(f"La pila esta vacia: {pila.vacia()}")
   pila.insertar(1)
   pila.insertar(2)
   pila.insertar(3)
   print(f"El primer elemento es: {pila.suprimir()}")
   for item in pila:
      print(item)
   print(f"La pila esta vacia: {pila.vacia()}")
   pila.insertar(4)
   pila.insertar(5)
   print(f"Ahora el primer elemento es: {pila.suprimir()}")
   pila.insertar(6)
   for item in pila:
      print(item)

if __name__ == "__main__":
   main()