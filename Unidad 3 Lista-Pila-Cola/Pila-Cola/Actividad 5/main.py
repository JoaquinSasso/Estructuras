from moduloColaEnlazada import ColaEnlazada

def main():
   #tamaño = int(input("Ingrese tamaño de la cola: "))
   cola = ColaEnlazada()
   opcion = "a"
   while opcion != "q":
      print("El estado de la cola es:")
      for elemento in cola:
         print(elemento, end=" ")
      print()
      opcion = input("Opcion: ")
      if opcion == "i":
         numero = int(input("Ingrese numero: "))
         try:
            cola.insertar(numero)
         except Exception as e:
            print(e)
      if opcion == "e":
         print(f"Eliminando {cola.eliminar()}")

if __name__ == "__main__":
   main()