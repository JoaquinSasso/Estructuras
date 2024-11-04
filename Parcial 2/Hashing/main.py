from bucket import bucket
import random

def main():
   tabla = bucket(1000)
   for _ in range(1000):
      clave = random.randint(44000000, 46000000)
      tabla.insertar(clave)
   
   print(tabla.buscar(clave))
   print(tabla.buscar(4499189))

if __name__ == "__main__":
   main()