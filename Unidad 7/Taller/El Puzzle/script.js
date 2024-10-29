class Nodo {
	constructor(tablero, profundidad, padre, movimiento) {
		this.tablero = tablero;
		this.profundidad = profundidad;
		this.heuristica = this.calcularHeuristica();
		this.padre = padre;
		this.movimiento = movimiento;
	}

	calcularHeuristica() {
		let correctas = 0;
		const objetivo = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 0],
		];

		for (let i = 0; i < 3; i++) {
			for (let j = 0; j < 3; j++) {
				if (this.tablero[i][j] === objetivo[i][j] && this.tablero[i][j] !== 0) {
					correctas++;
				}
			}
		}
		return 9 - correctas;
	}

   obtenerMovimientos() {
		const movimientos = [];
		const [fila, columna] = this.buscarVacio();

		const direcciones = [
			[fila - 1, columna, "Mover arriba"],
			[fila + 1, columna, "Mover abajo"],
			[fila, columna - 1, "Mover izquierda"],
			[fila, columna + 1, "Mover derecha"],
		];

		for (const [nuevaFila, nuevaColumna, direccion] of direcciones) {
			if (
				nuevaFila >= 0 &&
				nuevaFila < 3 &&
				nuevaColumna >= 0 &&
				nuevaColumna < 3
			) {
				const nuevoTablero = JSON.parse(JSON.stringify(this.tablero));
				const numeroMovido = nuevoTablero[nuevaFila][nuevaColumna];
				[nuevoTablero[fila][columna], nuevoTablero[nuevaFila][nuevaColumna]] = [
					nuevoTablero[nuevaFila][nuevaColumna],
					nuevoTablero[fila][columna],
				];
				const movimiento = `Se movió el ${numeroMovido} a (${fila + 1}, ${
					columna + 1
				})`;
				movimientos.push(
					new Nodo(nuevoTablero, this.profundidad + 1, this, movimiento)
				);
			}
		}

		return movimientos;
	}

	buscarVacio() {
		for (let i = 0; i < 3; i++) {
			for (let j = 0; j < 3; j++) {
				if (this.tablero[i][j] === 0) return [i, j];
			}
		}
	}

	esMeta() {
		const objetivo = [
			[1, 2, 3],
			[4, 5, 6],
			[7, 8, 0],
		];
		return JSON.stringify(this.tablero) === JSON.stringify(objetivo);
	}
}

let cantidadNodos;
let cantidadExpansiones;
let profundidad;

function resolverPuzzle() {
	cantidadExpansiones = 0;
	cantidadNodos = 0;
	const tableroInicial = obtenerTableroActual();
	const nodoInicial = new Nodo(tableroInicial, 0, null, "Estado inicial");
	const colaPrioridad = [nodoInicial];
	historial = [nodoInicial];
	const visitados = new Set();
	visitados.add(JSON.stringify(nodoInicial.tablero));

	while (colaPrioridad.length > 0) {
		cantidadExpansiones++;
		colaPrioridad.sort(
			(a, b) => a.heuristica + a.profundidad - (b.heuristica + b.profundidad)
		);
		const nodoActual = colaPrioridad.shift();

		if (nodoActual.esMeta()) {
			mostrarSolucion(nodoActual);
			profundidad = nodoActual.profundidad;
			return;
		}

		for (const nodoHijo of nodoActual.obtenerMovimientos()) {
			const tableroString = JSON.stringify(nodoHijo.tablero);
			if (!visitados.has(tableroString)) {
				cantidadNodos++;
				visitados.add(tableroString);
				colaPrioridad.push(nodoHijo);
			}
		}
	}

	document.getElementById("movimientos").innerHTML = "No se encontró solución.";
}

function mostrarSolucion(nodo) {
	profundidad = nodo.profundidad;
	const camino = [];
	while (nodo) {
		camino.unshift(nodo);
		nodo = nodo.padre;
	}
	document.getElementById("cantidadNodos").innerHTML = "La cantidad de nodos generados es de: " + cantidadNodos;
	document.getElementById("cantidadExpansiones").innerHTML = "La cantidad de nodos analizados es de: " + cantidadExpansiones;
	document.getElementById("profundidad").innerHTML = "La cantidad de movimientos es de: " + profundidad;
	let i = 0;
	function mostrarPaso() {
		if (i < camino.length) {
			const nodo = camino[i];
			actualizarTableroHTML(nodo.tablero);
			document.getElementById(
				"movimientos"
			).innerHTML += `<p>${nodo.movimiento}</p>`;
			i++;
			setTimeout(mostrarPaso, 500);
		}
	}
	mostrarPaso();
}

function actualizarTableroHTML(tablero) {
	for (let i = 0; i < 3; i++) {
		for (let j = 0; j < 3; j++) {
			const celda = document.getElementById("c" + (i * 3 + j + 1));
			if (tablero[i][j] === 0) {
				celda.innerHTML = "";
				celda.classList.add("empty");
			} else {
				celda.innerHTML = tablero[i][j];
				celda.classList.remove("empty");
			}
		}
	}
}

function obtenerTableroActual() {
	const tablero = [];
	for (let i = 0; i < 3; i++) {
		tablero.push([]);
		for (let j = 0; j < 3; j++) {
			const celda = document.getElementById("c" + (i * 3 + j + 1));
			tablero[i].push(celda.innerHTML ? parseInt(celda.innerHTML) : 0);
		}
	}
	return tablero;
}

function generarTableroAleatorio() {
   document.getElementById("movimientos").innerHTML = "";
	let numeros = Array.from({ length: 9 }, (_, i) => i);
	numeros = numeros.sort(() => Math.random() - 0.5);
	const tablero = [];
	let k = 0;
	for (let i = 0; i < 3; i++) {
		tablero.push([]);
		for (let j = 0; j < 3; j++) {
			tablero[i].push(numeros[k]);
			k++;
		}
   }
   if (!calcularInversiones(tablero)) {
      return generarTableroAleatorio();
   }
	actualizarTableroHTML(tablero);
}

function calcularInversiones(tablero) {
   let inversiones = 0;
   let i = 0;
   let j = 0;
   for (k = 0; k < 9; k++) {
      let maxI = Math.floor(k / 3);
      let maxJ = k % 3;
      if (tablero[maxI][maxJ] === 0) {
         i = maxI;
         j = maxJ;
      }
      for (let l = k + 1; l < 9; l++) {
         let nextI = Math.floor(l / 3);
         let nextJ = l % 3;
         if (tablero[nextI][nextJ] !== 0 && tablero[nextI][nextJ] < tablero[maxI][maxJ]) {
            inversiones++;
         }
      }
   }
   console.log(inversiones);
   return inversiones % 2 === 0;
}