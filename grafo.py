from collections import deque
import random

class Grafo:
    def __init__(self, dirigido=True):
        self.dirigido = dirigido
        self.vertices = {}
        self.flujo = {}

    def agregar_vertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = {}

    def modificar_peso_arista(self, u, v, nuevo_peso):
        if self.estan_unidos(u, v):
            self.vertices[u][v] = nuevo_peso
            if not self.dirigido:
                self.vertices[v][u] = nuevo_peso
        else:
            raise ValueError(f"No existe una arista entre {u} y {v}")

    def obtener_vertices(self):
        return list(self.vertices.keys())

    def agregar_arista(self, u, v, capacidad):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.vertices[u][v] = capacidad
        self.flujo[(u, v)] = 0
        if not self.dirigido:
            self.vertices[v][u] = capacidad
            self.flujo[(v, u)] = 0

    def estan_unidos(self, u, v):
        return v in self.vertices[u]
    def eliminar_vertice(self, v):
        if v in self.vertices:
            del self.vertices[v]
            for u in self.vertices:
                if v in self.vertices[u]:
                    del self.vertices[u][v]
            return True
        return False
    def adyacentes(self, u):
        return list(self.vertices[u].keys())
    
    def obtener_vertice_aleatorio(self):
        return random.choice(list(self.vertices.keys()))

    def obtener_grados_entrada(self):
        grados = {v: 0 for v in self.vertices}
        for u in self.vertices:
            for v in self.adyacentes(u):
                grados[v] += 1
        return grados

    def obtener_grados_salida(self):
        grados = {v: 0 for v in self.vertices}
        for v in self.vertices:
            grados[v] = len(self.adyacentes(v))
        return grados
    def copiar_grafo(self):
        copia = Grafo(self)
        for u in self.vertices:
            for v in self.vertices[u]:
                copia.agregar_arista(u, v, self.vertices[u][v])
        return copia
    def obtener_grados(self, v):
        return len(self.vertices[v])

    def peso_arista(self, u, v):
        return self.vertices[u][v]

    def bfs(self, fuente, sumidero, parent):
        visitado = {nodo: False for nodo in self.vertices}
        cola = [fuente]
        visitado[fuente] = True

        while cola:
            u = cola.pop(0)
            for v in self.vertices[u]:
                if not visitado[v] and self.vertices[u][v] - self.flujo[(u, v)] > 0:
                    cola.append(v)
                    visitado[v] = True
                    parent[v] = u
                    if v == sumidero:
                        return True
        return False
    
    def es_bipartito(self):
        '''Si no es bipartito devuelve False, si lo es, devuelve los 2 conjuntos de vertices'''
        if not self.vertices:
            return False

        colores = {}
        conjunto1 = set()
        conjunto2 = set()

        for v in self.vertices:
            if v not in colores:
                cola = deque([v])
                colores[v] = 0
                conjunto1.add(v)

                while cola:
                    u = cola.popleft()
                    for w in self.vertices[u]:
                        if w not in colores:
                            colores[w] = 1 - colores[u]
                            if colores[w] == 0:
                                conjunto1.add(w)
                            else:
                                conjunto2.add(w)
                            cola.append(w)
                        elif colores[w] == colores[u]:
                            return False
        return conjunto1, conjunto2

    def ford_fulkerson(self, fuente, sumidero):
        grafo_residual = Grafo(dirigido=self.dirigido)
        for u in self.vertices:
            for v in self.vertices[u]:
                grafo_residual.agregar_arista(u, v, self.vertices[u][v])
                if not grafo_residual.estan_unidos(v, u):
                    grafo_residual.agregar_arista(v, u, 0)
                self.flujo[(v, u)] = 0

        parent = {}
        flujo_maximo = 0

        while grafo_residual.bfs(fuente, sumidero, parent):
            path_flow = float('Inf')
            s = sumidero
            while s != fuente:
                path_flow = min(path_flow, grafo_residual.peso_arista(parent[s], s))
                s = parent[s]

            v = sumidero
            while v != fuente:
                u = parent[v]
                nuevo_peso = grafo_residual.peso_arista(u, v) - path_flow
                grafo_residual.agregar_arista(u, v, nuevo_peso)

                nuevo_peso_inverso = grafo_residual.peso_arista(v, u) + path_flow
                grafo_residual.agregar_arista(v, u, nuevo_peso_inverso)

                self.flujo[(u, v)] += path_flow
                self.flujo[(v, u)] -= path_flow
                
                v = u

            flujo_maximo += path_flow

        flujo_aristas = {(u, v): self.flujo[(u, v)] for u in self.vertices for v in self.vertices[u] if self.flujo[(u, v)] > 0}
        grafo_residual_final = {u: {v: self.vertices[u][v] - self.flujo[(u, v)] for v in self.vertices[u]} for u in self.vertices}

        return flujo_maximo, flujo_aristas, grafo_residual_final
    
    def __len__(self):
        return len(self.vertices)
    
    def __iter__(self):
        return iter(self.vertices)

    def __str__(self):
        result = ""
        for v in self.vertices:
            result += f"{v}: {self.vertices[v]}\n"
        return result.strip()
    