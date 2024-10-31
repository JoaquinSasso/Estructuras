class Grafo:
   __matriz : list[list[int]]
   __cantVertices : int
   
   def __init__(self, cantVertices) -> None:
      self.__cantVertices = cantVertices
      self.__matriz = []
      for i in range(cantVertices):
         self.__matriz.append([0] * cantVertices)
   
   def agregarArista(self, v1, v2, peso):
      self.__matriz[v1][v2] = peso
      self.__matriz[v2][v1] = peso
   
   def adyacentes(self, v): #Devuelve la lista de adyacentes del vertice v que recibe como parametro
      lista = []
      for i in range(self.__cantVertices):
         if self.__matriz[v][i] != 0:
            lista.append(i)
      return lista
   
   def camino(self, vActual, vFin, visitados = set(), recorrido = []): #Encuentra el camino entre vActual y vFin de manera recursiva y considerando ciclos
      visitados.add(vActual)
      recorrido.append(vActual)
      if vActual == vFin and self.__matriz[vActual][vFin] != 0: #Si se intenta ir desde un vertice a el mismo y hay loop
         return recorrido
      adyacentes = self.adyacentes(vActual)
      if vFin in adyacentes:  #Si el vertice final es adyacente del actual
         recorrido.append(vFin)
         return recorrido
      else:
         for ady in adyacentes:
            if ady not in visitados: #Se evitan los nodos que ya han sido visitados
               return self.camino(ady, vFin, visitados, recorrido.copy()) #Se analizan todos los adyacentes del actual que todavia no hayan sido visitados
