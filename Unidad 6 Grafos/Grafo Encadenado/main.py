from moduloGrafoEncadenado import grafoEncadenado
import time

def main():
   g = grafoEncadenado(5)
   g.agregarArista(0, 1, 1)
   g.agregarArista(0, 2, 1)
   g.agregarArista(1, 3, 1)
   g.agregarArista(2, 4, 1)
   
   print(f"El grafo es conexo = {g.conexo()}")
   print(f"El grafo es aciclico = {g.aciclico()}")
   
   print("Recorrido en anchura:")
   g.recorridoAnchura(0)
   print("\nRecorrido en profundidad:")
   g.recorridoProfundidad(0)
   
if __name__ == "__main__":
   main()