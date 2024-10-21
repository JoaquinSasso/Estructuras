import heapq

class grafoSecuencial:
   __matriz : list[list[int]]
   __cantNodos : int
   __visitados : set
   
   def __init__(self, cantNodos: int):
      self.__cantNodos = cantNodos
      self.__matriz = []
      self.__visitados = set()
      for i in range(0, cantNodos):
         self.__matriz.append([0] * cantNodos)
   
   def agregarArista(self, nodoA: int, nodoB: int):
      self.__matriz[nodoA][nodoB] = 1
      self.__matriz[nodoB][nodoA] = 1
   
   def eliminarArista(self, nodoA: int, nodoB: int):
      self.__matriz[nodoA][nodoB] = 0
      self.__matriz[nodoB][nodoA] = 0
   
   def imprimirGrafo(self):
      for i in range(0, self.__cantNodos):
         print(self.__matriz[i])
   
   def adyacentes(self, nodo):
      adyacentes = []
      for i in range(0, self.__cantNodos):
         if self.__matriz[nodo][i] == 1:
            adyacentes.append(i)
      return adyacentes
   
   def camino(self, nodoActual, nodoFin, caminoActual) -> list:
      caminoActual.append(nodoActual)
      self.__visitados.add(nodoActual)
      if nodoActual == nodoFin and self.__matriz[nodoActual][nodoActual] == 1:
         caminoActual.append(nodoActual)
         return caminoActual
      adyacentes = self.adyacentes(nodoActual)
      if nodoFin in adyacentes :
         caminoActual.append(nodoFin)
         return caminoActual
      else:
         for a in adyacentes:
            if a in self.__visitados:
               continue
            nuevoCamino = self.camino(a, nodoFin, caminoActual.copy())
            if nodoFin in nuevoCamino:
               return nuevoCamino
      return []

   def hayarCamino(self, nodoInicio, nodoFin) -> list:
      caminoActual = []
      self.__visitados = set()
      camino = self.camino(nodoInicio, nodoFin, caminoActual)
      return camino
   
   def conexo(self):
      contador = 1
      for i in range(1, self.__cantNodos):
         camino = self.hayarCamino(0, i)
         if camino == []:
            return False
      return True


   def aciclico(self) -> bool:
      contador = 0
      for i in range(0, self.__cantNodos):
         camino = self.hayarCamino(i, i)
         if camino == []:
            contador += 1
      if contador == self.__cantNodos:
         return True
      return False
   
   def recorrridoAnchura(self, nodoInicio):
      visitados = set()
      cola = [nodoInicio]
      visitados.add(nodoInicio)
      while cola:
         nodoActual = cola.pop(0)
         print(nodoActual)
         adyacentes = self.adyacentes(nodoActual)
         for a in adyacentes:
            if a not in visitados:
               visitados.add(a)
               cola.append(a)
   
   def recorridoProfundidad(self, nodoInicio, visitados = set()):
      print(nodoInicio)
      visitados.add(nodoInicio)
      adyacentes = self.adyacentes(nodoInicio)
      for a in adyacentes:
         if a not in visitados:
            self.recorridoProfundidad(a, visitados)
   
   
   
   # def dijkstra(self, nodoInicio):
   #    distancias = [float('inf')] * self.__cantNodos
   #    distancias[nodoInicio] = 0
   #    predecesores = [None] * self.__cantNodos
   #    cola_prioridad = [(0, nodoInicio)]
   #    visitados = set()

   #    while cola_prioridad:
   #       distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

   #       if nodo_actual in visitados:
   #          continue

   #       visitados.add(nodo_actual)

   #       for vecino in range(self.__cantNodos):
   #          if self.__matriz[nodo_actual][vecino] != 0 and vecino not in visitados:
   #             distancia = self.__matriz[nodo_actual][vecino]
   #             nueva_distancia = distancia_actual + distancia

   #             if nueva_distancia < distancias[vecino]:
   #                distancias[vecino] = nueva_distancia
   #                predecesores[vecino] = nodo_actual
   #                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

   #    return distancias, predecesores

   # def reconstruir_camino(self, predecesores, nodoInicio, nodoObjetivo):
   #    camino = []
   #    nodo_actual = nodoObjetivo
   #    while nodo_actual is not None:
   #       camino.append(nodo_actual)
   #       nodo_actual = predecesores[nodo_actual]
   #    camino.reverse()
   #    return camino
      