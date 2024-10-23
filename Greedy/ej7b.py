def precios_deflacion(R):
    R.sort(reverse=False)
    costo_total = 0

    for j in range(len(R)):
        costo_total += R[j] / (2 ** j)
    
    return costo_total