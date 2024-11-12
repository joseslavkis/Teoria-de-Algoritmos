# Se tiene una matriz de n × m casilleros, en la cual empezamos en la posición (0, 0) (arriba a la izquierda) y queremos
# llegar a la posición (n − 1, m − 1) (abajo a la derecha), pero solamente nos podemos mover hacia abajo o hacia la
# derecha, y comenzamos con una vida inicial V . Cada casillero puede estar vacío, o tener una trampa. En los casilleros
# que hay trampas se nos reduce la vida en una cantidad Ti conocida (dependiente de cada casillero).
# Diseñar un algoritmo de programación dinámica que dados todos los datos necesarios, permita determinar la cantidad
# de vida máxima con la que podemos llegar a (n − 1, m − 1). Implementar también una forma de poder reconstruir dicho
# camino. Indicar la complejidad del algoritmo propuesto, en tiempo y espacio.


#ec de recurrencia -> opt[i][j] = max(opt[i-1][j], opt[i][j-1]) - T[i][j]
#caso base: opt[0][0] = V - T[0][0]

def vida_maxima(matriz, vida, trampas):
    n = len(matriz)
    m = len(matriz[0])
    opt = [[0 for _ in range(m)] for _ in range(n)]
    opt[0][0] = vida - trampas[0][0]
    #inicializamos la primer fila y la primer columna    
    for j in range(1, m):
        if opt[0][j-1] >= 0:
            opt[0][j] = opt[0][j-1] - trampas[0][j] # puede seguir el camino
        else:
            opt[0][j] = -float('inf') #hardcodeado para que vea el algoritmo que desde aca ni en pedo se puede llegar
    #idem
    for i in range(1, n):
        if opt[i-1][0] >= 0:
            opt[i][0] = opt[i-1][0] - trampas[i][0]
        else:
            opt[i][0] = -float('inf')
    #aplicar la ec de recurrencia para el resto de las celdas
    for i in range(1, n):
        for j in range(1, m):
            vida_arriba = None
            vida_izquierda = None
            if opt[i][j-1] >= 0:
                vida_izquierda = opt[i][j-1] - trampas[i][j]
            else:
                vida_izquierda = -float('inf')

            if opt[i-1][j] >= 0:
                vida_arriba = opt[i-1][j] - trampas[i][j]
            else:
                vida_arriba = -float('inf')

            opt[i][j] = max(vida_arriba, vida_izquierda)

    return opt[n-1][m-1]

def reconstruccion(opt, n, m):
    i, j = n-1, m-1
    camino = [(i, j)]
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if opt[i-1][j] >= opt[i][j-1]:
                i -= 1
            else:
                j -= 1
        elif i > 0:
            i -= 1
        else:
            j -= 1
        camino.append((i, j))
    return camino[::-1]


