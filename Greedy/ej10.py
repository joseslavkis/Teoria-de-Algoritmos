def ordenar(x):
    return x[1]

def bifurcaciones_con_patrulla(ciudades):

    if (len(ciudades) == 0):
        return []

    result = []
    ciudades.sort(key=ordenar)
    ciudad_anterior = ciudades[0]
    i = 0
    j = 0

    while i < len(ciudades):
        while abs(ciudad_anterior[1] - ciudades[j][1]) <= 50 :
            j = j + 1
            if (j >= len(ciudades)):
                break
        result.append(ciudades[j-1])
        if (j + 1 >= len(ciudades)):
            break
        ciudad_anterior = ciudades[j+1]
        i = i + 1
        j = j + 1
    return result