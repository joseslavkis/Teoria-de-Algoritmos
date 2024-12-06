'''
opt[n] = min(optLondres[n], optCalifornia[n])

optLondres[n] = L[n] + min(optLondres[n-1], M + optCalifornia[n-1])
optCalifornia = C[n] + min(optCalifornia[n-1], M + optLondres[n-1])

'''

def plan_operativo(arreglo_L, arreglo_C, costo_M):
    n = len(arreglo_L)
    optLondres = [0] * n
    optCalifornia = [0] * n

    optLondres[0] = arreglo_L[0]
    optCalifornia[0] = arreglo_C[0]
    
    for i in range(1, n):
        optLondres[i] = arreglo_L[i] + min(optLondres[i - 1], costo_M + optCalifornia[i - 1])
        optCalifornia[i] = arreglo_C[i] + min(optCalifornia[i - 1], costo_M + optLondres[i - 1])
    
    return reconstrucción(optCalifornia, optLondres, arreglo_L, arreglo_C)

def reconstrucción(optCalifornia, optLondres, arreglo_L, arreglo_C):
    resultado = []
    n = len(optLondres)
    
    if optLondres[-1] < optCalifornia[-1]:
        ciudad_actual = "londres"
    else:
        ciudad_actual = "california"
    
    resultado.append(ciudad_actual)

    for i in range(n - 1, 0, -1):
        if ciudad_actual == "londres":
            if optLondres[i] - arreglo_L[i] == optLondres[i - 1]:
                ciudad_actual = "londres"
            else:
                ciudad_actual = "california"
        else:
            if optCalifornia[i] - arreglo_C[i] == optCalifornia[i - 1]:
                ciudad_actual = "california"
            else:
                ciudad_actual = "londres"
        resultado.append(ciudad_actual)

    return resultado[::-1]