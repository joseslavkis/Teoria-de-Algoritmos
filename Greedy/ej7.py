def precios_inflacion(R):
    R.sort(reverse=True)
    costo_total = 0
    for j in range(len(R)):
        costo_total += R[j] ** (j + 1)
    
    return costo_total