from moduloGrafoSecuencial import grafoSecuencial
import time

def main():
   g = grafoSecuencial(5)
   g.agregarArista(0, 1)
   g.agregarArista(1, 2)
   g.agregarArista(1, 3)
   g.agregarArista(2, 4)

   print("Imprimiendo grafo en anchura desde el 0")
   g.recorrridoAnchura(0)
   print("Imprimiendo grafo en profundidad desde el 0")
   g.recorridoProfundidad(0)
if __name__ == "__main__":
   main()