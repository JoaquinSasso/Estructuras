from moduloColaSecuencial import ColaSecuencial

def main():
   
   cola = ColaSecuencial(5)
   
   cola.insertar(1)
   cola.insertar(2)
   cola.insertar(3)
   cola.insertar(4)
   cola.insertar(5)
   cola.mostrar()
   print("Se suprimieron:", end=" ")
   print(cola.suprimir(), end=" y ")
   print(cola.suprimir())
   cola.insertar(6)
   cola.insertar(7)
   cola.mostrar()

if __name__ == "__main__":
   main()
   