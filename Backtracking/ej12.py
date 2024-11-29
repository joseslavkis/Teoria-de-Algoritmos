def max_sumatoria_n(lista, n):
    mejor_subconjunto = []
    mejor_suma = [0]
    sumatorias_bt(lista, n, mejor_subconjunto, [], 0, mejor_suma)
    return mejor_subconjunto

def sumatorias_bt(lista, n, mejor_subconjunto, subconjunto_actual, indice, mejor_suma):
    suma_actual = sum(subconjunto_actual)

    if suma_actual == n:
        mejor_subconjunto[:] = subconjunto_actual[:]
        mejor_suma[0] = suma_actual
        return
    
    if suma_actual > mejor_suma[0] and suma_actual <= n:
        mejor_subconjunto[:] = subconjunto_actual[:]
        mejor_suma[0] = suma_actual
    
    if indice >= len(lista):
        return

    subconjunto_actual.append(lista[indice])
    sumatorias_bt(lista, n, mejor_subconjunto, subconjunto_actual, indice + 1, mejor_suma)

    subconjunto_actual.pop()
    sumatorias_bt(lista, n, mejor_subconjunto, subconjunto_actual, indice + 1, mejor_suma)