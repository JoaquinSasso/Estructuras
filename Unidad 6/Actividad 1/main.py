from moduloGrafoSecuencial import grafoSecuencial
import time

def main():
   g = grafoSecuencial(5)
   g.agregarArista(0, 1)
   g.agregarArista(1, 2)
   g.agregarArista(1, 3)
   g.agregarArista(2, 4)

   inicio = time.time()
   print(g.hayarCamino(3, 4))
   print(f"El grafo es conexo: {g.conexo()}")
   fin = time.time()
   print(f"Tiempo de ejecución: {fin - inicio}")
if __name__ == "__main__":
   main()