from moduloTablaHash import TablaHash
import random
import time

def main():
   cantidadDatos = 1000
   tabla = TablaHash(cantidadDatos)
   random.seed(time.time())
   
   for i in range(cantidadDatos):
      numero = random.randint(40000000, 47000000)
      tabla.insertar(numero)
   
   opcion = 5
   while opcion != 0:
      opcion = int(input("""Menu de opciones
                         1. Agregar un valor
                         2. Buscar un valor
                         4. Mostrar la tabla
                         5. Calcular hash de un valor
                         6. Mostrar un hash
                         7. Cantidad de listas que difieren en 3 o mas del promedio
                         8. Mostrar cantidad de colisiones
                         0. Salir
                         Ingrese una opcion: """))
      if opcion == 1:
         valor = int(input("Ingrese el valor a agregar: "))
         tabla.insertar(valor)
      elif opcion == 2:
         valor = int(input("Ingrese el valor a buscar: "))
         hash, pos = tabla.buscar(valor)
         if pos != -1:
            print(f"El valor se encuentra en la posicion en el hash {hash} e indice {pos}")
      elif opcion == 4:
         tabla.mostrar()
      elif opcion == 5:
         valor = int(input("Ingrese el valor a calcular el hash: "))
         print(f"El hash del valor es {tabla.hash(valor)}")
      elif opcion == 6:
         hashValue = int(input("Ingrese el hash a buscar: "))
         lista = tabla.getElemento(hashValue)
         for elemento in lista:
            print(elemento)
      elif opcion == 7:
         print("Cantidad de listas que difieren en 3 o mas del promedio: ", tabla.cantidadFueraPromedio())
      elif opcion == 8:
         tabla.mostrarCantidadColisiones()
      elif opcion == 0:
         print("Saliendo...")
      else:
         print("Opcion no valida")

if __name__ == "__main__":
   main()
   