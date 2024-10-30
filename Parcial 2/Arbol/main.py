from moduloArbol import Arbol

def main():
   raiz = Arbol(10)
   raiz.insertar(5)
   raiz.insertar(15)
   raiz.insertar(3)
   raiz.insertar(7)
   raiz.insertar(13)
   raiz.insertar(18)
   raiz.insertar(4)
   raiz.insertar(1)
   raiz.insertar(6)
   raiz.insertar(8)
   raiz.insertar(11)
   raiz.insertar(14)
   raiz.insertar(16)
   
   raiz.suprimir(1)
   raiz.visualizar("Arbol suprimir 1")
   
if __name__ == "__main__":
   main()
   