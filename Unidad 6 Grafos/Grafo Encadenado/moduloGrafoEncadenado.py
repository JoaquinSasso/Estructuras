from moduloNodo import Nodo
import heapq

class grafoEncadenado:
   __cantNodos : int
   __nodos : list[Nodo]
   __visitados : set
   
   def __init__(self, cantNodos: int):
      self.__cantNodos = cantNodos
      self.__nodos = [None] * cantNodos
      self.__visitados = set()
         
   def agregarArista(self, nodoA: int, nodoB: int, peso: int):
      nodo = Nodo(nodoB, peso, self.__nodos[nodoA])
      self.__nodos[nodoA] = nodo
      nodo = Nodo(nodoA, peso, self.__nodos[nodoB])
      self.__nodos[nodoB] = nodo
   
   def adyacentes(self, nodo: int):
      adyacentes = []
      nodoActual = self.__nodos[nodo]
      while nodoActual is not None:
         adyacentes.append((nodoActual.getArista(), nodoActual.getPeso()))
         nodoActual = nodoActual.getSiguiente()
      return adyacentes

   def dijkstra(self, nodoInicio: int):
      distancias = {nodo: float('inf') for nodo in range(self.__cantNodos)}
      distancias[nodoInicio] = 0
      predecesores = {nodo: None for nodo in range(self.__cantNodos)}
      cola_prioridad = [(0, nodoInicio)]
      visitados = set()

      while cola_prioridad:
         distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

         if nodo_actual in visitados:
            continue

         visitados.add(nodo_actual)

         for vecino, peso in self.adyacentes(nodo_actual):
            if vecino not in visitados:
               nueva_distancia = distancia_actual + peso

               if nueva_distancia < distancias[vecino]:
                  distancias[vecino] = nueva_distancia
                  predecesores[vecino] = nodo_actual
                  heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

      return distancias, predecesores

   def reconstruir_camino(self, predecesores, nodoObjetivo):
      camino = []
      nodo_actual = nodoObjetivo
      while nodo_actual is not None:
         camino.append(nodo_actual)
         nodo_actual = predecesores[nodo_actual]
      camino.reverse()
      return camino
   
   def conexo(self):
      caminos, predecesores = self.dijkstra(0)
      for nodo in caminos:
         if caminos[nodo] == float('inf'):
            return False
      return True
   
   def DSF(self, nodoActual, nodoFin, printear = False, caminoActual = []) -> list:
      caminoActual.append(nodoActual)
      self.__visitados.add(nodoActual)
      if printear:
         print(nodoActual, end = " ")
      if nodoActual == nodoFin:
         self.__visitados.remove(nodoActual)
         if self.comprobarLoop(nodoActual):
            caminoActual.append(nodoActual)
            return caminoActual
      adyacentes = self.adyacentes(nodoActual)
      for a, p in adyacentes:
         if a == nodoFin:
            caminoActual.append(nodoFin)
            return caminoActual
      for a, p in adyacentes:
         if a in self.__visitados:
            continue
         nuevoCamino = self.DSF(a, nodoFin, printear, caminoActual.copy())
         if nodoFin in nuevoCamino:
            return nuevoCamino
      return []
   
   def comprobarLoop(self, nodo):
      nodoActual = self.__nodos[nodo]
      while nodoActual is not None:
         if nodoActual.getArista() == nodo:
            return True
         nodoActual = nodoActual.getSiguiente()
      return False
   
   def aciclico(self):
      for i in range(self.__cantNodos):
         self.__visitados.clear()
         if self.DSF(i, i, False) != []:
            return False
      return True
   
   def recorridoAnchura(self, nodoInicio):
      self.__visitados.clear()
      cola = []
      cola.append(nodoInicio)
      self.__visitados.add(nodoInicio)
      while cola:
         nodoActual = cola.pop(0)
         print(nodoActual, end = " ")
         adyacentes = self.adyacentes(nodoActual)
         for a, p in adyacentes:
            if a in self.__visitados:
               continue
            cola.append(a)
            self.__visitados.add(a)

   def recorridoProfundidad(self, nodoInicio):
      self.__visitados.clear()
      self.DSF(nodoActual=nodoInicio, nodoFin=None, printear=True)