from moduloColaEnlazada import ColaEnlazada

def main():
   ts = 300
   reloj = 0
   fr = 0.1
   cola = ColaEnlazada()
   contadorLlegada = 0
   tiempoAtencion = 0
   
   while reloj != ts:
      contadorLlegada += fr
      if contadorLlegada >= 1:
         cola.insertar(reloj)
         contadorLlegada = 0
      if cola.vacia() != True:
         tiempoAtencion += 1
      if tiempoAtencion == 15:
         cola.suprimir()
         tiempoAtencion = 0
      reloj += 1
      
   print(f"El maximo tiempo de espera es: {reloj - cola.suprimir()}")

if __name__ == "__main__":
   main()
      