def scheduling(charlas):
    if not charlas:
        return []
    charlas.sort(key=lambda x: x[1])

    n = len(charlas)
    opt = [0] * n
    selected = [[] for _ in range(n)]
    
    opt[0] = charlas[0][2]  # inicializo la ganancia de la primer charla como el optimo
    selected[0] = [charlas[0]]
    
    for i in range(1, n):
        no_tomar = opt[i - 1]

        prev = find_previous(charlas, i)
        tomar = charlas[i][2]
        if prev != -1:
            tomar += opt[prev]
        if tomar > no_tomar:
            opt[i] = tomar
            selected[i] = selected[prev] + [charlas[i]] if prev != -1 else [charlas[i]]
        else:
            opt[i] = no_tomar
            selected[i] = selected[i - 1]
    return selected[-1] if n > 0 else []
def find_previous(charlas, i):
    """encuentra el indice de la ultima charla que no se solapa con la charla i"""
    low, high = 0, i - 1
    while low <= high:
        mid = (low + high) // 2
        if charlas[mid][1] <= charlas[i][0]:
            if charlas[mid + 1][1] <= charlas[i][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1