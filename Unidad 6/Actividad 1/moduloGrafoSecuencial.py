class grafoSecuencial:
   __matriz : list[list[int]]
   __cantNodos : int
   __visitados : list[int]
   
   def __init__(self, cantNodos: int):
      self.__cantNodos = cantNodos
      self.__matriz = []
      self.__visitados = []
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
      self.__visitados.append(nodoActual)
      if nodoActual == nodoFin:
         return caminoActual
      adyacentes = self.adyacentes(nodoActual)
      if nodoFin in adyacentes :
         caminoActual.append(nodoFin)
         return caminoActual
      else:
         caminoFinal = [1] * (self.__cantNodos + 1)
         for a in adyacentes:
            if a not in self.__visitados:
               nuevoCamino = self.camino(a, nodoFin, caminoActual.copy())
               if len(nuevoCamino) < len(caminoFinal):
                  caminoFinal = nuevoCamino
         return caminoFinal

   def hayarCamino(self, nodoInicio, nodoFin) -> list:
      caminoActual = []
      self.__visitados = []
      camino = self.camino(nodoInicio, nodoFin, caminoActual)
      if camino == [1] * (self.__cantNodos + 1):
         camino = []
      return camino
   
   def conexo(self):
      contador = 1
      for i in range(1, self.__cantNodos):
         camino = self.hayarCamino(0, i)
         if camino != []:
            contador += 1
      return contador == self.__cantNodos
   