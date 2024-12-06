'''MAX(opt[n-1][v], opt[n-1][v-vi]+vi)'''

def subset_sum(elementos, v):
    n = len(elementos)
    opt = [[0] * (v + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, v + 1):
            if elementos[i - 1] > j:
                opt[i][j] = opt[i - 1][j]
            else:
                opt[i][j] = max(opt[i - 1][j], opt[i - 1][j - elementos[i - 1]] + elementos[i - 1])

    return reconstruccion(elementos, opt, v, n)

def reconstruccion(elementos, opt, v, n):
    w = v
    resultado = []
    for i in range(n, 0, -1):
        if opt[i][w] != opt[i - 1][w]:
            resultado.append(elementos[i - 1])
            w -= elementos[i - 1]
    return resultado[::-1]