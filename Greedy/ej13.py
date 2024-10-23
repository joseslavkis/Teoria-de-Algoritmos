def cobertura(casas, R, K):
    casas.sort()
    i = 0
    posiciones_antenas = []
    while i < len(casas):
        posicion_antena = min(casas[i] + R, K)
        posiciones_antenas.append(posicion_antena)

        while i < len(casas) and casas[i] <= posicion_antena + R:
            i += 1
    
    return posiciones_antenas



#Es un algoritmo greedy porque realiza en cada paso el fichar la casa de la izquierda
#para avanzar hasta a la maxima a la que puede acceder por la derecha si es que puede(tambien las casas intermedias).
#La complejidad es O(n log n)
#Obtiene una solución óptima local en cada paso al optimizar el rango de cada antena a la hora de colocarse, para abarcar la mayor cantidad de espacio útil posible.
#Al minimizar el numero de antenas, se consigue una serie de soluciones óptimas locales y deriva en una solucion óptima global que minimiza la cantidad de antenas necesarias