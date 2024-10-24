from balanza import * # type: ignore

def encontrar_joya(joyas):
    aux = []
    ubicacion_de_joyas = llenar_indices(joyas, aux)
    return _encontrar_joyas(joyas, ubicacion_de_joyas, 0)

def llenar_indices(origen, destino):
    for i in range(len(origen)):
        destino.append(i)
    return destino

def _encontrar_joyas(joyas, indices_joyas, cantidad_extraidas):
    if len(joyas) == 1: return indices_joyas[0]

    medio = (len(joyas))//2
    izq, der = joyas[:medio], joyas[medio:]

    if len(izq) > len(der):
        izq = joyas[1:medio]
        joya_extraida = cantidad_extraidas

    elif len(izq) < len(der):
        der = joyas[medio:len(joyas)-1]
        joya_extraida = (len(joyas) - 1 + cantidad_extraidas)

    res = balanza(izq, der) # type: ignore

    if res == 1:
        return _encontrar_joyas(izq, indices_joyas[:medio], len(der))
    elif res == -1:
        return _encontrar_joyas(der, indices_joyas[medio:], len(izq))
    else:
        return joya_extraida