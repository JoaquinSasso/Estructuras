from moduloNodo import nodo

class ColaEnlazada:
   __cabeza : nodo
   __cantidad : int
   __ultimo :nodo
   
   def __init__(self) -> None:
      self.__cabeza = None
      self.__ultimo = None
      self.__cantidad = 0
      
   
   def insertar(self, dato):
      nuevoNodo = nodo(dato)
      self.__cantidad += 1
      if self.__cabeza == None:
         nuevoNodo.setSiguiente(self.__cabeza)
         self.__cabeza = nuevoNodo
         self.__ultimo = nuevoNodo
      else:
         self.__ultimo.setSiguiente(nuevoNodo)
         self.__ultimo = nuevoNodo

   
   def suprimir(self):
      if  self.__cantidad == 0:
         print("La cola esta vacia")
      else:
         dato = self.__cabeza.getDato()
         self.__cabeza = self.__cabeza.getSiguiente()
         self.__cantidad -= 1
         return dato
   
   def vacia(self):
      return self.__cabeza == None