from moduloNodoArbol import NodoArbol
from graphviz import Digraph

class ArbolBinarioBusqueda:
   raiz : NodoArbol

   def __init__(self):
      self.raiz = None
   
   def insertar(self, dato, actual: NodoArbol) -> None:
      if self.raiz == None:
         self.raiz = NodoArbol(dato)
      elif dato < actual.getDato():
         if actual.getIzquierda() == None:
            actual.setIzquierda(NodoArbol(dato))
            #self.calcularBalance(self.raiz)
         else:
            self.insertar(dato, actual.getIzquierda())            
      elif dato > actual.getDato():
         if actual.getDerecha() == None:
            actual.setDerecha(NodoArbol(dato))
            #self.calcularBalance(self.raiz)
         else:
            self.insertar(dato, actual.getDerecha())
      else:
         print("La clave ya esta en el árbol")

   def balancear(self, actual: NodoArbol) -> None:
      balance = actual.getBalance()
      padre = self.padre(actual)
      if padre != None:
         if balance > 1:
            if padre.getBalance() > 0:
               self.rotacionSimpleIzquierda(actual)
            else:
               self.rotacionDobleIzquierda(padre)
         elif balance < -1:
            if padre.getBalance() < 0:
               self.rotacionSimpleDerecha(actual)
            else:
               self.rotacionDobleDerecha(padre)
      else:
         if balance > 1:
            self.rotacionSimpleIzquierda(actual)
         else:
            self.rotacionDobleIzquierda(actual)
            
      
   def rotacionSimpleIzquierda(self, nodo: NodoArbol) -> None:
      if nodo == None:
         nodo = self.raiz
      padre = self.padre(nodo)
      temp = nodo.getDerecha()
      nodo.setDerecha(temp.getIzquierda())
      temp.setIzquierda(nodo)
      nodo.actualizarBalance(0)
      temp.actualizarBalance(0)
      if padre == None:
         self.raiz = temp
      else:
         if padre.getDerecha() == nodo:
            padre.setDerecha(temp)
         else:
            padre.setIzquierda(temp)
   
   def rotacionSimpleDerecha(self, nodo: NodoArbol) -> None:
      if nodo == None:
         nodo = self.raiz
      padre = self.padre(nodo)
      temp = nodo.getIzquierda()
      nodo.setIzquierda(temp.getDerecha())
      temp.setDerecha(nodo)
      nodo.actualizarBalance(0)
      temp.actualizarBalance(0)
      if padre == None:
         self.raiz = temp
      else:
         if padre.getDerecha() == nodo:
            padre.setDerecha(temp)
         else:
            padre.setIzquierda(temp)
   
   def rotacionDobleIzquierda(self, nodo: NodoArbol) -> None:
      self.rotacionSimpleDerecha(nodo.getDerecha())
      self.rotacionSimpleIzquierda(nodo)
   
   def rotacionDobleDerecha(self, nodo: NodoArbol) -> None:
      self.rotacionSimpleIzquierda(nodo.getIzquierda())
      self.rotacionSimpleDerecha(nodo)
   
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
      if self.raiz == None:
         print("Árbol vacío")
      else:
         if actual == None:
            actual = self.raiz
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
      return self.raiz == None
   
   def altura(self, nodo) -> int:
      if nodo == None:
         return 0
      else:
         return 1 + max(self.altura(nodo.getIzquierda()), self.altura(nodo.getDerecha()))
   
   def calcularBalance(self, actual: NodoArbol) -> None:
      if actual != None:
         alturaIzquierda = self.altura(actual.getIzquierda())
         alturaDerecha = self.altura(actual.getDerecha())
         balance = alturaDerecha - alturaIzquierda
         actual.actualizarBalance(balance)
         if balance < -1 or balance > 1:
            self.balancear(actual)
         self.calcularBalance(actual.getIzquierda())
         self.calcularBalance(actual.getDerecha())
   
   def padre(self, hijo) -> NodoArbol:
      actual = self.raiz
      while actual != None:
         if actual.getIzquierda() == hijo or actual.getDerecha() == hijo:
            return actual
         if hijo.getDato() < actual.getDato():
            actual = actual.getIzquierda()
         else:
            actual = actual.getDerecha()
   
   def visualizar(self, nombre):
        dot = Digraph() # crea el objeto
        self.__visualizar(dot, self.raiz) # llama la funcion recursiva
        filename = f'arbol-{nombre}' # crea un nombre unico para cada imagen
        dot.render(filename, format='png', cleanup=True)  # Guarda el gráfico como 'arbol.png'
       

   def __visualizar(self, dot, nodo : NodoArbol):
      if nodo is not None:
         label = f'{nodo.getDato()} B:{nodo.getBalance()}' # crea el string para el nodo
         # dot.node(str(nodo.getDato()), str(nodo.getDato()), shape='circle')
         dot.node(str(nodo.getDato()), label, shape='circle') # crea el nodo con su ID y etiqueta
         if nodo.getIzquierda() is not None:
               dot.edge(str(nodo.getDato()), str(nodo.getIzquierda().getDato()))
               self.__visualizar(dot, nodo.getIzquierda())
         if nodo.getDerecha() is not None:
               dot.edge(str(nodo.getDato()), str(nodo.getDerecha().getDato()))
               self.__visualizar(dot, nodo.getDerecha())
