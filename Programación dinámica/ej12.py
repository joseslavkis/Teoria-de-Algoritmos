# cada campaña publicitaria i de la forma (Gi, Ci)

#opt[n][P] = max(opt[n-1][P], opt[n-1][P-Ci] + Gi)


def carlitos(c_publicitaria, P):
    n = len(c_publicitaria)
    opt = [[0] * (P + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        G_i, C_i = c_publicitaria[i - 1]
        for j in range(P + 1):
            if C_i <= j:
                opt[i][j] = max(opt[i - 1][j], opt[i - 1][j - C_i] + G_i)
            else:
                opt[i][j] = opt[i - 1][j]

    return reconstruir_seleccion(c_publicitaria, opt, P)

def reconstruir_seleccion(c_publicitaria, opt, P):
    resultado = []
    n = len(c_publicitaria)
    j = P
    for i in range(n, 0, -1):
        if opt[i][j] != opt[i - 1][j]:
            resultado.append(c_publicitaria[i-1])
            j -= c_publicitaria[i - 1][1]
    return resultado[::-1]