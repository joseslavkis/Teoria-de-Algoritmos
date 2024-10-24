def mergear_y_contar(izq, der):
    ordenado = []
    contador = 0
    i = 0
    j = 0
    while i < len(izq) and j < len(der):
        izquierdo = izq[i]
        derecho = der[j]
        if izquierdo <= derecho:
            ordenado.append(izquierdo)
            i += 1
            continue
        ordenado.append(derecho)
        j += 1
        contador += len(izq)-i
    ordenado.extend(izq[i:])
    ordenado.extend(der[j:])
    return ordenado, contador

def _contar_inversiones(arreglo, inicio, fin):
    if inicio >= fin:
        return [arreglo[inicio]], 0
    medio = (inicio + fin) // 2
    izq, contador_izq = _contar_inversiones(arreglo, inicio, medio)
    der, contador_der = _contar_inversiones(arreglo, medio+1, fin)
    ordenado, contador = mergear_y_contar(izq, der)
    return ordenado, contador_izq + contador_der + contador 

def contar_inversiones(A, B):
    _, inversiones = _contar_inversiones(B, 0, len(B)-1)
    return inversiones
