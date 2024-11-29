from grafo import Grafo

def hay_isomorfismo(g1, g2):
    if len(g1.obtener_vertices()) != len(g2.obtener_vertices()):
        return False
    vertices_g1 = g1.obtener_vertices()
    vertices_g2 = g2.obtener_vertices()
    mapeo = {}
    visitados = set()

    return backtracking_isomorfismo(g1, g2, vertices_g1, vertices_g2, mapeo, visitados, 0)

def backtracking_isomorfismo(g1, g2, vertices_g1, vertices_g2, mapeo, visitados, index):
    if index == len(vertices_g1):
        return True

    v1 = vertices_g1[index]
    for v2 in vertices_g2:
        if v2 not in visitados:
            mapeo[v1] = v2
            visitados.add(v2)

            if es_valido_isomorfismo(g1, g2, mapeo, v1):
                if backtracking_isomorfismo(g1, g2, vertices_g1, vertices_g2, mapeo, visitados, index + 1):
                    return True
            del mapeo[v1]
            visitados.remove(v2)

    return False

def es_valido_isomorfismo(g1, g2, mapeo, v1):
    v2 = mapeo[v1]
    if len(g1.adyacentes(v1)) != len(g2.adyacentes(v2)):
        return False
    for vecino in g1.adyacentes(v1):
        if vecino in mapeo:
            w2 = mapeo[vecino]
            if not g2.estan_unidos(v2, w2):
                return False
    return True