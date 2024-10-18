from moduloGrafoSecuencial import grafoSecuencial

def main():
   g = grafoSecuencial(5)
   g.agregarArista(0, 1)
   g.agregarArista(1, 2)
   g.agregarArista(1, 3)
   g.agregarArista(2, 4)
   
   g.imprimirGrafo()
   print(g.adyacentes(0))
   print(g.camino(0, 4, []))
if __name__ == "__main__":
   main()