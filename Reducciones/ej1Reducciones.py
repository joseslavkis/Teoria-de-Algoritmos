'''
(★) El problema del Independent Set se define como: dado un grafo no dirigido,
obtener el máximo subconjunto de vértices del grafo tal que ningun par de vértices del subconjunto sea adyacente entre si.
Dicho conjunto es un Independet Set. Definir el problema de decisión del Independent Set.
Luego, implementar un verificador polinomial para este problema.
¿Cuál es la complejidad del verificador implementado? Justificar
'''
from grafo import Grafo

def independet_set_verificador(grafo, IS):
    for v in IS:
        for w in grafo.adyacentes(v):
            if w in IS:
                return False
    return True

# complejidad = O(D + E) porque recorro todos los vertices y sus adyacentes,
# siendo D la cantidad de vertices de IS y E la suma de las aristas de los vertices de IS 



