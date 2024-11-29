def max_grupos_bodegon(P, W):
    resultado = []
    solucion_optima = []
    backtrack(P, W, 0, 0, [], solucion_optima, resultado)
    return resultado

def backtrack(P, W, index, ocupacion_actual, solucion_parcial, solucion_optima, resultado):
    if ocupacion_actual > W:
        return solucion_optima

    if ocupacion_actual > sum(solucion_optima):
        solucion_optima.clear()
        solucion_optima.extend(solucion_parcial)
        resultado.clear()
        resultado.extend(solucion_optima)
    if index == len(P):
        return solucion_optima

    solucion_parcial.append(P[index])
    solucion_optima = backtrack(P, W, index + 1, ocupacion_actual + P[index], solucion_parcial, solucion_optima, resultado)
    solucion_parcial.pop()

    solucion_optima = backtrack(P, W, index + 1, ocupacion_actual, solucion_parcial, solucion_optima, resultado)

    return solucion_optima