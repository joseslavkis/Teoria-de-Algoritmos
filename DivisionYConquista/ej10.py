def mas_de_la_mitad(arr):
    cand = _mas_de_la_mitad(arr)
    return cand != None

def _mas_de_la_mitad(arr):

    if len(arr) == 1:
        return arr[0]
    if len(arr) == 0:
        return None
    aux = []

    for i in range(0, len(arr)-1, 2):
        if arr[i] == arr[i+1]:
            aux.append(arr[i])

    candidato = _mas_de_la_mitad(aux)

    if candidato and arr.count(candidato) > len(arr)//2:
        return candidato
    if len(arr)%2 != 0 and arr.count(arr[-1]) > len(arr)//2:
        return arr[-1]
    else:
        return None