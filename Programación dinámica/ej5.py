'''opt[i][j] = max(opt[i][j-1], opt[i-1][j]) + matriz[i][j]'''

def laberinto(matriz):
    if not matriz:
        return 0
    n = len(matriz)
    m = len(matriz[0])
    opt = [[0]*m for _ in range(n)]
    opt[0][0] = matriz[0][0]
    for j in range(1, m):
        opt[0][j] = opt[0][j-1] + matriz[0][j]
    for i in range(1, n):
        opt[i][0] = opt[i-1][0] + matriz[i][0]
    for i in range(1, n):
        for j in range(1, m):
            opt[i][j] = max(opt[i][j-1], opt[i-1][j]) + matriz[i][j]
    camino = reconstrucción(opt)
    return opt[n-1][m-1]


def reconstrucción(opt):
    n = len(opt)
    m = len(opt[0])
    camino = []
    i, j = n-1, m-1
    while i > 0 and j>0:
        camino.append((i,j))
        if i == 0:
            j-=1
        elif j == 0:
            i-=1
        else:
            if opt[i-1][j] > opt[i][j-1]:
                i -= 1
            else:
                j -= 1
    camino.append((0,0))
    camino.reverse()
    return camino