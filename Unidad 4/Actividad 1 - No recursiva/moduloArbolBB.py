from moduloNodoArbol import NodoArbol

class ArbolBinarioBusqueda:
   __raiz : NodoArbol
   __altura : int

   def __init__(self):
      self.__raiz = None
      self.__altura = 0
   
   
   def insertar(self, dato, actual: NodoArbol, nivel = 1) -> None:
      if self.__raiz == None:
         self.__raiz = NodoArbol(dato)
         self.__altura = 1
      elif dato < actual.getDato():
         if actual.getIzquierda() == None:
            actual.setIzquierda(NodoArbol(dato))
            if nivel + 1 > self.__altura:
               self.__altura = nivel
         else:
            self.insertar(dato, actual.getIzquierda(), nivel +1)
      elif dato > actual.getDato():
         if actual.getDerecha() == None:
            actual.setDerecha(NodoArbol(dato))
            if nivel > self.__altura:
               self.__altura = nivel
         else:
            self.insertar(dato, actual.getDerecha(), nivel+1)
      else:
         print("La clave ya esta en el árbol") 
   
   
   def suprimir(self, dato) -> None:
      objetivo = self.buscar(dato)
      if objetivo == None:
         print("Dato no encontrado")
      else:
         actual = objetivo.getIzquierda()
         anterior = objetivo
         while actual.getDerecha() != None:
            anterior = actual
            actual = actual.getDerecha()
         anterior.setDerecha(actual.getIzquierda())
         objetivo.setDato(actual.getDato())

      
   def buscar(self, dato, actual = None) -> NodoArbol:
      if self.__raiz == None:
         print("Árbol vacío")
      else:
         if actual == None:
            actual = self.__raiz
         if dato == actual.getDato():
            return actual
         elif dato < actual.getDato():
            if actual.getIzquierda() == None:
               return None
            else:
               return self.buscar(dato, actual.getIzquierda())
         elif dato > actual.getDato():
            if actual.getDerecha() == None:
               return None
            else:
               return self.buscar(dato, actual.getDerecha())
   
   def vacio(self) -> bool:
      return self.__raiz == None
   
   def raiz(self) -> NodoArbol:
      return self.__raiz
   
   def nivel(self, dato) -> int:
      if self.__raiz == None:
         print("Árbol vacío")
      else:
         actual = self.__raiz
         nivel = 1
         while actual.getDato() != dato or actual == None:
            if dato < actual.getDato():
               actual = actual.getIzquierda()
               nivel += 1
            else:
               actual = actual.getDerecha()
               nivel += 1
         if actual == None:
            print("Dato no encontrado")
            return -1
         else:
            return nivel
   
   def hoja(self, dato) -> bool:
      if self.__raiz == None:
         print("Árbol vacío")
      else:
         nodo = self.buscar(dato)
         if nodo == None:
            print("Dato no encontrado")
         else:
            return nodo.getIzquierda() == None and nodo.getDerecha() == None
   
   def hijo(self, hijo, padre) -> bool:
      if self.__raiz == None:
         print("Árbol vacío")
      else:
         nodoHijo = self.buscar(hijo)
         nodoPadre = self.buscar(padre)
         if nodoHijo == None or nodoPadre == None:
            print("Dato no encontrado")
         else:
            return nodoPadre.getIzquierda() == nodoHijo or nodoPadre.getDerecha() == nodoHijo
   
   def padre(self, hijo, padre) -> bool:
      return self.hijo(hijo, padre)
   
   def camino(self, partida, fin) -> list:
      if self.__raiz == None:
         print("Árbol vacío")
      else:
         actual = self.buscar(partida)
         camino = []
         if actual == None:
            print("Dato no encontrado")
            return []
         else:
            while actual.getDato() != fin or actual == None:
               camino.append(actual.getDato())
               if fin < actual.getDato():
                  actual = actual.getIzquierda()
               else:
                  actual = actual.getDerecha()
            if actual == None:
               print("Dato no encontrado")
               return []
            else:
               camino.append(actual.getDato())
               return camino
   
   def altura(self) -> int:
      return self.__altura
   
   def inOrden(self, actual) -> None:
      if actual != None:
         self.inOrden(actual.getIzquierda())
         print(actual.getDato(), end=", ")
         self.inOrden(actual.getDerecha())
   
   def preOrden(self, actual) -> None:
      if actual != None:
         print(actual.getDato(), end=", ")
         self.preOrden(actual.getIzquierda())
         self.preOrden(actual.getDerecha())
      
   def postOrden(self, actual) -> None:
      if actual != None:
         self.postOrden(actual.getIzquierda())
         self.postOrden(actual.getDerecha())
         print(actual.getDato(), end=", ")