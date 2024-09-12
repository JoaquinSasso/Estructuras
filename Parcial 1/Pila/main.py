from moduloPilaSecuencial import PilaSecuencial
from moduloPilaEnlazada import PilaEnlazada

def main():
   #pila = PilaSecuencial(4)
   pila = PilaEnlazada()
   
   pila.insertar(2)
   pila.insertar(3)
   pila.mostrar()
   pila.insertar(1)
   pila.insertar(5)
   pila.insertar(6)
   pila.mostrar()
   print("Se suprimio:")
   print(pila.suprimir())
   pila.mostrar()

if __name__ == "__main__":
   main()
