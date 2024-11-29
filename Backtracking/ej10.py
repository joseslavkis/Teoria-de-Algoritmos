def sumatoria_dados(n, s):
    resultado = []
    buscar_combinaciones(n, s, [], resultado)
    return resultado

def buscar_combinaciones(dados_restantes, suma_restante, combinacion_actual, resultado):
    if dados_restantes == 0:
        if suma_restante == 0:
            resultado.append(combinacion_actual[:])
        return

    suma_minima_posible = dados_restantes
    suma_maxima_posible = dados_restantes * 6
    if suma_restante < suma_minima_posible or suma_restante > suma_maxima_posible:
        return

    for i in range(1, 7):
        if suma_restante >= i:
            combinacion_actual.append(i)
            buscar_combinaciones(dados_restantes - 1, suma_restante - i, combinacion_actual, resultado)
            combinacion_actual.pop()