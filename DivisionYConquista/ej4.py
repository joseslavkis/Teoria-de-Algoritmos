def posicion_pico(v, ini, fin):
    if ini >= fin:
        return ini
    
    medio = (ini + fin) // 2

    if v[medio-1] < v[medio] > v[medio+1]:
        return medio
    
    if v[medio-1] > v[medio]:
        return posicion_pico(v, ini, medio-1)
    
    return posicion_pico(v, medio+1, fin)