def obtener_pos_ady(i, j, matriz):
    total = []

    for i2 in range(max(0, i - 2), min(i + 3, len(matriz))):
        for j2 in range(max(0, j - 2), min(j + 3, len(matriz[i2]))):
            total.append((i2, j2))

    return total

def contar_submarinos(i, j, matriz):
    pos = obtener_pos_ady(i, j, matriz)
    count = 0

    for i2, j2 in pos:
        if matriz[i2][j2]:
            count += 1

    return count

def calcular_mejores_pos(matriz):
    celdas_iluminadas = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            celdas_iluminadas.append(((i, j), contar_submarinos(i, j, matriz)))

    celdas_iluminadas.sort(key=lambda x: x[1], reverse=True)

    return celdas_iluminadas

def submarinos(matriz):
    if len(matriz) == 0:
        return []
    
    celdas_iluminadas = calcular_mejores_pos(matriz)

    faros = []

    while True:
        (x, y), peso = celdas_iluminadas.pop(0)

        if peso == 0:
            break

        faros.append((x, y))

        posiciones = obtener_pos_ady(x, y, matriz)

        for i, j in posiciones:
            matriz[i][j] = False

        celdas_iluminadas = calcular_mejores_pos(matriz)

    return faros