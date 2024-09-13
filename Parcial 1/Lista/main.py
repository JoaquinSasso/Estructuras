from moduloListaSecuencial import ListaSecuencial
from moduloListaEnlazada import ListaEnlazada

def main():
   #lista = ListaSecuencial(5)
   lista = ListaEnlazada()
   
   lista.insertarIndice(1,0)
   lista.insertarIndice(2,1)
   lista.insertarIndice(3,0)
   lista.insertarIndice(4,2)
   lista.insertarIndice(5,1)
   
   # lista.insertarOrdenado(3)
   # lista.insertarOrdenado(4)
   # lista.insertarOrdenado(2)
   # lista.insertarOrdenado(1)
   # lista.insertarOrdenado(5)

   lista.mostrar()
   
   print(f"Se suprimio: {lista.suprimirIndice(2)}")
   
   lista.mostrar()

if __name__ == "__main__":
   main()