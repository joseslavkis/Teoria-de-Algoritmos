#opt[P][W] = max(opt[P-1][W], opt[P-1][W-P[i]] + P[i])


def bodegon_dinamico(P, W):
    n = len(P)
    opt = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        Pi = P[i-1]
        for j in range(1, W+1):
            if Pi <= j:
                opt[i][j] = max(opt[i-1][j], opt[i-1][j-Pi] + Pi)
            else:
                opt[i][j] = opt[i-1][j]
    return reconstruccion(P, W, opt)


def reconstruccion(P, W, opt):
    j = W
    resultado = []

    for i in range(len(P), 0, -1):
        if opt[i-1][j] != opt[i][j]:
            resultado.append(P[i-1])
            j -= P[i-1]
    return resultado[::-1]