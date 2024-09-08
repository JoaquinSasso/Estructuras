from moduloListaEnlazadaOrdenada import ListaEnlazada
from moduloListaSecuencialOrdenada import ListaSecuencial

def mostrarLista(lista):
   print("El estado de la lista es:")
   for elemento in lista:
      print(elemento, end=", ")
   print()

def main():
   #lista = ListaEnlazada()
   lista = ListaSecuencial(5)
   lista.insertar(4)
   lista.insertar(2)
   lista.insertar(3)
   mostrarLista(lista)
   lista.suprimir(1)
   mostrarLista(lista)
   lista.insertar(1)
   lista.insertar(5)
   mostrarLista(lista)

if __name__ == "__main__":
   main()