class Digrafo:
   __matriz : list[list[int]]
   __cantVertices : int
   
   def __init__(self, cantVertices) -> None:
      self.__cantVertices = cantVertices
      self.__matriz = []
      for i in range(cantVertices):
         self.__matriz.append([0] * cantVertices)
   
   def agregarArista(self, vertice1, vertice2, peso):
      self.__matriz[vertice1][vertice2] = peso
   
   def gradoSalida(self, vertice): #Calcula el grado de salida de un vertice
      contador = 0
      for i in range(self.__cantVertices):
         if self.__matriz[vertice][i] != 0:
            contador += 1
      return contador

   def gradoEntrada(self, vertice): #Calcula el grado de entrada de un vertice
      contador = 0
      for i in range(self.__cantVertices):
         if self.__matriz[i][vertice] != 0:
            contador += 1
      return contador

   def esFuente(self, vertice): #Verifica las condiciones necesarias para que un vertice sea fuente
      return self.gradoEntrada(vertice) == 0 and self.gradoSalida(vertice) != 0

   def mostrarFuentes(self): #Mostrar todos los vertices que son fuentes
      for i in range(self.__cantVertices):
         if self.esFuente(i):
            print(f"El vertice {i} es fuente")
   
   #Complejidad de gradoSalida / gradoEntrada cambiando los corchetes
      #contador = 0                             1ut
      # for i in range(self.__cantVertices):    2n + 1ut
      # if self.__matriz[vertice][i] != 0:         2n
      # contador += 1                           n
      # return contador                         1ut
      # Total                                   5n + 3ut : O(n)
   
   #Complejidad de esFuente
      # return self.gradoEntrada(vertice) == 0 and self.gradoSalida(vertice) != 0
      # Es la complejidad de gradoEntrada + gradoSalida + 4ut
      # Las 4 ut son por 3 operaciones y el retorno
      # Operacion auxiliar                      2 * (5n + 3ut) + 4ut
      # Total                                   10n + 10 ut : O(n)
      
   #Complejidad mostrarFuentes
      # for i in range(self.__cantVertices):    2n + 1ut
      #    if self.esFuente(i):                 10n + 11 ut
      #      print(f"El vertice {i} es fuente") 1 ut
      # Total                                   12n + 13ut : O(n)        
   
