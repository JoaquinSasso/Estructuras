from moduloGrafoSecuencial import grafoSecuencial
import time

def main():
   g = grafoSecuencial(10)
   g.agregarArista(0, 1)
   g.agregarArista(1, 2)
   g.agregarArista(1, 3)
   g.agregarArista(2, 4)
   g.agregarArista(3, 5)
   g.agregarArista(4, 6)
   g.agregarArista(5, 7)
   g.agregarArista(6, 8)
   g.agregarArista(7, 9)
   g.agregarArista(0,9)
   
   inicio = time.time()
   print(g.hayarCamino(3, 8))
   print(f"El grafo es conexo: {g.conexo()}")
   fin = time.time()
   print(f"Tiempo de ejecución: {fin - inicio}")
if __name__ == "__main__":
   main()