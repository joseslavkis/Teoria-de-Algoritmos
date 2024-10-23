# conocidos: lista de pares de invitados que se conocen, cada elemento es un (a,b)
from grafo import Grafo

def obtener_invitados(conocidos):
    grafo1 = Grafo()
    for (a,b) in conocidos:
        if not a in grafo1:
            grafo1.agregar_vertice(a)
        if not b in grafo1:
            grafo1.agregar_vertice(b)
        if not grafo1.estan_unidos(a,b):
            grafo1.agregar_arista(a,b)
    invitados = []
    vertices = grafo1.obtener_vertices()
    cambio = True
    while cambio:
        cambio = False
        for v in vertices:
            if v not in grafo1:
                continue
            if len(grafo1.adyacentes(v)) < 4:
                cambio = True
                for w in grafo1.adyacentes(v):
                    grafo1.borrar_arista(v,w)
                grafo1.borrar_vertice(v)

    for v in grafo1:
        invitados.append(v)
    return invitados