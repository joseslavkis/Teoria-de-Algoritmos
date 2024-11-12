from grafo import Grafo

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    solucion_optima = set(vertices)
    solucion_parcial = set()
    return list(dominating_set_rec(grafo, vertices, 0, solucion_parcial, solucion_optima))

def dominating_set_rec(grafo, vertices, index, solucion_parcial, solucion_optima):
    if len(solucion_parcial) >= len(solucion_optima):
        return solucion_optima

    if index == len(vertices):
        if es_dominating_set(grafo, solucion_parcial):
            if len(solucion_parcial) < len(solucion_optima):
                solucion_optima = set(solucion_parcial)
        return solucion_optima

    solucion_optima = dominating_set_rec(grafo, vertices, index + 1, solucion_parcial, solucion_optima)

    v = vertices[index]
    solucion_parcial.add(v)
    solucion_optima = dominating_set_rec(grafo, vertices, index + 1, solucion_parcial, solucion_optima)
    solucion_parcial.remove(v)

    return solucion_optima

def es_dominating_set(grafo, solucion_parcial):
    for v in grafo.obtener_vertices():
        if v in solucion_parcial:
            continue
        tiene_adyacente = False
        for w in grafo.adyacentes(v):
            if w in solucion_parcial:
                tiene_adyacente = True
                break
        if tiene_adyacente == False:
            return False
    return True


grafo = Grafo(dirigido=False)
grafo.agregar_vertice("H")
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')
grafo.agregar_vertice('F')
grafo.agregar_arista("H", "C", 0)
grafo.agregar_arista('H', 'A', 0)
grafo.agregar_arista('A', 'B', 0)
grafo.agregar_arista('B', 'C', 0)
grafo.agregar_arista('C', 'D', 0)
grafo.agregar_arista('D', 'E', 0)
grafo.agregar_arista('E', 'F', 0)
grafo.agregar_arista('F', 'B', 0)

print(dominating_set_min(grafo))