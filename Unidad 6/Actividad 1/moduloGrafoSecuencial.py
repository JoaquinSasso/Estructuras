class grafoSecuencial:
   __matriz : list[list[int]]
   __cantNodos : int
   
   def __init__(self, cantNodos: int):
      self.__cantNodos = cantNodos
      self.__matriz = []
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
   
   def camino(self, nodoActual, nodoFin, camino) -> list:
      camino.append(nodoActual)
      if nodoActual == nodoFin:
         return camino
      adyacentes = self.adyacentes(nodoActual)
      if nodoFin in adyacentes:
         camino.append(nodoFin)
         return camino
      else:
         caminoFinal = camino
         for a in adyacentes:
            if a not in camino:
               nuevoCamino = self.camino(a, nodoFin, camino)
               if len(nuevoCamino) < len(caminoFinal):
                  caminoFinal = nuevoCamino
         return caminoFinal

   
   