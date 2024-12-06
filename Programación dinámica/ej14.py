'''opt[i] = max(optCaso1, optCaso2)
-optCaso1 = max(optCaso1[i−1],optCaso1[i−2]+ganancias[i]), i pertenece (0, n-2)
-optCaso2 = max(optCaso2[i−1],optCaso2[i−2]+ganancias[i]), i pertenece (1, n-1)
'''

def lunatico(ganancias):
    n = len(ganancias)

    if n == 0:
        return []
    elif n == 1:
        return [0]

    optCaso1 = calcular_ganancia(ganancias, 0, n - 1)
    optCaso2 = calcular_ganancia(ganancias, 1, n)

    if optCaso1[-1] > optCaso2[-1]:
        casas_a_robar = reconstruir_solucion(optCaso1, 0, n - 1)
    else:
        casas_a_robar = reconstruir_solucion(optCaso2, 1, n)

    return sorted(casas_a_robar)

def calcular_ganancia(ganancias, inicio, fin):
    opt = [0] * (fin - inicio)

    opt[0] = ganancias[inicio]
    if fin - inicio > 1:
        opt[1] = max(ganancias[inicio], ganancias[inicio + 1])

    for i in range(2, fin - inicio):
        opt[i] = max(opt[i - 1], opt[i - 2] + ganancias[inicio + i])

    return opt

def reconstruir_solucion(opt, inicio, fin):
    casas_a_robar = []
    i = len(opt) - 1

    while i >= 0:
        if i == 0 or opt[i] != opt[i - 1]:
            casas_a_robar.append(inicio + i)
            i -= 2
        else:
            i -= 1

    return casas_a_robar