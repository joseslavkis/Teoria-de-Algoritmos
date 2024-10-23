def parte_entera_raiz(n):
    return _parte_entera_raiz(n, 0, n)

def _parte_entera_raiz(n, inicio, fin):
    if inicio > fin:
        return fin
    medio = (inicio + fin) // 2

    if medio*medio == n:
        return medio
    elif medio*medio < n:
        return _parte_entera_raiz(n, medio + 1, fin)
    else:
        return _parte_entera_raiz(n, inicio, medio - 1)