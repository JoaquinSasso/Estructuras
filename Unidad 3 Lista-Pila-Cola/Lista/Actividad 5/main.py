from moduloListaEnlazadaOrdenada import ListaEnlazada
from moduloTermino import Termino

def sumarPolinomios(polinomio1 : ListaEnlazada, polinomio2 : ListaEnlazada) -> ListaEnlazada:
   i = 1
   j = 1
   polinomioResultado = ListaEnlazada()
   
   while i <= polinomio1.getCantidad() and j <= polinomio2.getCantidad():
      termino1 = polinomio1.recuperar(i)
      termino2 = polinomio2.recuperar(j)
      
      if termino1 == termino2:
         polinomioResultado.insertar(Termino(termino1.getCoeficiente() + termino2.getCoeficiente(), termino1.getGrado()))
         i += 1
         j += 1
      elif termino1 > termino2:
         polinomioResultado.insertar(termino1)
         i += 1
      else:
         polinomioResultado.insertar(termino2)
         j += 1
   while i <= polinomio1.getCantidad():
      polinomioResultado.insertar(polinomio1.recuperar(i))
      i += 1
   while j <= polinomio2.getCantidad():
      polinomioResultado.insertar(polinomio2.recuperar(j))
      j += 1
   return polinomioResultado

def agruparTerminos(polinomio : ListaEnlazada) -> ListaEnlazada:
   i = 1
   polinomioResultado = ListaEnlazada()
   while i < polinomio.getCantidad():
      gradoActual = polinomio.recuperar(i).getGrado()
      sumador = polinomio.recuperar(i).getCoeficiente()
      i += 1
      while gradoActual == polinomio.recuperar(i).getGrado():
         sumador += polinomio.recuperar(i).getCoeficiente()
         i += 1
      polinomioResultado.insertar(Termino(sumador, gradoActual))
   if polinomio.recuperar(i).getGrado() != polinomio.recuperar(i-1).getGrado():
      polinomioResultado.insertar(Termino(polinomio.recuperar(i).getCoeficiente(), polinomio.recuperar(i).getGrado()))
   return polinomioResultado
         
def productoPolinomios(polinomio1 : ListaEnlazada, polinomio2 : ListaEnlazada) -> ListaEnlazada:
   polinomioParcial = ListaEnlazada()
   i = 0
   while i <= polinomio1.getCantidad():
      j = 0
      while j <= polinomio2.getCantidad():
         termino1 = polinomio1.recuperar(i)
         termino2 = polinomio2.recuperar(j)
         polinomioParcial.insertar(Termino(termino1.getCoeficiente() * termino2.getCoeficiente(), termino1.getGrado() + termino2.getGrado()))
         j += 1
      i += 1
      
   polinomioResultado = agruparTerminos(polinomioParcial)
   return polinomioResultado

def divisionPolinomios(polinomio1 : ListaEnlazada, polinomio2 : ListaEnlazada) -> ListaEnlazada:
   polinomioParcial = ListaEnlazada()
   i = 1
   while i <= polinomio1.getCantidad():
      termino1 = polinomio1.recuperar(i)
      j = 1
      while j <= polinomio2.getCantidad():
         termino2 = polinomio2.recuperar(j)
         polinomioParcial.insertar(Termino(termino1.getCoeficiente() / termino2.getCoeficiente(), termino1.getGrado() - termino2.getGrado()))
         j += 1
      i += 1
   polinomioResultado = agruparTerminos(polinomioParcial)
   return polinomioResultado
   
def restaPolinomios(polinomio1 : ListaEnlazada, polinomio2 : ListaEnlazada) -> ListaEnlazada:
   i = 1
   j = 1
   polinomioResultado = ListaEnlazada()
   
   while i <= polinomio1.getCantidad() and j <= polinomio2.getCantidad():
      termino1 = polinomio1.recuperar(i)
      termino2 = polinomio2.recuperar(j)
      
      if termino1 == termino2:
         polinomioResultado.insertar(Termino(termino1.getCoeficiente() - termino2.getCoeficiente(), termino1.getGrado()))
         i += 1
         j += 1
      elif termino1 > termino2:
         polinomioResultado.insertar(termino1)
         i += 1
      else:
         polinomioResultado.insertar(termino2)
         j += 1
   while i <= polinomio1.getCantidad():
      polinomioResultado.insertar(polinomio1.recuperar(i))
      i += 1
   while j <= polinomio2.getCantidad():
      polinomioResultado.insertar(polinomio2.recuperar(j))
      j += 1
   return polinomioResultado
         

def main():
   polinomio1 = ListaEnlazada()
   polinomio2 = ListaEnlazada()
   
   #Termino(coeficiente, grado)
   
   polinomio1.insertar(Termino(3, 2))
   polinomio1.insertar(Termino(4, 1))
   polinomio1.insertar(Termino(2, 0))
   
   polinomio2.insertar(Termino(5, 4))
   polinomio2.insertar(Termino(2, 3))
   polinomio2.insertar(Termino(1, 2))
   polinomio2.insertar(Termino(3, 0))
   
   polinomioSuma = sumarPolinomios(polinomio1, polinomio2)
   polinomioProducto = productoPolinomios(polinomio1, polinomio2)
   polinomioDivision = divisionPolinomios(polinomio1, polinomio2)
   polinomioResra = restaPolinomios(polinomio1, polinomio2)
   
   print("La suma de los polinomios da como resultado")
   for termino in polinomioSuma:
      print(termino, end=" + ")
   print("\n")
   print("El producto de los polinomios da como resultado")
   for termino in polinomioProducto:
      print(termino, end=" + ")
   print("\n")
   print("La division de los polinomios da como resultado")
   for termino in polinomioDivision:
      print(termino, end=" + ")
   print("\n")
   print("La resta de los polinomios da como resultado")
   for termino in polinomioResra:
      print(termino, end=" + ")
   
if __name__ == "__main__":
   main()