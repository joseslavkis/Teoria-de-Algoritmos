def cajas(capacidad, libros):
    libros_ordenados = sorted(libros)
    caja_con_libros = []
    cajas = []

    for espesor in libros_ordenados:
        if espesor > capacidad:
            continue
        elif sum(caja_con_libros) + espesor <= capacidad:
            caja_con_libros.append(espesor)
        else:
            cajas.append(caja_con_libros)
            caja_con_libros = [espesor]

    if caja_con_libros:
        cajas.append(caja_con_libros)

    return cajas