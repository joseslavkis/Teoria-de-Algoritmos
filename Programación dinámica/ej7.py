# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    n = len(elementos)
    opt = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        valor, peso = elementos[i-1]
        for j in range(1, W+1):
            if peso <= j:
                opt[i][j] = max(opt[i-1][j], opt[i-1][j - peso] + valor)
            else:
                opt[i][j] = opt[i-1][j]
    return reconstruir_camino(elementos, opt, n, W)


def reconstruir_camino(elementos, opt, n, W):

    resultado = []
    j = W
    for i in range(n, 0, -1):
        if opt[i][j] != opt[i - 1][j]:
            resultado.append(elementos[i - 1])
            j -= elementos[i - 1][1]
    resultado.reverse()
    return resultado