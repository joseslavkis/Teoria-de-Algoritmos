'''La ecuación de recurrencia es opt[i]= min(opt[i-1]+1,opt[i/2]+1)'''

def operaciones(k):
    if k == 0:
        return []

    opt = [float('inf')] * (k + 1)
    prev = [-1] * (k + 1)
    operaciones = [''] * (k + 1)

    opt[0] = 0

    for i in range(1, k + 1):
        if opt[i - 1] + 1 < opt[i]:
            opt[i] = opt[i - 1] + 1
            prev[i] = i - 1
            operaciones[i] = 'mas1'

        if i % 2 == 0 and opt[i // 2] + 1 < opt[i]:
            opt[i] = opt[i // 2] + 1
            prev[i] = i // 2
            operaciones[i] = 'por2'

    camino = []
    actual = k
    while actual > 0:
        camino.append(operaciones[actual])
        actual = prev[actual]

    return camino[::-1]