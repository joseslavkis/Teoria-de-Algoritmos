# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    elementos_ordenados = sorted(elementos, key=lambda x: x[0] / x[1], reverse=True)

    capacidad_restante = W
    valor_total = 0
    elementos_elegidos = []

    for valor, peso in elementos_ordenados:
        if peso <= capacidad_restante:
            elementos_elegidos.append((valor, peso))
            valor_total += valor
            capacidad_restante -= peso
    return elementos_elegidos