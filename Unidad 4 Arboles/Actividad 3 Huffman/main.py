from moduloNodoHuffman import NodoHuffman
   

def analizarCadena(cadena: str) -> list:
   lista = []
   while cadena != "":
      letra = cadena[0]
      frecuencia = cadena.count(letra)
      for i in range(len(cadena)):
         cadena = cadena.replace(letra, "", -1)
      lista.append(NodoHuffman(letra, frecuencia))
   return lista

def ordenarLista(lista: list) -> list:
   lista.sort(key = lambda x: x.getFrecuencia())
   return lista

def armarArbol(lista: list) -> NodoHuffman:
   while len(lista) > 1:
      nodo1 = lista.pop(0)
      nodo2 = lista.pop(0)
      frecuencia = nodo1.getFrecuencia() + nodo2.getFrecuencia()
      nodo = NodoHuffman(nodo1.getStr() + nodo2.getStr(), frecuencia)
      nodo.setIzquierda(nodo1)
      nodo.setDerecha(nodo2)
      lista.append(nodo)
      lista = ordenarLista(lista)
   return lista[0]

def codificar(arbol: NodoHuffman, cadena: str) -> str:
   codificacion = ""
   for letra in cadena:
      nodo = arbol
      while nodo.getStr() != letra:
         if letra in nodo.getIzquierda().getStr():
            codificacion += "0"
            nodo = nodo.getIzquierda()
         else:
            codificacion += "1"
            nodo = nodo.getDerecha()
      codificacion += " "
   return codificacion

def main():
   cadena = input("Ingrese la cadena que desee codificicar: ")
   cadena = cadena.lower()
   lista = analizarCadena(cadena)
   lista = ordenarLista(lista)
   print("La frecuencia de cada letra es: ")
   for nodo in lista:
      print(f"Letra: {nodo.getStr()} Frecuencia: {nodo.getFrecuencia()}")
   arbol = armarArbol(lista)
   print("La codificación de la cadena es: ")
   print(codificar(arbol, cadena))
   
if __name__ == "__main__":
   main()