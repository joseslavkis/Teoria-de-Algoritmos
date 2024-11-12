# Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no
# puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta $Ci. 
# También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos Gi.
# Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos. Indicar y
# justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores están expresados en pesos argentinos,
# dólares u otra moneda? (haciendo la equivalencia de divisa, siempre suponiendo valores enteros).


#Bueno este es un ejercicio de programación dinámica 
#Si estuviste haciendo reducciones podrás ver que es literalmente el problema de la mochila, W sería P, Ci seria Pi(el peso del elemento i)
# y Gi sería Vi(el valor del elemento i)

#Ec de recurrencia -> opt[n][P] = max(opt[n-1][P], opt[n-1][P-Ci] + Gi)

#Asumo que campañas es un diccionario con clave el nombre y valor una tupla (Gi, Ci)
def seleccionar_campañas(campañas, P):
    n = len(campañas)
    opt = [[0 for _ in range(P + 1)] for _ in range(n + 1)]
    for i in range(1, n+1):
        ganancia, coste = campañas[i-1]
        for j in range(1, P+1):
            if coste <= j:
                opt[i][j] = max(opt[i-1][j], opt[i-1][j-coste] + ganancia)
            else:
                opt[i][j] = opt[i-1][j]
    return reconstruccion(opt, P, campañas)

def reconstruccion(opt, P, campañas):
    n = len(opt)
    j = P
    resultado = []
    for i in range(n, 0, -1):
        if opt[i][j] != opt[i-1][j]:
            resultado.append(campañas[i-1])
            j -= campañas[i-1][1]
    return resultado[::-1]





