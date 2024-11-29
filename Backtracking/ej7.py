movimientos_caballo = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def es_valido(x, y, tablero, n):
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1

def cuenta_movimientos_validos(x, y, tablero, n):
    contador = 0
    for mov in movimientos_caballo:
        nuevo_x = x + mov[0]
        nuevo_y = y + mov[1]
        if es_valido(nuevo_x, nuevo_y, tablero, n):
            contador += 1
    return contador

def resolver_tour(tablero, x, y, mov_count, n):
    if mov_count == n * n:
        return True

    posibles_movimientos = []
    for mov in movimientos_caballo:
        nuevo_x = x + mov[0]
        nuevo_y = y + mov[1]
        if es_valido(nuevo_x, nuevo_y, tablero, n):
            posibles_movimientos.append((cuenta_movimientos_validos(nuevo_x, nuevo_y, tablero, n), nuevo_x, nuevo_y))

    posibles_movimientos.sort()

    for _, nuevo_x, nuevo_y in posibles_movimientos:
        tablero[nuevo_x][nuevo_y] = mov_count
        if resolver_tour(tablero, nuevo_x, nuevo_y, mov_count + 1, n):
            return True
        tablero[nuevo_x][nuevo_y] = -1

    return False

def knight_tour(n):
    tablero = [[-1 for _ in range(n)] for _ in range(n)]
    x_inicial, y_inicial = 0, 0
    tablero[x_inicial][y_inicial] = 0

    if resolver_tour(tablero, x_inicial, y_inicial, 1, n):
        for fila in tablero:
            print(fila)
        return True
    else:
        return False