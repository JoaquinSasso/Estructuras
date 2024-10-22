from moduloArbolBB import ArbolBinarioBusqueda

def main():
   arbol = ArbolBinarioBusqueda()
   arbol.insertar(30, arbol.raiz())
   arbol.insertar(20, arbol.raiz())
   arbol.insertar(40, arbol.raiz())
   arbol.insertar(10, arbol.raiz())
   arbol.insertar(25, arbol.raiz())
   arbol.insertar(35, arbol.raiz())
   arbol.insertar(50, arbol.raiz())
   arbol.insertar(5, arbol.raiz())
   arbol.insertar(15, arbol.raiz())
   arbol.insertar(45, arbol.raiz())
   arbol.insertar(60, arbol.raiz())
   arbol.insertar(1, arbol.raiz())
  
   print("La familia del nodo 20 es: ")
   arbol.PadreHermano(20)
   
   print("Los sucesores del 10 son:")
   arbol.sucesores(10)
   
   print(f"\n La altura del árbol es: {arbol.altura()}")
   
   print("La cantidad de nodos es: ", arbol.cantidadNodos(arbol.raiz()))
      

if __name__ == "__main__":
   main()