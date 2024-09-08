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
   
   lista2 = ListaEnlazada()
   lista2.insertar(Elemento(1, 1, 6))
   lista2.insertar(Elemento(12, 62, 3))
   lista2.insertar(Elemento(34, 21, 5))
   lista2.insertar(Elemento(50, 49, 7))
   lista2.insertar(Elemento(67, 23, 3))
   lista2.insertar(Elemento(95,88,9))
   
   matrizSuma = ListaEnlazada()
   
   i = 1
   j = 1
   
   while i < lista1.getCantidad() and j < lista2.getCantidad():
      elemento1 = lista1.recuperar(i)
      elemento2 = lista2.recuperar(j)
      if elemento1 == elemento2:
         matrizSuma.insertar(Elemento(elemento1.getFila(), elemento1.getColumna(), elemento1.getValor() + elemento2.getValor()))
         i += 1
         j += 1
      elif elemento1 < elemento2:
         matrizSuma.insertar(elemento1)
         i += 1
      else:
         matrizSuma.insertar(elemento2)
         j += 1
   
   while i <= lista1.getCantidad():
      elemento1 = lista1.recuperar(i)
      matrizSuma.insertar(elemento1)
      i += 1
   
   while j <= lista2.getCantidad():
      elemento2 = lista2.recuperar(j)
      matrizSuma.insertar(elemento2)
      j += 1
   
   
   print("El resultado de la matriz suma es: ")
   for elemento in matrizSuma:
      print(elemento)

   matrizProducto = ListaEnlazada()
   i = 1
   j = 1
   while i < lista1.getCantidad() and j < lista2.getCantidad():
      elemento1 = lista1.recuperar(i)
      elemento2 = lista2.recuperar(j)
      if elemento1 == elemento2:
         matrizProducto.insertar(Elemento(elemento1.getFila(), elemento1.getColumna(), elemento1.getValor() * elemento2.getValor()))
         i += 1
         j += 1
      elif elemento1 < elemento2:
         i += 1
      else:
         j += 1
   
   print("\nEl resultado de la matriz producto es: ")
   for elemento in matrizProducto:
      print(elemento)
if __name__ == "__main__":
   main()