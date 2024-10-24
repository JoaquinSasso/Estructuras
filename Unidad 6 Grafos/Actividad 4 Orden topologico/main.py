from moduloDigrafoSecuencial import digrafoSecuencial

def ordenTopologico(g, cantNodos):
   grados = [0] * cantNodos
   for i in range(cantNodos):
      grados[i] = g.gradoEntrada(i)
   cola = []
   for i in range(cantNodos):
      if grados[i] == 0:
         cola.append(i)
   orden = []
   while cola:
      nodo = cola.pop(0)
      orden.append(nodo)
      adyacentes, _ = g.adyacentes(nodo)
      for adyacente in adyacentes:
         grados[adyacente] -= 1
         if grados[adyacente] == 0:
            cola.append(adyacente)
   return orden

def main():
   cantNodos = 6
   g = digrafoSecuencial(cantNodos)
   ae2 = 0
   ae3 = 1
   ed1 = 2
   ed2 = 3
   ed3 = 4
   trad_int = 5
   nombres = {0: "ae2", 1: "ae3", 2: "ed1", 3: "ed2", 4: "ed3", 5: "trad_int"}
   g.agregarArista(ae2, ed1, 1)
   g.agregarArista(ed1, ed2, 1)
   g.agregarArista(ed1, ae3, 1)
   g.agregarArista(ed2, ed3, 1)
   g.agregarArista(ed3, trad_int, 1)
   g.agregarArista(ae3, trad_int, 1)
   orden = ordenTopologico(g, cantNodos)
   print("Orden topologico:")
   for nodo in orden:
      print(nombres[nodo], end=" ")
   print()
if __name__ == "__main__":
   main()
