def camino_hamiltoniano(grafo):
    if len(grafo) == 0:
        return []
    visitados = set()
    camino = []
    for v in grafo:
        if camino_hamiltoniano_dfs(grafo, v, visitados, camino):
            return camino
    return []

def camino_hamiltoniano_dfs(grafo, v, visitados, camino):
    visitados.add(v)
    camino.append(v)

    if len(camino) == len(grafo):
        return True

    for w in grafo.adyacentes(v):
        if w not in visitados and camino_hamiltoniano_dfs(grafo, w, visitados, camino):
            return True
    visitados.remove(v)
    camino.pop()
    return False