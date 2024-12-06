def optimo_juan_el_vago(trabajos):
    n = len(trabajos)
    if n == 0:
        return [0]
    if n == 1:
        return [0, trabajos[0]]

    OPT = [0] * (n+1)
    OPT[1] = trabajos[0]
    OPT[2] = max(trabajos[0], trabajos[1])

    for i in range(3, n+1):
        OPT[i] = max(OPT[i-1], OPT[i-2] + trabajos[i-1])

    return OPT

def reconstruccion(OPT, trabajos):
    elecciones = []
    d = len(trabajos)
    while d > 0:
        if OPT[d] == OPT[d - 1]:
            d -= 1
        else:
            elecciones.append(d - 1)
            d -= 2

    elecciones.reverse()
    return elecciones

def juan_el_vago(trabajos):
    optimo = optimo_juan_el_vago(trabajos)
    return reconstruccion(optimo, trabajos)