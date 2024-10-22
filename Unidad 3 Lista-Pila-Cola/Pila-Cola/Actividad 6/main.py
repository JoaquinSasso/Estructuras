from moduloColaEnlazada import ColaEnlazada
import random
class Tarea:
   def __init__(self, demora, relojInicio):
      self.restante = demora
      self.tiempoInicio = relojInicio

def randomNum():
   random.seed(None)
   numero = random.random()
   return numero
def nuevaTarea(reloj, posibilidad, cola, cantidadTotalTareas):
   numeroAleatorio = randomNum()
   if numeroAleatorio < posibilidad:
      demoraTarea = random.randint(1,8)
      nuevaTarea = Tarea(demoraTarea, reloj)
      cola.insertar(nuevaTarea)
      cantidadTotalTareas += 1
   return cantidadTotalTareas

def main():
   tms = int(input("Ingrese el tiempo de simulacion: "))
   tiempoMedioEspera = int(input("Ingrese el tiempo medio de espera: "))
   posibilidad = 1/tiempoMedioEspera
   cola = ColaEnlazada()
   reloj = 0
   cantidadTareasResueltas = 0
   cantidadTotalTareas = 0
   tiempoRespuestaTotal = 0
   while reloj <= tms:
      cantidadTotalTareas = nuevaTarea(reloj, posibilidad, cola, cantidadTotalTareas)
      tareaActual : Tarea = cola.eliminar()
      if tareaActual != None:
         tiempoImpresora = 5
         while tareaActual.restante > 0 and tiempoImpresora > 0:
            tiempoImpresora -= 1
            tareaActual.restante -= 1
            cantidadTotalTareas = nuevaTarea(reloj, posibilidad, cola, cantidadTotalTareas)
            reloj += 1
         if tareaActual.restante > 0:
            cola.insertar(tareaActual)
         else:
            tiempoRespuestaTotal += reloj - tareaActual.tiempoInicio
            cantidadTareasResueltas += 1
      else:
         reloj += 1
   print("Cantidad de tareas no resueltas: ", cantidadTotalTareas - cantidadTareasResueltas)
   print("El promdedio de espera de los trabajos es: ", reloj/cantidadTareasResueltas)

if __name__ == "__main__":
   main()
   