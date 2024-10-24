import heapq

class digrafoSecuencial:
   __matriz : list[list[int]]
   __cantNodos : int
   __visitados : set
   
   def __init__(self, cantNodos: int):
      self.__cantNodos = cantNodos
      self.__matriz = []
      self.__visitados = set()
      for i in range(0, cantNodos):
         self.__matriz.append([0] * cantNodos)
   
   def agregarArista(self, nodoOrigen: int, nodoFin: int, peso: int):
      self.__matriz[nodoOrigen][nodoFin] = peso
   
   def eliminarArista(self, nodoOrigen: int, nodoFin: int):
      self.__matriz[nodoOrigen][nodoFin] = 0
   
   def imprimirDigrafo(self):
      for i in range(0, self.__cantNodos):
         print(self.__matriz[i])
   
   def adyacentes(self, nodo):
      adyacentes = []
      pesos = []
      for i in range(0, self.__cantNodos):
         if self.__matriz[nodo][i] != 0:
            adyacentes.append(i)
            pesos.append(self.__matriz[nodo][i])
      return adyacentes, pesos
   
   def gradoEntrada(self, nodo):
      grado = 0
      for i in range(0, self.__cantNodos):
         if self.__matriz[i][nodo] != 0:
            grado += 1
      return grado
   
   def gradoSalida(self, nodo):
      grado = 0
      for i in range(0, self.__cantNodos):
         if self.__matriz[nodo][i] != 0:
            grado += 1
      return grado
   
   def fuente(self, nodo):
      return self.gradoEntrada(nodo) == 0 and self.gradoSalida(nodo) != 0
   
   def sumidero(self, nodo):
      return self.gradoEntrada(nodo) != 0 and self.gradoSalida(nodo) == 0
   
   def dijkstra(self, inicio: int):
      distancias = {nodo: float('inf') for nodo in range(self.__cantNodos)}
      distancias[inicio] = 0
      predecesores = {nodo: None for nodo in range(self.__cantNodos)}
      cola_prioridad = [(0, inicio)]
      
      while cola_prioridad:
         distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
         
         if distancia_actual > distancias[nodo_actual]:
            continue
         
         adyacentes, pesos = self.adyacentes(nodo_actual)
         for i, vecino in enumerate(adyacentes):
            peso = pesos[i]
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
               distancias[vecino] = distancia
               predecesores[vecino] = nodo_actual
               heapq.heappush(cola_prioridad, (distancia, vecino))
      
      return distancias, predecesores
   
   def reconstruirCamino(self, fin: int, predecesores: dict):
      camino = []
      nodo_actual = fin
      if predecesores[nodo_actual] is None:
         return None
      while nodo_actual is not None:
         camino.insert(0, nodo_actual)
         nodo_actual = predecesores[nodo_actual]
      return camino
   
   
   def fuertementeConexo(self):
      for i in range(0, self.__cantNodos):
         caminosActuales, predecesores = self.dijkstra(i)
         for nodo in range(self.__cantNodos):
            caminosAuxiliares, predecesoresAuxiliares = self.dijkstra(nodo)
            if caminosActuales[nodo] == float('inf') or caminosAuxiliares[i] == float('inf'):
               return False
         return True
   
   def simpleConexo(self):
      for i in range(0, self.__cantNodos):
         caminosActuales, predecesores = self.dijkstra(i)
         for nodo in range(self.__cantNodos):
            caminosAuxiliares, predecesoresAuxiliares = self.dijkstra(nodo)
            if caminosActuales[nodo] == float('inf') and caminosAuxiliares[i] == float('inf'):
               return False
         return True


   def DSF(self, nodoActual, nodoFin, caminoActual = []) -> list:
      caminoActual.append(nodoActual)
      self.__visitados.add(nodoActual)
      if nodoActual == nodoFin:
         self.__visitados.remove(nodoActual)
         if self.__matriz[nodoActual][nodoActual] == 1:
            caminoActual.append(nodoActual)
            return caminoActual
      adyacentes, pesos = self.adyacentes(nodoActual)
      if nodoFin in adyacentes:
         caminoActual.append(nodoFin)
         return caminoActual
      for a in adyacentes:
         if a in self.__visitados:
            continue
         nuevoCamino = self.DSF(a, nodoFin, caminoActual.copy())
         if nodoFin in nuevoCamino:
            return nuevoCamino
      return []

   def aciclico(self):
      for i in range(0, self.__cantNodos):
         self.__visitados = set()
         if self.DSF(i, i) != []:
            return False
      return True
   
   def recorrridoAnchura(self, nodoInicio):
      visitados = set()
      cola = [nodoInicio]
      visitados.add(nodoInicio)
      while cola:
         nodoActual = cola.pop(0)
         print(nodoActual)
         adyacentes, pesos = self.adyacentes(nodoActual)
         for a in adyacentes:
            if a not in visitados:
               visitados.add(a)
               cola.append(a)
   
   def recorridoProfundidad(self, nodoInicio, visitados = set()):
      print(nodoInicio)
      visitados.add(nodoInicio)
      adyacentes, pesos = self.adyacentes(nodoInicio)
      for a in adyacentes:
         if a not in visitados:
            self.recorridoProfundidad(a, visitados)
