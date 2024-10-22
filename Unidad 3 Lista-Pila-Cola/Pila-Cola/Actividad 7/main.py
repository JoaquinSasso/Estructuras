from moduloColaEnlazada import ColaEnlazada
import random

def randomNum():
   random.seed(None)
   numero = random.random()
   return numero

class cliente:
   def __init__(self, demora, tiempoInicio):
      self.demora = demora
      self.tiempoInicio = tiempoInicio

class ClaseCajero:
   __ocupado : bool
   __cola : ColaEnlazada
   
   def __init__(self):
      self.__ocupado = False
      self.__cola = ColaEnlazada()
   
   def ocupado(self):
      return self.__ocupado
   
   def cantidadClientes(self):
      return self.__cola.cantidadElementos()
   
   def insertar(self, cliente):
      self.__cola.insertar(cliente)
   
   def eliminar(self):
      cliente = self.__cola.eliminar()
      return cliente
   
   def cambiarOcupado(self):
      if self.__ocupado == False:
         self.__ocupado = True
      else:
         self.__ocupado = False

def elegirCajero(cliente, cajeros):
   totalLibres = 0
   for cajero in cajeros:
      if cajero.ocupado() == False:
         totalLibres += 1
   if totalLibres == 3:
      numero = int(randomNum() * 2)
      cajeros[numero].insertar(cliente)
   else:
      minimo = cajeros[0].cantidadClientes()
      minimoCajero = 0
      for i in range(3):
         if minimo > cajeros[i].cantidadClientes():
            minimo = cajeros[i].cantidadClientes()
            minimoCajero = i
      cajeros[minimoCajero].insertar(cliente)
   
def actualizarCajero(cajero, tiempoAtencion, reloj):
   clienteActual : cliente =cajero.eliminar()
   termino = 0
   tiempoRespuesta = 0
   if clienteActual != None:
      posibilidad = 1 / tiempoAtencion
      numeroAleatorio = randomNum()
      if numeroAleatorio < posibilidad:
         termino = 1
         tiempoRespuesta = reloj - clienteActual.tiempoInicio
      else:
         cajero.insertar(clienteActual)
   return termino, tiempoRespuesta
      
      
def main():
   cajero1 = ClaseCajero()
   cajero2 = ClaseCajero()
   cajero3 = ClaseCajero()   
   cajeros = [cajero1, cajero2, cajero3]
   tms = 120
   frecuencia = 2
   posibilidad = 1 / frecuencia
   reloj = 0
   cantidadClientesAtendidos = 0
   cantidadTotalClientes = 0
   tiempoResuestaClientesAtendidos = 0
   tiempoMaximoEspera = 0
   while reloj <= tms:
      numeroAleatorio = randomNum()
      if numeroAleatorio < posibilidad:
         demoraTarea = int(randomNum() * 10)
         nuevoCliente = cliente(demoraTarea, reloj)
         elegirCajero(nuevoCliente, cajeros)
         cantidadTotalClientes += 1
      atendido, tiempo = actualizarCajero(cajero1, 5, reloj)
      if atendido == 1:
         cantidadClientesAtendidos += 1
         tiempoResuestaClientesAtendidos += tiempo
         if tiempo > tiempoMaximoEspera:
            tiempoMaximoEspera = tiempo
      atendido, tiempo = actualizarCajero(cajero2, 3, reloj)
      if atendido == 1:
         cantidadClientesAtendidos += 1
         tiempoResuestaClientesAtendidos += tiempo
         if tiempo > tiempoMaximoEspera:
            tiempoMaximoEspera = tiempo
      atendido, tiempo = actualizarCajero(cajero3, 4, reloj)
      if atendido == 1:
         cantidadClientesAtendidos += 1
         tiempoResuestaClientesAtendidos += tiempo
         if tiempo > tiempoMaximoEspera:
            tiempoMaximoEspera = tiempo
      reloj += 1
   cantidadClientesNoAtendidos = 0
   tiempoRespuestaClientesNoAtendidos = 0
   for cajero in cajeros:
      cantidadClientesNoAtendidos += cajero.cantidadClientes()
      clienteActual : cliente =cajero.eliminar()
      while clienteActual != None:
         cantidadClientesNoAtendidos += 1
         tiempoRespuestaClientesNoAtendidos += tms - clienteActual.tiempoInicio
         clienteActual = cajero.eliminar()
   
   print("Cantidad de clientes atendidos: ", cantidadClientesAtendidos)
   print("Tiempo de respuesta media de los clientes atendidos: ", tiempoResuestaClientesAtendidos / cantidadClientesAtendidos)
   print("Tiempo máximo de espera de los clientes atendidos: ", tiempoMaximoEspera)
   print("Cantidad de clientes no atendidos: ", cantidadClientesNoAtendidos)
   print("Tiempo de respuesta media de los clientes no atendidos: ", tiempoRespuestaClientesNoAtendidos / cantidadClientesNoAtendidos)

if __name__ == "__main__":
   main()