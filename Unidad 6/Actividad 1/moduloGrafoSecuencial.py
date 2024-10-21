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
      if nodoActual == nodoFin:
         return caminoActual
      adyacentes = self.adyacentes(nodoActual)
      if nodoFin in adyacentes :
         caminoActual.append(nodoFin)
         return caminoActual
      else:
         for a in adyacentes:
            if a  in self.__visitados:
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
         if camino != None:
            contador += 1
      return contador == self.__cantNodos
   