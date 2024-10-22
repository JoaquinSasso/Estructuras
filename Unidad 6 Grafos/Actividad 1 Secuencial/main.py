from moduloGrafoSecuencial import grafoSecuencial
import time

def main():
   g = grafoSecuencial(5)
   g.agregarArista(0, 1, 1)
   g.agregarArista(1, 2, 1)
   g.agregarArista(1, 3, 1)
   g.agregarArista(2, 4, 1)
   
   caminos, predesores = g.dijkstra(0)
   
   print("Distancias: ", caminos)
   print("Predecesores: ", predesores)
   print("Camino de 0 a 4: ", g.reconstruirCamino(4, predesores))
   print(f"Camino con DSF: {g.DSF(0, 0)}")
   print(f"El grafo es aciclico: {g.aciclico()}")
   print(f"El grafo es conexo: {g.conexo()}")
if __name__ == "__main__":
   main()