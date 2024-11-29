from compatibles import * #type:ignore

def obtener_combinaciones(materias):
    if not materias:
        return []
    return obtener_combinaciones_rec(materias, [])

def obtener_combinaciones_rec(materias, solucion_actual):
    if len(materias) == 0:
        if es_valido(solucion_actual):
            return [solucion_actual]
        else:
            return []
    
    materia_actual = materias[0]
    restantes = materias[1:]
    soluciones = []

    for curso in materia_actual:
        nueva_solucion = solucion_actual + [curso]
        if es_valido(nueva_solucion):
            soluciones.extend(obtener_combinaciones_rec(restantes, nueva_solucion))

    return soluciones

def es_valido(sol):
    for i in range(len(sol)):
        for j in range(i + 1, len(sol)):
            if not son_compatibles(sol[i], sol[j]): # type:ignore
                return False
    return True