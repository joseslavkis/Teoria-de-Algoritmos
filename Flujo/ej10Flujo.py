# (★★) Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos).
#  Dado un grafo dirigido y dos vértices s y t, encontrar el máximo número de caminos disjuntos s-t en G.
#  Dar una metodología, explicando en detalle cómo se modela el problema,
#  cómo se lo resuelve y cómo se consigue el máximo número de caminos disjuntos.
#  ¿Cuál es el orden temporal de la solución implementada?


from grafo import Grafo
#recibo grafo dirigido pero con pesos desconocidos, los debo inicializar en 1 para que no se repitan caminos
def disjoint_paths(grafo, s, t): 
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grafo.modificar_peso_arista(v, w, 1)
    flujo_maximo, _, _ = grafo.ford_fulkerson(s, t)
    return flujo_maximo


if __name__ == "__main__":
    grafo = Grafo(dirigido=True)
    
    #pesos randoms
    grafo.agregar_arista('s', 'a', 121)
    grafo.agregar_arista('s', 'b', 5)
    grafo.agregar_arista('a', 'c', 121)
    grafo.agregar_arista('b', 'c', 21)
    grafo.agregar_arista('c', 't', 3)
    grafo.agregar_arista("b", "f", 2)
    grafo.agregar_arista("f", "t", 9)
    s = 's'
    t = 't'
    
    max_disjoint_paths = disjoint_paths(grafo, s, t)
    print(f"El número máximo de caminos disjuntos entre {s} y {t} es: {max_disjoint_paths}")

