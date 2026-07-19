# utilidades.py

from collections import deque
import heapq


# R1 - Modelado del grafo

def construir_grafo():
    """
    Construye la red de ciudades como lista de adyacencia.
        Formato: ciudad - ciudad_vecina, distancia_km
        Grafo no dirigido: cada carretera se agrega en ambos sentidos.
    Complejidad: O(A), donde A es el número de carreteras (aristas).
    """
    grafo = {
        "Quito": [], "Ambato": [], "Riobamba": [], "Cuenca": [], "Guayaquil": [], "Manta": [], "Loja": []
    }

    carreteras = [
        ("Quito", "Ambato", 153),
        ("Quito", "Guayaquil", 432),
        ("Quito", "Cuenca", 463),
        ("Ambato", "Riobamba", 56),
        ("Riobamba", "Cuenca", 266),
        ("Guayaquil", "Cuenca", 196),
        ("Guayaquil", "Manta", 200),
        ("Cuenca", "Loja", 211),
        ("Manta", "Loja", 592),
    ]

    for ciudad_a, ciudad_b, distancia in carreteras:
        grafo[ciudad_a].append((ciudad_b, distancia))
        grafo[ciudad_b].append((ciudad_a, distancia))

    return grafo

def calcular_grados(grafo):
    """
    Devuelve {ciudad: grado}, es decir, con cuántas ciudades conecta directamente cada ciudad.
    Complejidad: O(V), recorre una vez la lista de adyacencia de cada ciudad.
    """
    return {ciudad: len(vecinos) for ciudad, vecinos in grafo.items()}


# R2 - Recorrido del grafo (BFS)

def bfs_escalas(grafo, origen):
    """
    Recorre el grafo en anchura (BFS) desde 'origen'.
    Devuelve:
      - escalas: ciudad: numero_de_escalas_desde_origen
      - predecesor: ciudad: ciudad_anterior_en_el_camino para reconstruir rutas
    Complejidad: O(V + E), cada ciudad y cada carretera se visita una sola vez.
    """
    escalas = {origen: 0}
    predecesor = {origen: None}
    cola = deque([origen])

    while cola:
        actual = cola.popleft()
        for vecino, _distancia in grafo[actual]:
            if vecino not in escalas:
                escalas[vecino] = escalas[actual] + 1
                predecesor[vecino] = actual
                cola.append(vecino)

    return escalas, predecesor

def red_completamente_conectada(grafo, escalas):
    """
    Indica si todas las ciudades del grafo fueron alcanzadas por el BFS.
    Devuelve True, si todas son alcanzables, o False si no.
    Complejidad: O(V).
    """
    aisladas = [ciudad for ciudad in grafo if ciudad not in escalas]
    return (len(aisladas) == 0, aisladas)

def reconstruir_camino_bfs(predecesor, destino):
    """
    Reconstruye el camino (ciudad por ciudad) desde el origen usado en el BFS hasta 'destino', usando el diccionario de predecesores.
    Complejidad: O(V) en el peor caso (largo del camino).
    """
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = predecesor.get(actual)
    camino.reverse()
    return camino


# R3 - Dijkstra (entregado por el profesor)

def dijkstra(grafo, origen):
    """Devuelve {ciudad: distancia_minima_desde_origen}."""
    dist = {ciudad: float('inf') for ciudad in grafo}
    dist[origen] = 0
    heap = [(0, origen)]  # cola de prioridad
    while heap:
        d, u = heapq.heappop(heap)  # el mas cercano pendiente
        if d > dist[u]:
            continue  # ya teniamos una ruta mejor
        for vecino, peso in grafo[u]:
            if dist[u] + peso < dist[vecino]:  # relajacion
                dist[vecino] = dist[u] + peso
                heapq.heappush(heap, (dist[vecino], vecino))
    return dist
    # Complejidad: O((V + E) log V) -> el log V viene de las operaciones
    # de inserción/extracción en la cola de prioridad (heap).

def ciudad_mas_cercana_lejana(distancias, origen):
    """
    A partir del diccionario de distancias que devuelve dijkstra(), determina cuál ciudad (distinta del origen) es la más cercana y cuál la más lejana en kilómetros.
    Complejidad: O(V).
    """
    otras = {c: d for c, d in distancias.items() if c != origen}
    mas_cercana = min(otras, key=otras.get)
    mas_lejana = max(otras, key=otras.get)
    return mas_cercana, mas_lejana

def reconstruir_camino_dijkstra(grafo, distancias, origen, destino):
    """
    Reconstruye la ruta de menor distancia entre 'origen' y 'destino' a partir de las distancias ya calculadas por dijkstra(). No se modifica la función provista: solo usa su resultado (dist).
    Complejidad: O(V) en el peor caso.
    """
    if distancias[destino] == float('inf'):
        return None

    camino = [destino]
    actual = destino
    while actual != origen:
        siguiente = None
        for vecino, peso in grafo[actual]:
            if abs(distancias[vecino] + peso - distancias[actual]) < 1e-9:
                siguiente = vecino
                break
        if siguiente is None:
            return None  # no debería pasar si el grafo es consistente
        camino.append(siguiente)
        actual = siguiente

    camino.reverse()
    return camino
