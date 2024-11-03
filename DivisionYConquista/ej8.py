def contar_inversiones(A, B):
    _, inversiones = _contar_inversiones(B, 0, len(B)-1)
    return inversiones

def _contar_inversiones(arr, ini, fin):
    if ini >= fin:
        return [arr[ini]], 0
    medio = (ini + fin) // 2
    izq, cont_izq = _contar_inversiones(arr, ini, medio)
    der, cont_der = _contar_inversiones(arr, medio+1, fin)
    ordenado, contador = mergear_y_contar(izq, der)
    return ordenado, cont_der + cont_izq + contador

def mergear_y_contar(izq, der):
    ordenado = []
    i, j, contador = 0, 0, 0
    while i < len(izq) and j < len(der):
        izquierdo, derecho = izq[i], der[j]
        if izquierdo <= derecho:
            ordenado.append(izquierdo)
            i += 1
        else:
            ordenado.append(derecho)
            j += 1
            contador += len(izq) - i
    ordenado.extend(izq[i:])
    ordenado.extend(der[j:])
    return ordenado, contador