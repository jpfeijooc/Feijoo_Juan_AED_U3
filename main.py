# main.py

from utilidades import (
    construir_grafo,
    calcular_grados,
    bfs_escalas,
    red_completamente_conectada,
    reconstruir_camino_bfs,
    dijkstra,
    ciudad_mas_cercana_lejana,
    reconstruir_camino_dijkstra,
)

def pedir_ciudad(grafo, mensaje):
    while True:
        ciudad = input(mensaje).strip().title()
        if ciudad in grafo:
            return ciudad
        print(f"  '{ciudad}' no existe en la red. Ciudades disponibles: {list(grafo.keys())}")

def opcion_1(grafo):
    print("\n--- Modelado del grafo ---")
    print("Lista de adyacencia (ciudad -> [(vecina, km), ...]):")
    for ciudad, vecinos in grafo.items():
        print(f"  {ciudad}: {vecinos}")

    print("\nGrado de cada ciudad (con cuántas ciudades conecta directamente):")
    grados = calcular_grados(grafo)
    for ciudad, grado in grados.items():
        print(f"  {ciudad}: {grado}")

def opcion_2(grafo):
    print("\n--- Recorrido BFS ---")
    origen = pedir_ciudad(grafo, "Ciudad de origen para el BFS: ")
    escalas, predecesor = bfs_escalas(grafo, origen)

    print(f"\nCiudades alcanzables desde {origen} (con número de escalas):")
    for ciudad, n_escalas in sorted(escalas.items(), key=lambda x: x[1]):
        print(f"  {ciudad}: {n_escalas} escala(s)")

    conectada, aisladas = red_completamente_conectada(grafo, escalas)
    if conectada:
        print("\nLa red está completamente conectada desde este origen.")
    else:
        print(f"\nLa red no está completamente conectada. Ciudad(es) aislada(s): {aisladas}")

def opcion_3(grafo):
    print("\n--- Ruta más barata (Dijkstra) ---")
    origen = pedir_ciudad(grafo, "Ciudad de origen para Dijkstra: ")
    distancias = dijkstra(grafo, origen)

    print(f"\nDistancia mínima en km desde {origen} a cada ciudad:")
    for ciudad, dist in distancias.items():
        print(f"  {ciudad}: {dist} km")

    mas_cercana, mas_lejana = ciudad_mas_cercana_lejana(distancias, origen)
    print(f"\nCiudad más cercana a {origen}: {mas_cercana} ({distancias[mas_cercana]} km)")
    print(f"Ciudad más lejana a {origen}: {mas_lejana} ({distancias[mas_lejana]} km)")

def opcion_4(grafo):
    print("\n--- Comparación e interpretación (BFS vs Dijkstra) ---")
    origen = pedir_ciudad(grafo, "Ciudad de origen: ")
    destino = pedir_ciudad(grafo, "Ciudad de destino: ")

    # Ruta con menos escalas (BFS)
    escalas, predecesor_bfs = bfs_escalas(grafo, origen)
    camino_bfs = reconstruir_camino_bfs(predecesor_bfs, destino)

    # Ruta de menor distancia (Dijkstra)
    distancias = dijkstra(grafo, origen)
    camino_dijkstra = reconstruir_camino_dijkstra(grafo, distancias, origen, destino)

    print(f"\nRuta con menos escalas ({origen} -> {destino}):")
    print(f"  {' -> '.join(camino_bfs)}")
    print(f"  Escalas: {escalas[destino]}")

    print(f"\nRuta con menor distancia en km ({origen} -> {destino}):")
    print(f"  {' -> '.join(camino_dijkstra)}")
    print(f"  Distancia total: {distancias[destino]} km")

    if camino_bfs == camino_dijkstra:
        print("\nAmbas rutas coinciden.")
    else:
        print("\nLas rutas no coinciden: BFS prioriza el menor número de tramos "
              "(sin ver el peso), mientras que Dijkstra prioriza la menor "
              "distancia total, aunque eso implique pasar por más ciudades.")

def menu():
    grafo = construir_grafo()

    opciones = {
        "1": ("Mostrar grafo y grados", lambda: opcion_1(grafo)),
        "2": ("BFS desde una ciudad", lambda: opcion_2(grafo)),
        "3": ("Ruta más barata (Dijkstra)", lambda: opcion_3(grafo)),
        "4": ("Comparar BFS vs Dijkstra entre dos ciudades", lambda: opcion_4(grafo)),
        "5": ("Salir", None),
    }

    while True:
        print("\n===== RED DE CIUDADES - MENÚ =====")
        for clave, (descripcion, _) in opciones.items():
            print(f"  {clave}. {descripcion}")

        eleccion = input("Elija una opción: ").strip()
        if eleccion not in opciones:
            print("Opción inválida, intente de nuevo.")
            continue
        if eleccion == "5":
            print("¡Hasta luego!")
            break

        _, funcion = opciones[eleccion]
        funcion()

if __name__ == "__main__":
    menu()
