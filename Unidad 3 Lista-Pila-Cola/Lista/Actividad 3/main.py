from moduloListaCursor import ListaCursor

def mostrar(lista : ListaCursor) -> None:
   for dato in lista:
      print(dato, end=", ")
   print()

def main():
   lista = ListaCursor(5)
   lista.insertar(3)
   lista.insertar(1)
   mostrar(lista)
   lista.insertar(2)
   lista.insertar(5)
   lista.insertar(4)
   mostrar(lista)
   lista.suprimir(2)
   lista.suprimir(1)
   lista.insertar(2.5)
   mostrar(lista)
   print(lista.recuperar(2))
   print(lista.siguienteElemento(1))
   print(lista.anteriorElemento(3))
      
if __name__ == "__main__":
   main()