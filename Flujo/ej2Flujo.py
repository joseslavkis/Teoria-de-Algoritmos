from collections import deque, defaultdict

def bfs_camino_aumentante(grafo_residual, fuente, sumidero, padres):
    """
    Realiza una búsqueda BFS en el grafo residual para encontrar un camino aumentante desde
    la fuente al sumidero. Si encuentra un camino, actualiza el diccionario 'padres' y
    devuelve True. Si no, devuelve False.
    """
    visitado = set()
    cola = deque([fuente])
    visitado.add(fuente)

    while cola:
        u = cola.popleft()

        # Recorrer vecinos de u en el grafo residual
        for v in grafo_residual[u]:
            if v not in visitado and grafo_residual[u][v] > 0:  # Capacidad positiva
                padres[v] = u  # Registramos el predecesor de v
                if v == sumidero:
                    return True
                cola.append(v)
                visitado.add(v)
    
    return False

def ford_fulkerson(grafo, fuente, sumidero):
    """
    Implementa el algoritmo de Ford-Fulkerson para encontrar el flujo máximo en un grafo de capacidades.
    - 'grafo' es un diccionario que representa el grafo original con capacidades.
    - 'fuente' es el nodo fuente.
    - 'sumidero' es el nodo sumidero.
    Devuelve un diccionario con los flujos en cada arista del grafo original.
    """
    # Inicializar el grafo residual como una copia del grafo original (capacidades)
    grafo_residual = defaultdict(lambda: defaultdict(int))
    for u in grafo:
        for v in grafo[u]:
            grafo_residual[u][v] = grafo[u][v]  # Capacidad inicial

    # Inicializar el diccionario de flujo
    flujo = defaultdict(lambda: defaultdict(int))

    padres = {}  # Para guardar el camino aumentante encontrado

    flujo_maximo = 0

    # Mientras exista un camino aumentante en el grafo residual
    while bfs_camino_aumentante(grafo_residual, fuente, sumidero, padres):
        # Encontrar la capacidad mínima del camino (cuello de botella)
        capacidad_bottleneck = float('Inf')
        v = sumidero
        while v != fuente:
            u = padres[v]
            capacidad_bottleneck = min(capacidad_bottleneck, grafo_residual[u][v])
            v = u

        # Actualizar el flujo en el grafo residual y el flujo total
        v = sumidero
        while v != fuente:
            u = padres[v]
            # Restar la capacidad de la arista directa
            actualizar_grafo_residual(grafo_residual, u, v, -capacidad_bottleneck)
            # Sumar capacidad en la arista inversa (residual)
            actualizar_grafo_residual(grafo_residual, v, u, capacidad_bottleneck)

            # Actualizar el flujo (solo para las aristas originales, no las inversas)
            if (u, v) in grafo:  # Si la arista está en el grafo original
                flujo[u][v] += capacidad_bottleneck
            else:  # Si es una arista inversa
                flujo[v][u] -= capacidad_bottleneck

            v = u

        flujo_maximo += capacidad_bottleneck

    return flujo

# Ejemplo de uso:
if __name__ == "__main__":
    # Grafo con capacidades (grafo original)
    grafo = {
        'super_fuente': {'S': 9, 'X': 3},
        'S': {'V': 6, 'U': 3},
        'V': {'T': 3, 'W': 1},
        'W': {'T': 6},
        'U': {'W': 6, 'Z': 3},
        'X': {'Z': 3},
        'Z': {'W': 1, 'U': 1},
    }

    fuente = 'super_fuente'
    sumidero = 'T'

    # Ejecutar el algoritmo de Ford-Fulkerson
    flujo = ford_fulkerson(grafo, fuente, sumidero)

    # Imprimir el flujo en cada arista
    print("Flujos finales en las aristas:")
    for u in grafo:
        for v in grafo[u]:
            if flujo[u][v] > 0:
                print(f"Arista {u} -> {v}: Flujo = {flujo[u][v]}")



def actualizar_grafo_residual(grafo_residual, u, v, valor):
    """
    Actualiza el grafo residual modificando la capacidad de la arista (u, v).
    """
    grafo_residual[u][v] += valor


# Ejemplo de uso:
if __name__ == "__main__":
    # Grafo con capacidades (grafo original)
    grafo = {
        'super_fuente': {'S': 9, 'X': 3},
        'S': {'V': 6, 'U': 3},
        'V': {'T': 3, 'W': 1},
        'W': {'T': 6},
        'U': {'W': 6, 'Z': 3},
        'X': {'Z': 3},
        'Z': {'W': 1, 'U': 1},
    }

    fuente = 'super_fuente'
    sumidero = 'T'

    # Ejecutar el algoritmo de Ford-Fulkerson
    flujo = ford_fulkerson(grafo, fuente, sumidero)

    # Imprimir el flujo en cada arista
    print("Flujos finales en las aristas:")
    for u in flujo:
        for v in flujo[u]:
            print(f"Arista {u} -> {v}: Flujo = {flujo[u][v]}")
