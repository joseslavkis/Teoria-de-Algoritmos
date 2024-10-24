def max_crossing_subarray(arr, inicio, medio, fin):
    suma_izquierda = float('-inf')
    suma_temp = 0
    max_izquierda = medio
    
    for i in range(medio, inicio - 1, -1):
        suma_temp += arr[i]
        if suma_temp > suma_izquierda:
            suma_izquierda = suma_temp
            max_izquierda = i

    suma_derecha = float('-inf')
    suma_temp = 0
    max_derecha = medio + 1
    
    for i in range(medio + 1, fin + 1):
        suma_temp += arr[i]
        if suma_temp > suma_derecha:
            suma_derecha = suma_temp
            max_derecha = i
    
    return suma_izquierda + suma_derecha, max_izquierda, max_derecha

def max_subarray_rec(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio], inicio, inicio

    medio = (inicio + fin) // 2

    suma_izquierda, left_start, left_end = max_subarray_rec(arr, inicio, medio)
    suma_derecha, right_start, right_end = max_subarray_rec(arr, medio + 1, fin)
    suma_cruzada, cross_start, cross_end = max_crossing_subarray(arr, inicio, medio, fin)

    if suma_izquierda >= suma_derecha and suma_izquierda >= suma_cruzada:
        return suma_izquierda, left_start, left_end
    elif suma_derecha >= suma_izquierda and suma_derecha >= suma_cruzada:
        return suma_derecha, right_start, right_end
    else:
        return suma_cruzada, cross_start, cross_end

def max_subarray(arr):
    if len(arr) == 0:
        return []
    
    _, inicio, fin = max_subarray_rec(arr, 0, len(arr) - 1)
    return arr[inicio:fin + 1]