def mas_de_la_mitad(arr):
    if not arr:
        return False

    candidato = elemento_mayoritario_rec(arr, 0, len(arr) - 1)
    conteo = contar_ocurrencias(arr, candidato, 0, len(arr) - 1)
    
    return conteo > len(arr) // 2

def elemento_mayoritario_rec(arr, izquierda, derecha):
    if izquierda == derecha:
        return arr[izquierda]

    medio = (izquierda + derecha) // 2
    mayoritario_izquierda = elemento_mayoritario_rec(arr, izquierda, medio)
    mayoritario_derecha = elemento_mayoritario_rec(arr, medio + 1, derecha)

    if mayoritario_izquierda == mayoritario_derecha:
        return mayoritario_izquierda

    conteo_izquierda = contar_ocurrencias(arr, mayoritario_izquierda, izquierda, derecha)
    conteo_derecha = contar_ocurrencias(arr, mayoritario_derecha, izquierda, derecha)

    if conteo_izquierda > (derecha - izquierda + 1) // 2:
        return mayoritario_izquierda
    elif conteo_derecha > (derecha - izquierda + 1) // 2:
        return mayoritario_derecha
    else:
        return None

def contar_ocurrencias(arr, num, izquierda, derecha):
    conteo = 0
    for i in range(izquierda, derecha + 1):
        if arr[i] == num:
            conteo += 1
    return conteo