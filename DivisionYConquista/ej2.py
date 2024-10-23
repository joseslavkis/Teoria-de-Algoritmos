def indice_primer_cero(arr):
    return _indice_primer_cero(arr, 0, len(arr) - 1)

def _indice_primer_cero(arr, inicio, fin):
    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2

    if arr[medio] == 0 and (medio == 0 or arr[medio - 1] == 1):
        return medio

    elif arr[medio] == 1:
        return _indice_primer_cero(arr, medio + 1, fin)
    else:
        return _indice_primer_cero(arr, inicio, medio - 1)