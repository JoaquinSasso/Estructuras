from graphviz import Digraph
class Arbol:
   __dato : object
   __izquierda : object
   __derecha : object
   
   def __init__(self, dato) -> None:
      self.__dato = dato
      self.__izquierda : Arbol = None
      self.__derecha : Arbol = None
   
   def getIzquierda(self):
      return self.__izquierda
   
   def getDerecha(self):
      return self.__derecha
   
   def getDato(self):
      return self.__dato
   
   def setDerecha(self, nodo):
      self.__derecha = nodo
      
   def setIzquierda(self, nodo):
      self.__izquierda = nodo
   
   def insertar(self, dato):
      if dato < self.__dato:
         if self.__izquierda == None:
            self.__izquierda = Arbol(dato)
         else:   
            self.__izquierda.insertar(dato)
      elif dato > self.__dato:
         if self.__derecha == None:
            self.__derecha = Arbol(dato)
         else:   
            self.__derecha.insertar(dato)
      else:
         print("El dato ya existe en el arbol")
   
   def grado(self, dato): #Operacion recursiva para calcular el grado de
      if dato == self.__dato:
         if self.__izquierda == None and  self.__derecha == None:
            return 0
         if self.__izquierda != None and self.__derecha != None:
            return 2
         else:
            return 1
      if dato < self.__dato:
         return self.__izquierda.grado(dato)
      else:
         return self.__derecha.grado(dato)
      
   
   def calcularDecendientes(self, dato): #Operacion recursiva que retorna la cantidad de descendientes de un nodo Parte 1
      if dato == self.__dato:
         return self.cantidadDecendientes() #Cuando se encuentra el nodo al cual se desea calcular los descendientes se invoca la parte 2
      elif dato < self.__dato and self.__izquierda != None:
         return self.__izquierda.buscar(dato)
      elif dato > self.__dato and self.__derecha != None:
         return self.__derecha.buscar(dato)
      return None
  
  
   def cantidadDecendientes(self): #Operacion recursiva que retorna la cantidad de descendientes de un nodo Parte 2
      if self.__izquierda == None and self.__derecha == None:
         return 0
      elif self.__izquierda == None and self.__derecha != None:
         return 1 + self.__derecha.cantidadDecendientes()
      elif self.__derecha == None:
         return 1 + self.__izquierda.cantidadDecendientes()
      else:
         return 2 + self.__izquierda.cantidadDecendientes() + self.__derecha.cantidadDecendientes()
      
   def nodosHojas(self): #Operacion recursiva que imprime todas las hojas (Inorden)
      if self.__izquierda != None:
         self.__izquierda.nodosHojas()
      if self.__izquierda == None and self.__derecha == None:
         print(self.__dato)
      if self.__derecha != None:
         self.__derecha.nodosHojas()
   
   
   def profundidad(self, dato): #NO ESTABA EN EL PARCIAL
      if dato == self.__dato:
         return 0
      elif dato < self.__dato and self.__izquierda != None:
         return 1 + self.__izquierda.profundidad(dato)
      elif dato > self.__dato and self.__derecha != None:
         return 1 + self.__derecha.profundidad(dato)
      return None
   
   
   def visualizar(self, nombre): #ES PARA CREAR UN GRAFICO DEL ARBOL
        dot = Digraph() # crea el objeto
        self.__visualizar(dot, self) # llama la funcion recursiva
        filename = f'{nombre}' # crea un nombre unico para cada imagen
        dot.render(filename, format='png', cleanup=True)  # Guarda el gráfico como '{nombre}.png'
       

   def __visualizar(self, dot, nodo): #ES PARA CREAR UN GRAFICO DEL ARBOL
      if nodo is not None:
         label = f'{nodo.getDato()}' # crea el string para el nodo
         # dot.node(str(nodo.getDato()), str(nodo.getDato()), shape='circle')
         dot.node(str(nodo.getDato()), label, shape='circle') # crea el nodo con su ID y etiqueta
         if nodo.getIzquierda() is not None:
               dot.edge(str(nodo.getDato()), str(nodo.getIzquierda().getDato()))
               self.__visualizar(dot, nodo.getIzquierda())
         if nodo.getDerecha() is not None:
               dot.edge(str(nodo.getDato()), str(nodo.getDerecha().getDato()))
               self.__visualizar(dot, nodo.getDerecha())
   
   
   def buscarMayor(self, anterior): #NO ESTABA EN EL PARCIAL
      if self.__derecha != None:
         return self.__derecha.buscarMayor(self)
      elif self.__izquierda != None:
         anterior.setDerecha(self.__izquierda)
      else:
         anterior.setDerecha(None)
      return self.__dato
   
   def suprimir(self, dato, anterior = None): #NO ESTABA EN EL PARCIAL
      if dato == self.__dato:
         if self.__izquierda == None and self.__derecha == None:
            if anterior.getIzquierda() == self:
               anterior.setIzquierda(None)
            else:
               anterior.setDerecha(None)
         elif self.__izquierda.grado(self.__izquierda.getDato()) != 0:
            datoAuxiliar = self.__izquierda.buscarMayor(self)
            self.__dato = datoAuxiliar
         else:
            self.__dato = self.__izquierda.getDato()
            self.__izquierda = None
      elif dato < self.__dato and self.__izquierda != None:
         return self.__izquierda.suprimir(dato, self)
      elif dato > self.__dato and self.__derecha != None:
         return self.__derecha.suprimir(dato, self)
      return None
   
   