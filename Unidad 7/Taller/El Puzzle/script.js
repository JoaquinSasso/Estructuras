class Nodo {
   constructor(tablero, completitud) {
      this.tablero = tablero;
      this.valor = completitud;
      this.siguiente = [];
      this.numHijos = 0;
   }
   agregarSiguiente(nodo) {
      this.siguiente.push(nodo);
      this.siguiente.sort((a, b) => a.valor - b.valor);
      this.numHijos++;
   }
}

let tablero = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 0],
];
let historial;
let nodoRaiz;
let pasos;

function inicializarVariables() {
   tablero = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 0],
   ];
   historial = [];
   nodoRaiz = new Nodo(tablero, calcularCompletitud(tablero));
}

function resolverPuzzle() {
   inicializarVariables();
   historial.push(nodoRaiz.tablero);
   expandirArbol();
   dibujarTablero();
}


function generarTableroAleatorio() {
	let numeros = [];
	for (let i = 0; i < 9; i++) {
		numeros.push(i); // Llena el array con los números del 0 al 8
	}
	numeros = numeros.sort(() => Math.random() - 0.5); // Desordena el array
	let k = 0;
	for (let i = 0; i < 3; i++) {
		for (let j = 0; j < 3; j++) {
			tablero[i][j] = numeros[k]; // Llena el tablero con los números desordenados
			k++;
		}
	}
	dibujarTablero(); // Llama a la función para dibujar el tablero
}

function dibujarTablero() {
	for (let i = 0; i < 3; i++) {
		for (let j = 0; j < 3; j++) {
			let celda = document.getElementById("c" + (i * 3 + j + 1)); // Obtiene la celda del html
			if (tablero[i][j] == 0) {
            celda.innerHTML = ""; // Limpia la celda
            celda.classList.toggle("empty", true); // Agrega la clase empty
			} else {
            celda.innerHTML = tablero[i][j]; // Muestra el número en la celda
            celda.classList.toggle("empty", false); // Elimina la clase empty
			}
		}
	}
}

function calcularCompletitud(tableroActual) {
   let completitud = 0;
   for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
         if (tableroActual[i][j] == ((j + 1 + (i * 3))) % 9) {
            completitud++;
         }
      }
   }
   return completitud;
}

function buscarVacio(tableroActual) {
   for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
         if (tableroActual[i][j] == 0) {
            return [i, j];
         }
      }
   }
}

function expandirArbol()
{
   let nodoActual = new Nodo(tablero, calcularCompletitud(tablero));
   historial.push(nodoActual.tablero);
   let completitudActual = calcularCompletitud(tablero);
   if (completitudActual == 9) {
      return 1;
   }
   vacio = buscarVacio(tablero);
   let i = vacio[0];
   let j = vacio[1];
   if (i < 2) // Movimiento hacia abajo
   {
      let tableroAuxiliar = JSON.parse(JSON.stringify(tablero));
      let aux = tableroAuxiliar[i][j];
      tableroAuxiliar[i][j] = tableroAuxiliar[i + 1][j];
      tableroAuxiliar[i + 1][j] = aux;
      if (!historial.includes(tableroAuxiliar)) {
         nodoActual.agregarSiguiente(new Nodo(tableroAuxiliar, calcularCompletitud(tableroAuxiliar)));
      }
   }
   if (i > 0) // Movimiento hacia arriba
   {
      let tableroAuxiliar = JSON.parse(JSON.stringify(tablero));
      let aux = tableroAuxiliar[i][j];
      tableroAuxiliar[i][j] = tableroAuxiliar[i - 1][j];
      tableroAuxiliar[i - 1][j] = aux;
      if (!historial.includes(tableroAuxiliar)) {
         nodoActual.agregarSiguiente(new Nodo(tableroAuxiliar, calcularCompletitud(tableroAuxiliar)));
      }
   }
   if (j < 2) // Movimiento hacia la derecha
   {
      let tableroAuxiliar = JSON.parse(JSON.stringify(tablero));
      let aux = tableroAuxiliar[i][j];
      tableroAuxiliar[i][j] = tableroAuxiliar[i][j + 1];
      tableroAuxiliar[i][j + 1] = aux;
      if (!historial.includes(tableroAuxiliar)) {
         nodoActual.agregarSiguiente(new Nodo(tableroAuxiliar, calcularCompletitud(tableroAuxiliar)));
      }
   }
   if (j > 0) // Movimiento hacia la izquierda
   {
      let tableroAuxiliar = JSON.parse(JSON.stringify(tablero));
      let aux = tableroAuxiliar[i][j];
      tableroAuxiliar[i][j] = tableroAuxiliar[i][j - 1];
      tableroAuxiliar[i][j - 1] = aux;
      if (!historial.includes(tableroAuxiliar)) {
         nodoActual.agregarSiguiente(new Nodo(tableroAuxiliar, calcularCompletitud(tableroAuxiliar)));
      }
   }
   for (let i = 0; i < nodoActual.numHijos; i++) {
      tablero = nodoActual.siguiente[i].tablero;
      resultado = expandirArbol();
      if (resultado == 1) {
         return;
      }
   }
}
