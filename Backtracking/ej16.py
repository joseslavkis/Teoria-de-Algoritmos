from grafo import Grafo

def pintar_colectivos(colectivos, paradas):
    grafo = Grafo()

    for colectivo in colectivos:
        grafo.agregar_vertice(colectivo)

    for parada in paradas:
        for i in range(len(parada)):
            for j in range(i + 1, len(parada)):
                if parada[i] in colectivos and parada[j] in colectivos:
                    if not grafo.estan_unidos(parada[i], parada[j]):
                        grafo.agregar_arista(parada[i], parada[j])

    color_asignado = {}
    colores_usados = set()

    vertices_ordenados = sorted(grafo.obtener_vertices(), key=lambda v: len(grafo.adyacentes(v)), reverse=True)

    for vertice in vertices_ordenados:
        colores_vecinos = {color_asignado.get(vecino) for vecino in grafo.adyacentes(vertice) if vecino in color_asignado}

        color = 0
        while color in colores_vecinos:
            color += 1

        color_asignado[vertice] = color
        colores_usados.add(color)

    return len(colores_usados)