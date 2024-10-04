from moduloTablaHash import TablaHash
import random
import time

def main():
   tabla = TablaHash(1009)
   random.seed(time.time())
   
   for i in range(1000):
      numero = random.randint(40000000, 47000000)
      tabla.insertar(numero)
   
   opcion = 5
   while opcion != 0:
      opcion = int(input("""Menu de opciones
                         1. Agregar un valor
                         2. Buscar un valor
                         3. Suprimir un valor
                         4. Mostrar la tabla
                         5. Calcular hash de un valor
                         6. Mostrar cantidad de colisiones
                         0. Salir
                         Ingrese una opcion: """))
      if opcion == 1:
         valor = int(input("Ingrese el valor a agregar: "))
         tabla.insertar(valor)
      elif opcion == 2:
         valor = int(input("Ingrese el valor a buscar: "))
         pos = tabla.buscar(valor)
         if pos != -1:
            print(f"El valor se encuentra en la posicion {pos}")
         else:
            print("El valor no se encuentra en la tabla")
      elif opcion == 3:
         valor = int(input("Ingrese el valor a suprimir: "))
         tabla.suprimir(valor)
      elif opcion == 4:
         tabla.mostrar()
      elif opcion == 5:
         valor = int(input("Ingrese el valor a calcular el hash: "))
         print(f"El hash del valor es {tabla.hash(valor)}")
      elif opcion == 6:
         tabla.mostrarCantidadColisiones()
      elif opcion == 0:
         print("Saliendo...")
      else:
         print("Opcion no valida")

if __name__ == "__main__":
   main()
   