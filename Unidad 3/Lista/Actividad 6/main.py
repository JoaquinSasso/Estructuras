from moduloListaSecuencial import ListaSecuencial

def inicializarMemoria(memoria : ListaSecuencial) -> None:
   for i in range(0, 10):
      memoria.insertar(10, i)

def pedirMemoria(memoria : ListaSecuencial, cantidad : int) -> None:
   i = 0
   while i < memoria.cantidadElementos() and memoria.recuperar(i) < cantidad:
      i += 1
   if i < memoria.cantidadElementos() and memoria.recuperar(i) >= cantidad:
      cantidadDisponible = memoria.suprimir(i)
      memoria.insertar(cantidadDisponible - cantidad, i)
   else:
      print("No hay memoria disponible")

def liberarMemoria(memoria : ListaSecuencial, cantidad : int) -> None:
   i = 0
   while i < memoria.cantidadElementos() and memoria.recuperar(i) + cantidad > 10:
      i += 1
   if i < memoria.cantidadElementos() and memoria.recuperar(i) + cantidad <= 10:
      cantidadDisponible = memoria.suprimir(i)
      memoria.insertar(cantidadDisponible + cantidad, i)
   else:
      print("No se puede liberar esa cantidad de memoria")

def mostrarMemoria(memoria : ListaSecuencial) -> None:
   for i in range(0, memoria.cantidadElementos()):
      print(f"Memoria {i}: {memoria.recuperar(i)}")

def main():
      memoria = ListaSecuencial(10)
      inicializarMemoria(memoria)
      opcion = 0
      while opcion != -1:
         opcion = int(input("""Menu de opciones:
                            1) Pedir memoria
                            2) Liberar memoria
                            3) Mostrar memoria libre
                            -1) Salir
                            Ingrese una opcion: """))
         if opcion == 1:
            cantidad = int(input("Ingrese la cantidad de memoria a pedir: "))
            pedirMemoria(memoria, cantidad)
         elif opcion == 2:
            cantidad = int(input("Ingrese la cantidad de memoria a liberar: "))
            liberarMemoria(memoria, cantidad)
         elif opcion == 3:
            mostrarMemoria(memoria)
         elif opcion == -1:
            print("Deteniendo ejecucion")

if __name__ == "__main__":
   main()
      
      