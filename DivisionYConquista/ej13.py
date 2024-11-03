def max_subarray(arr):
    return _max_subarray(arr, 0, len(arr) - 1)

def _max_subarray(arr, ini, fin):
    if ini == fin:
        return [arr[ini]]
    medio = (ini + fin) // 2
    max_izq = _max_subarray(arr, ini, medio)
    max_der = _max_subarray(arr, medio + 1, fin)
    max_cross = max_crossing_subarray(arr, ini, medio, fin)
    return max([max_izq, max_der, max_cross], key=lambda x: sum(x))

def max_crossing_subarray(arr, ini, medio, fin):
    max_izq_sum = -float('inf')
    max_izq_i = medio
    suma_actual = 0
    for i in range(medio, ini - 1, -1):
        suma_actual += arr[i]
        if suma_actual > max_izq_sum:
            max_izq_sum = suma_actual
            max_izq_i = i

    max_der_sum = -float('inf')
    max_der_i = medio + 1
    suma_actual = 0
    for i in range(medio + 1, fin + 1):
        suma_actual += arr[i]
        if suma_actual > max_der_sum:
            max_der_sum = suma_actual
            max_der_i = i

    return arr[max_izq_i:max_der_i + 1]
