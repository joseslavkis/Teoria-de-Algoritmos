def bolsas(capacidad, productos):
    copia = productos[:]
    copia.sort()
    carrito = []
    bolsa = []

    for producto in copia:
        if sum(bolsa)+producto <= capacidad: 
            bolsa.append(producto)
            continue
        carrito.append(bolsa.copy())
        bolsa.clear() 
        bolsa.append(producto) 

    if bolsa: carrito.append(bolsa) 

    return carrito