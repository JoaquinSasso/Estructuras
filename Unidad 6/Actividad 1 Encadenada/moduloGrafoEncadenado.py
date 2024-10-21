from moduloNodo import Nodo

class grafoEncadenado:
   __cantNodos : int
   __nodos : list[Nodo]
   __visitados : set
   
   def __init__(self, cantNodos: int):
      self.__cantNodos = cantNodos
      self.__nodos = [None] * cantNodos
      self.__visitados = set()
      for i in range(0, cantNodos):
         self.__nodos.append(None)
         
   def agregarArista(self, nodoA: int, nodoB: int, peso: int):
      nodo = Nodo(nodoB, peso, self.__nodos[nodoA])
      self.__nodos[nodoA] = nodo
      nodo = Nodo(nodoA, peso, self.__nodos[nodoB])
      self.__nodos[nodoB] = nodo
   
   def adyacentes