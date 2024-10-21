from moduloGrafoSecuencial import grafoSecuencial
import time

def main():
   g = grafoSecuencial(5)
   g.agregarArista(0, 1)
   g.agregarArista(1, 2)
   g.agregarArista(1, 3)
   g.agregarArista(2, 4)

   inicio = time.time()
   distancias, predecesores = g.dijkstra(0)
   print(distancias)
   print(f"Camino más corto: {g.reconstruir_camino(predecesores, 0, 4)}")
   fin = time.time()
   print(f"Tiempo de ejecución: {fin - inicio}")
if __name__ == "__main__":
   main()