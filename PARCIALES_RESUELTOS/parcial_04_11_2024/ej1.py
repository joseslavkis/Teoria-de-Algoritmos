# Resolver, utilizando backtracking, el problema de la mochila con cantidades mínimas. Este tiene el mismo planteo al
# original pero además cuenta con un parámetro K, donde además de las condiciones impuestas para el problema original,
# se deben utilizar al menos K elementos. Es decir, el planteo completo es: Dados n elementos de valores v1, v2, ..., vn
# con pesos p1, p2, ..., pn, y valores W y K, encontrar el subconjunto de al menos K elementos, cuya suma de valor sea
# máxima y cuyo peso no exceda el valor de W.


#Doy por echo que las tuplas son (valor, peso)

def mochila(elementos, W, K):
    resultado = []
    bt(elementos, W, K, 0, [], resultado)
    return resultado

def bt(elementos, W, K, i, solucion_parcial, resultado):
    peso_actual = sum(map(lambda x: x[1], solucion_parcial))
    valor_actual = sum(map(lambda x: x[0], solucion_parcial))

    if i == len(elementos):
        if len(solucion_parcial) >= K and peso_actual <= W:
            if sum(map(lambda x: x[0], resultado)) < valor_actual:
                resultado.clear()
                resultado.extend(solucion_parcial)
        return

    if peso_actual > W:
        return

    elem = elementos[i]
    solucion_parcial.append(elem)
    bt(elementos, W, K, i + 1, solucion_parcial, resultado)
    solucion_parcial.pop()
    bt(elementos, W, K, i + 1, solucion_parcial, resultado)
    return

