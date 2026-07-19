# Red de Ciudades - Grafos (Unidad 3, Algoritmos y Estructuras de Datos)

Programa de consola en Python que modela una red de 7 ciudades ecuatorianas
conectadas por carreteras (grafo ponderado no dirigido) y responde preguntas
sobre ella usando BFS y Dijkstra.

## Cómo ejecutar

Requiere Python 3 (sin librerías externas).

```bash
python main.py
```

Se mostrará un menú interactivo con 5 opciones.

## Estructura del proyecto

- `main.py`: punto de entrada, contiene el menú de consola.
- `utilidades.py`: construcción del grafo y funciones de BFS / Dijkstra.

## Qué hace cada requerimiento

- **R1 - Modelado del grafo**: la red se representa como lista de adyacencia
  (diccionario `{ciudad: [(vecina, distancia_km), ...]}`). La opción 1 del
  menú imprime el grafo completo y el grado de cada ciudad (con cuántas
  ciudades conecta directamente).
- **R2 - Recorrido BFS**: la opción 2 pide una ciudad de origen y recorre el
  grafo en anchura, mostrando cuántas escalas hay hasta cada ciudad alcanzable
  y si la red queda completamente conectada o si alguna ciudad queda aislada.
- **R3 - Ruta más barata (Dijkstra)**: la opción 3 usa la función `dijkstra()`
  provista por la cátedra (sin modificar) para calcular la distancia mínima
  en km desde una ciudad de origen hacia todas las demás, e indica cuál es
  la ciudad más cercana y cuál la más lejana.
- **R4 - Comparación e interpretación**: la opción 4 compara, entre dos
  ciudades elegidas por el usuario, la ruta con menos escalas (BFS) frente a
  la ruta de menor distancia (Dijkstra). En la red de ejemplo, para
  Quito -> Cuenca ambas rutas **no coinciden**: BFS toma la carretera directa
  (1 escala, 440 km) mientras que Dijkstra toma Quito -> Ambato -> Riobamba ->
  Cuenca (3 escalas, 380 km), porque BFS solo cuenta tramos y Dijkstra
  minimiza el peso acumulado.

## Complejidades

| Operación                          | Complejidad          |
|-------------------------------------|-----------------------|
| Construcción del grafo (R1)         | O(A)                  |
| Cálculo de grados (R1)              | O(V)                  |
| BFS (R2)                            | O(V + E)              |
| Dijkstra (R3, provisto)             | O((V + E) log V)      |
| Reconstrucción de camino (R4)       | O(V)                  |

V = número de ciudades, E/A = número de carreteras.
