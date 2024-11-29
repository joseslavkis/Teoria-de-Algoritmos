def resolver_sudoku(matriz):
    celda = encontrar_celda_vacia(matriz)
    if not celda:
        return matriz
    fila, columna = celda
    for num in range(1, len(matriz) + 1):
        if es_valido(matriz, fila, columna, num):
            matriz[fila][columna] = num
            if resolver_sudoku(matriz):
                return matriz
            matriz[fila][columna] = 0
    return False

def encontrar_celda_vacia(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                return (i, j)
    return None

def es_valido(matriz, fila, col, num):
    for i in range(len(matriz)):
        if matriz[fila][i] == num:
            return False
    for i in range(len(matriz[0])):
        if matriz[i][col] == num:
            return False
    inicio_fila = (fila // 3) * 3
    inicio_columna = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if matriz[inicio_fila + i][inicio_columna + j] == num:
                return False
    return True