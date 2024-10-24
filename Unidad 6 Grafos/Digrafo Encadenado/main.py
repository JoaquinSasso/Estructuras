from moduloDigrafoEncadenado import digrafoEncadenado
import time

def main():
   g = digrafoEncadenado(5)
   g.agregarArista(0, 1, 1)
   g.agregarArista(0, 2, 1)
   g.agregarArista(1, 3, 1)
   g.agregarArista(2, 4, 1)
   
   print(f"Grado de entrada del nodo 1 = {g.gradoEntrada(1)}")
   print(f"Grado de salida del nodo 0 = {g.gradoSalida(0)}")
   print(f"El nodo 0 es fuente = {g.nodoFuente(0)}")
   print(f"El nodo 4 es sumidero = {g.nodoSumidero(4)}")
   print(f"El grafo es simple conexo = {g.simpleConexo()}")
   print(f"El grafo es aciclico = {g.aciclico()}")
   print(f"El grafo es fuertemente conexo = {g.fuertementeConexo()}")
   
   
if __name__ == "__main__":
   main()