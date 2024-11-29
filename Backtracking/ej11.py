def sumatorias_n(lista, n):
    resultado = []
    sumatorias_bt(lista, n, resultado, [], 0)
    return resultado

def sumatorias_bt(lista, n, resultado, subconjunto_actual, indice):
    if sum(subconjunto_actual) == n:
        resultado.append(list(subconjunto_actual))
        return
    if sum(subconjunto_actual) > n or indice >= len(lista):
        return
    subconjunto_actual.append(lista[indice])
    sumatorias_bt(lista, n, resultado, subconjunto_actual, indice + 1)

    subconjunto_actual.pop()
    sumatorias_bt(lista, n, resultado, subconjunto_actual, indice + 1)