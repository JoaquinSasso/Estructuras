from moduloPilaEnlazada import pilaEnlazada
def main():
   pila = pilaEnlazada()
   numero = int(input("Ingrese un numero: "))
   origial = numero
   if numero == 0:
      print("El factorial de 0 es 1")
   else:
      while numero > 0:
         pila.insertar(numero)
         numero -= 1
      factorial = 1
      while not pila.vacia():
         factorial *= pila.suprimir()
      print(f"El factorial de {origial} es: {factorial}")

if __name__ == "__main__":
   main()