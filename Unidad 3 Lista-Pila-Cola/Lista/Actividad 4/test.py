from moduloListaEnlazadaOrdenada import ListaEnlazada
from moduloElemento import Elemento

def main():
   lista1 = ListaEnlazada()
   lista1.insertar(Elemento(1, 1, 1))
   lista1.insertar(Elemento(12, 62, 6))
   lista1.insertar(Elemento(37, 13, 3))
   lista1.insertar(Elemento(45, 45, 5))
   lista1.insertar(Elemento(67, 23, 2))
   lista1.insertar(Elemento(83, 91, 7))
   
   
   for elemento in lista1:
      print(elemento)
   print()
   print(lista1.recuperar(5))

if __name__ == "__main__":
   main()