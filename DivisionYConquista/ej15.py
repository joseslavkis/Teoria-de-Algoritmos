def raiz(funcion, a, b):
    if funcion(a)*funcion(b) > 0:
        return None
    return raiz_rec(funcion, a, b)

def raiz_rec(funcion, a, b):
    if a == b:
        return a

    medio = (a+b) // 2

    if funcion(medio) == 0:
        return medio
    if funcion(a)*funcion(medio) < 0:
        return raiz_rec(funcion, a, medio)
    else:
        return raiz_rec(funcion, medio, b)