'''
(★) El problema del Vertex Cover se define como: dado un grafo no dirigido,
obtener el mínimo subconjunto de vértices del grafo tal que toda arista del grafo
tenga al menos uno de sus vértices perteneciendo al subconjunto.
Dicho conjunto es un Vertex Cover. Definir el problema de decisión del Vertex Cover.
Luego, implementar un verificador polinomial para este problema.
¿Cuál es la complejidad del verificador implementado? Justificar
'''

def vertex_cover_verificador(grafo, VC):
    aristas = set()
    for v in grafo:
        for w in grafo.adyacentes(v):
            aristas.add((v, w))
            aristas.add((w, v))
    for arista in aristas:
        if arista[0] not in VC or arista[1] not in VC:
            return False
    return True

