def cambio(monedas, monto):
    monedas.sort(reverse=True)
    resultado = []

    for m in monedas:
        while monto >= m:
            resultado.append(m)
            monto -= m
    return resultado