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
      
      print("Altura del árbol:", arbol.altura())
      print("Nivel del dato 30:", arbol.nivel(30))
      print("Nivel del dato 5:", arbol.nivel(5))
      print("Los datos mostrados de manera ordenada son:")
      arbol.preOrden(arbol.raiz())
      print()
      print("Suprimir el dato 30")
      arbol.suprimir(30)
      print("Los datos mostrados de manera ordenada son:")
      arbol.preOrden(arbol.raiz())
      print()

if __name__ == "__main__":
    main()