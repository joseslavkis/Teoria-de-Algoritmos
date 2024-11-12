"""
(★★) Dado un grafo no dirigido bipartito,
un match es un subconjunto de las aristas en el cual para todo vértice v a lo sumo una arista del match incide en v
(en el match, tienen grado a lo sumo 1). Decimos que el vértice vv está matcheado si hay alguna arista que incida en él
(sino, está unmatcheado).
El matching máximo es aquel en el que tenemos la mayor cantidad de aristas (matcheamos la mayor cantidad posible).
Dar una metodología para encontrar el matching máximo de un grafo,
explicando en detalle cómo se modela el problema, cómo se lo resuelve y cómo se consigue el matching máximo.
¿Cuál es el orden temporal de la solución implementada?
"""
from grafo import Grafo
# O(V*E) EXPLICACION EN CLASE DE 14/10
def perfect_bipartite_matching(grafo):
    resultado = []
    gr_ent = grafo.obtener_grados_entrada()
    gr_sal = grafo.obtener_grados_salida()
    if not grafo.es_bipartito(): return
    conjunto1, conjunto2 = grafo.es_bipartito()
    fuente, sumidero = 'fuente', 'sumidero'
    grafo_dirigido = Grafo(dirigido=True)

    for v in conjunto1:
        for w in conjunto2:
            if grafo.estan_unidos(v, w):
                grafo_dirigido.agregar_arista(v, w, 1)

    grafo_dirigido.agregar_vertice(fuente)
    grafo_dirigido.agregar_vertice(sumidero)
    for v in conjunto1:
        grafo_dirigido.agregar_arista(fuente, v, 1)
    for w in conjunto2:
        grafo_dirigido.agregar_arista(w, sumidero, 1)

    _, flujo_aristas, _ = grafo_dirigido.ford_fulkerson(fuente, sumidero)

    for (v, w) in flujo_aristas:
        if fuente not in (v, w) and sumidero not in (v, w):
            resultado.append((v, w))
    
    return resultado

if __name__ == "__main__":
    grafo = Grafo(dirigido=False)

    vertices_conjunto1 = ['A', 'B', 'C', 'D']
    vertices_conjunto2 = ['1', '2', '3', '4']

    for v in vertices_conjunto1 + vertices_conjunto2:
        grafo.agregar_vertice(v)
    

    for v1 in vertices_conjunto1:
        for v2 in vertices_conjunto2:
            grafo.agregar_arista(v1, v2, 1)

    resultado = perfect_bipartite_matching(grafo)
    print("Matching máximo:", resultado)
