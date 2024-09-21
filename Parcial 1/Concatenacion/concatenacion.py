from moduloListaEnlazada import ListaEnlazada

def main():
   lista1= ListaEnlazada()
   lista2= ListaEnlazada()
   
   for i in range(0, 3):
      lista1.insertar(i, i)
   for i in range(0, 3):
      lista2.insertar(i, i)
   
   lista3 = lista1
   
   lista3.ultimoElemento().setSiguiente(lista2.primerElemento())
   
   for elemento in lista3:
      print(elemento)
      
if __name__ == "__main__":
   main()