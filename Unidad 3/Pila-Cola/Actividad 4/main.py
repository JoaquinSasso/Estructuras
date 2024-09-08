from moduloPilaEnlazada import pilaEnlazada
def potencia(base, exponente):
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado

def mostrar(torres):
   print("El estado de las torres es:")
   for i in range(3):
      print(f"Torre {i+1}", end=": ")
      for dato in torres[i]:
         print(dato, end=" ")
      print()

def juego(torres, cantidadDiscos):
   contador = 0
   while not torres[2].llena(cantidadDiscos):
      try:
         sacar = int(input("Escriba la torre de la que desea sacar un disco: "))
      except ValueError:
         print("El numero introducido no es un numero entero")
      else:
         try:
            disco = torres[sacar-1].suprimir()
         except ValueError:
            print("El numero introducido no es un numero entero")
         else:
            if disco != None:
               poner = int(input("Escriba la torre de la que desea poner un disco: "))
               aux = torres[poner-1].suprimir()
               if aux == None:
                  torres[poner-1].insertar(disco)
                  contador += 1
               elif aux > disco:
                  torres[poner-1].insertar(aux)
                  torres[poner-1].insertar(disco)
                  contador += 1
               else:
                  print("El disco no puede ser colocado en la torre porque es mayor que el que hay en ella")
                  torres[sacar-1].insertar(disco)
                  torres[poner-1].insertar(aux)
            else:
               print("No hay discos en la torre")
            mostrar(torres)
   return contador
   
def main():
   torre1 = pilaEnlazada()
   torre2 = pilaEnlazada()
   torre3 = pilaEnlazada()
   contador = 0
   cantidadDiscos = int(input("Escriba la cantidad de discos con los que desea jugar: "))
   for i in range(cantidadDiscos,0,-1):
      torre1.insertar(i)
   torres = [torre1, torre2, torre3]
   mostrar(torres)
   contador = juego(torres, cantidadDiscos)
   print(f"GANASTE!!! Has realizado {contador} movimientos")
   print(f"La cantidad minima de jugadas era {potencia(2,cantidadDiscos)-1}")

if __name__ == "__main__":
   main()