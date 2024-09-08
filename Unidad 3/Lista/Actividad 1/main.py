from moduloListaSecuencial import ListaSecuencial
from moduloListaEnlazada import ListaEnlazada

def main():
   lista = ListaEnlazada()
   lista.insertar(1,0)
   lista.insertar(2,1)
   lista.insertar(3,0)
   lista.suprimir(1)
   lista.insertar(4,0)
   lista.insertar(5,2)
   lista.insertar(6,1)
   lista.suprimir(2)
   
   for element in lista:
      print(element)

if __name__ == "__main__":
   main()
