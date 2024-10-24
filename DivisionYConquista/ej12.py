def alternar(arr):
    arr = alternar_arr(arr, 0, len(arr)-1)
            
def alternar_arr(arr, inicio, fin):
    if fin-inicio < 2:
        return
    centro = (inicio+fin) // 2
    alternar_arr(arr, inicio, centro)
    alternar_arr(arr, centro+1, fin)
    for i in range(inicio, centro+1):
        if i % 2 != 0:
            arr[i], arr[centro+i-inicio] = arr[centro+i-inicio], arr[i]
    return