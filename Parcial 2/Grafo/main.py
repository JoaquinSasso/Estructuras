from moduloDigrafo import Digrafo
from moduloGrafo import Grafo
def main():
   d = Digrafo(5)
   d.agregarArista(0, 1, 1)
   d.agregarArista(1, 2, 1)
   d.agregarArista(2, 3, 1)
   d.agregarArista(3, 4, 1)
   d.mostrarFuentes()

   
   g = Grafo(5)
   g.agregarArista(0, 2, 1)
   g.agregarArista(2, 1, 1)
   g.agregarArista(1, 3, 1)
   g.agregarArista(3, 4, 1)
   print(g.camino(0,0))
   
if __name__ == "__main__":
   main()