def elemento_desordenado(arr):
    if fuera_de_lugar(arr, 0):
        return arr[0]
    return elemento_desordenado_rec(arr, 0, len(arr)-1)

def fuera_de_lugar(arr, pos):
    if pos == 0:
        return arr[0] > arr[1] and (len(arr) < 3 or arr[1] < arr[2])
    if pos == len(arr)-1:
        return arr[pos] < arr[pos-1] and (len(arr) < 3 or arr[pos-2] < arr[pos-1])
    return arr[pos-1] < arr[pos+1] and (arr[pos] > arr[pos+1] or arr[pos] < arr[pos-1])

def elemento_desordenado_rec(arr, ini, fin):
    medio = (ini+fin) // 2

    if fin < ini:
        return 0

    if fuera_de_lugar(arr, medio):
        return arr[medio]
    
    izq = elemento_desordenado_rec(arr, ini, medio-1)
    der = elemento_desordenado_rec(arr, medio+1, fin)

    return izq + der