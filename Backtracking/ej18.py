def contar_ordenamientos(grafo):
    resultado = [0]
    grados_entrada = gr_ent(grafo)
    backtracking(grafo, grados_entrada, resultado, [], set())
    return resultado[0]

def backtracking(grafo, grados_entrada, resultado, solucion_parcial, visitados):
    if len(solucion_parcial) == len(grafo.obtener_vertices()):
        resultado[0] += 1
        return
    for v in grafo.obtener_vertices():
        if grados_entrada[v] == 0 and v not in visitados:
            solucion_parcial.append(v)
            visitados.add(v)
            for w in grafo.adyacentes(v):
                grados_entrada[w] -= 1
            backtracking(grafo, grados_entrada, resultado, solucion_parcial, visitados)
            solucion_parcial.pop()
            visitados.remove(v)
            for w in grafo.adyacentes(v):
                grados_entrada[w] += 1

def gr_ent(grafo):
    vertices = grafo.obtener_vertices()
    grados_entrada = {v: 0 for v in vertices}
    for v in vertices:
        for w in grafo.adyacentes(v):
            grados_entrada[w] += 1
    return grados_entrada