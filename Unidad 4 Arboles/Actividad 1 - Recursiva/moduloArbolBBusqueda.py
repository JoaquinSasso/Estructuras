# Este codigo esta incompleto y no funciona
class ArbolBinarioBusqueda:
   __dato : object
   __izquierda : object
   __derecha : object
   
   def __init__(self, dato) -> None:
      self.__dato = dato
      self.__izquierda : ArbolBinarioBusqueda = None
      self.__derecha : ArbolBinarioBusqueda = None
   
   def insertar(self, dato):
      if dato < self.__dato:
         if self.__izquierda == None:
            self.__izquierda = ArbolBinarioBusqueda(dato)
         else:   
            self.__izquierda.insertar(dato)
      elif dato > self.__dato:
         if self.__derecha == None:
            self.__derecha = ArbolBinarioBusqueda(dato)
         else:   
            self.__derecha.insertar(dato)
      else:
         print("El dato ya existe en el arbol")
   
#    def suprimir(self, dato, p1 = None, p2 = None, p3 = None):
#       if self.__izquierda == None and self.__derecha == None:
#          return self
#       if p1 == None:
#          if self.__dato == dato:
#             p1 = self
#          elif dato < self.__dato:
#             self.__izquierda.suprimir(dato, p1, self, p3)
#          else:
#             self.__derecha.suprimir(dato, p1, self, p3)
         
   
#    def buscar(self, dato):
#       if dato == self.__dato:
#          return self
#       elif dato < self.__dato:
#          self.__izquierda.buscar(dato)
#       else:
#          self.__derecha.buscar(dato)
   