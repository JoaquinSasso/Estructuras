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
   
   def camino(self, vActual, vFin, visitados = set(), recorrido = []):
      visitados.add(vActual)
      recorrido.append(vActual)
      if vActual == vFin:
         return recorrido
      adyacentes = set(self.adyacentes(vActual)) - visitados
      for ady in adyacentes:
         return self.camino(ady, vFin, visitados, recorrido.copy())
