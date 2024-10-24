from moduloDigrafoSecuencial import digrafoSecuencial

def main():
   g = digrafoSecuencial(6)
   ana = 0
   belen = 1
   cecilia = 2
   daniel = 3
   ezequiel = 4
   federico = 5
   nombres = {0: "Ana", 1: "Belen", 2: "Cecilia", 3: "Daniel", 4: "Ezequiel", 5: "Federico"}
   num = {v: k for k, v in nombres.items()}
   g.agregarArista(ana, belen, 3)
   g.agregarArista(ana, daniel, 6)
   g.agregarArista(belen, cecilia, 1)
   g.agregarArista(belen, ezequiel, 2)
   g.agregarArista(belen, federico, 1)
   g.agregarArista(cecilia, daniel, 2)
   g.agregarArista(daniel, belen, 3)
   g.agregarArista(ezequiel, daniel, 3)
   g.agregarArista(ezequiel, federico, 2)
   g.agregarArista(federico, daniel, 1)
   g.agregarArista(federico, ana, 5)
   print("Bienvenido al sistema de mensajes SMS")
   opcion = 1
   while opcion != 3:
      opcion = int(input("""Menu de opciones:
                      1. Buscar forma mas economica de enviar un mensaje
                      2. Calcular costo de envio mas economico
                      3. Salir
                      Ingrese la opcion deseada: """))
      if opcion == 1:
         origen = input("Ingrese el nombre del remitente: ")
         destino = input("Ingrese el nombre del destinatario: ")
         if origen in num and destino in num:
            pesos, antecesores = g.dijkstra(num[origen])
            camino = g.reconstruirCamino(num[destino], antecesores)
            print(f"El camino mas economico de {origen} a {destino} es: ")
            for nodo in camino:
               print(nombres[nodo], end=" ")
            print()
         else:
            print("Los nombres ingresados no son validos")
      elif opcion == 2:
         origen = input("Ingrese el nombre del remitente: ")
         destino = input("Ingrese el nombre del destinatario: ")
         if origen in num and destino in num:
            pesos, predecesores = g.dijkstra(num[origen])
            print(f"El costo de enviar un mensaje de {origen} a {destino} es de: {pesos[num[destino]]} centavos")
         else:
            print("Los nombres ingresados no son validos")
      elif opcion == 3:
         print("Deteniendo ejecucion")
      else:
         print("Opcion invalida")
         
if __name__ == "__main__":
   main()
    