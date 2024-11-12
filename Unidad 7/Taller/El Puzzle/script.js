const objetivo = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 0],
];
const objetivoHash = objetivo.flat().join(',');

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
			[fila - 1, columna],
			[fila + 1, columna],
			[fila, columna - 1],
			[fila, columna + 1],
		];

		for (const [nuevaFila, nuevaColumna] of direcciones) {
			if (
				nuevaFila >= 0 &&
				nuevaFila < 3 &&
				nuevaColumna >= 0 &&
				nuevaColumna < 3
			) {
				const nuevoTablero = JSON.parse(JSON.stringify(this.tablero)); // Copia el tablero sin referenciarlo
				const numeroMovido = nuevoTablero[nuevaFila][nuevaColumna];
				nuevoTablero[nuevaFila][nuevaColumna] = 0;
				nuevoTablero[fila][columna] = numeroMovido;
				const movimiento = `Se movió el ${numeroMovido} a (${fila + 1}, ${
					columna + 1
                    })`;
                let nuevoNodo = new Nodo(nuevoTablero, this.profundidad + 1, this, movimiento);
                movimientos.push(nuevoNodo);
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
        return hashTablero(this.tablero) === objetivoHash;
    }
}

let cantidadNodos;
let cantidadExpansiones;
let profundidad;
let tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 0]];
let mostrarPasoTimeout;

function hashTablero(tablero) {
    return tablero.flat().join(',');
}

function resolverPuzzle() {
    cantidadExpansiones = 1;
    cantidadNodos = 1;
    const nodoInicial = new Nodo(tablero, 0, null, "Estado inicial");
    const colaPrioridad = [nodoInicial];
    const visitados = new Set();
    
    visitados.add(hashTablero(tablero));
    const tiempoInicio = performance.now();

    while (colaPrioridad.length > 0) {
        cantidadExpansiones++;
        // Encontrar el nodo con la menor heurística + profundidad
        let mejorIndice = 0;
        for (let i = 1; i < colaPrioridad.length; i++) {
            if (colaPrioridad[i].heuristica * 2 + colaPrioridad[i].profundidad < colaPrioridad[mejorIndice].heuristica * 2 + colaPrioridad[mejorIndice].profundidad) {
                mejorIndice = i;
            }
        }
        const nodoActual = colaPrioridad.splice(mejorIndice, 1)[0];

        if (nodoActual.esMeta()) {
            const tiempoFin = performance.now();
            const tiempoTotal = tiempoFin - tiempoInicio;
            mostrarSolucion(nodoActual, tiempoTotal);
            profundidad = nodoActual.profundidad;
            return;
        }

        for (const nodoHijo of nodoActual.obtenerMovimientos()) {
            const tableroHash = hashTablero(nodoHijo.tablero);
            if (!visitados.has(tableroHash)) {
                cantidadNodos++;
                visitados.add(tableroHash);
                colaPrioridad.push(nodoHijo);
            }
        }
    }

    document.getElementById("movimientos").innerHTML = "No se encontró solución.";
}

function mostrarSolucion(nodo, tiempoTotal) {
    profundidad = nodo.profundidad;
    const camino = [];
    while (nodo) {
        camino.unshift(nodo);
        nodo = nodo.padre;
    }
    document.getElementById("cantidadNodos").innerHTML = "La cantidad de nodos generados es de: " + cantidadNodos;
    document.getElementById("cantidadExpansiones").innerHTML = "La cantidad de nodos analizados es de: " + cantidadExpansiones;
    document.getElementById("profundidad").innerHTML = "La cantidad de movimientos es de: " + profundidad;
    document.getElementById("tiempo").innerHTML = "El tiempo total es de: " + (tiempoTotal / 1000).toFixed(2) + " segundos";
    let i = 0;
    function mostrarPaso() {
        if (i < camino.length) {
            const nodo = camino[i];
            actualizarTableroHTML(nodo.tablero);
            document.getElementById(
                "movimientos"
            ).innerHTML += `<p>${nodo.movimiento}</p>`;
            i++;
            mostrarPasoTimeout = setTimeout(mostrarPaso, 500);
        }
    }
    mostrarPaso();
}

function actualizarTableroHTML(tableroActual) {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            const celda = document.getElementById("c" + (i * 3 + j + 1));
            if (tableroActual[i][j] === 0) {
                celda.innerHTML = "";
                celda.classList.add("empty");
            } else {
                celda.innerHTML = tableroActual[i][j];
                celda.classList.remove("empty");
            }
        }
    }
}

function obtenerTableroActual() {
    return JSON.parse(JSON.stringify(tablero));
}

function generarTableroAleatorio() {
    clearTimeout(mostrarPasoTimeout);
    document.getElementById("movimientos").innerHTML = "";
    document.getElementById("cantidadNodos").innerHTML = "La cantidad de nodos generados es de: 0";
    document.getElementById("cantidadExpansiones").innerHTML = "La cantidad de nodos analizados es de: 0";
    document.getElementById("profundidad").innerHTML = "La cantidad de movimientos es de: 0";
    document.getElementById("tiempo").innerHTML = "El tiempo total es de: 0 segundos";
    let i = 0;
    let numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8];
    numeros = numeros.sort(() => Math.random() - 0.5);
    tablero = [];
    let k = 0;
    for (let i = 0; i < 3; i++) {
        tablero.push([]);
        for (let j = 0; j < 3; j++) {
            tablero[i].push(numeros[k]);
            k++;
        }
    }
    if (!calcularInversiones()) {
        return generarTableroAleatorio();
    }
    actualizarTableroHTML(tablero);
}

function calcularInversiones() { //Esta funcion se utiliza para verificar si el tablero generado tiene solucion
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