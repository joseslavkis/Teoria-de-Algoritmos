# Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
# utilizando programación dinámica. Indicar y justificar la complejidad del algoritmo implementado (cuidado con esto, es
# fácil tentarse a dar una cota más alta de lo correcto). Implementar un algoritmo que permita reconstruir la solución.
# Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1^2
# , por lo que siempre existe solución. Sin embargo, la expresión 10 = 3^2 + 1^2
# es una manera más económica de escribirlo para n = 10, pues sólo tiene dos términos.

#Este es bastante dificil y poco trivial. Lo que habría que hacer es usar los cuadrados perfecto menores que i, 
# los cuales llamaremos muy originalmente como j. J son todas las raices menores o iguales que i (LA PARTE ENTERA),
#esto nos dará los cuadrados perfectos. 

# Ec de recurrencia -> opt[i] = min(opt[i], opt[i-j^2]+1), j <= sqrt(i)

#La verdad que este ej no lo entendí muy bien

import math

def minimos_cuadrados(n):
    opt = [float('inf')] * (n + 1)
    opt[0] = 0

    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            opt[i] = min(opt[i], opt[i - j * j] + 1) #Pongo opt[i] para evitar un gordo index error
    return opt[n]

def reconstruir_solucion(n):
    opt = [float('inf')] * (n + 1)
    opt[0] = 0
    pasos = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if opt[i] > opt[i - j * j] + 1:
                opt[i] = opt[i - j * j] + 1
                pasos[i] = j * j

    resultado = []
    while n > 0:
        resultado.append(pasos[n])
        n -= pasos[n]

    return resultado[::-1]

# Ejemplo de uso
n = 10
print("Mínima cantidad de términos:", minimos_cuadrados(n))
print("Reconstrucción de la solución:", reconstruir_solucion(n))



# Seguimiento del cálculo de opt[10]:

# 1. Inicializamos la tabla `opt` donde `opt[i]` representará el número mínimo de cuadrados perfectos necesarios para sumar `i`.
#    Inicialmente, `opt[0] = 0` y el resto es infinito: 
#    opt = [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

# 2. Calculamos opt[1]:
#    - Probamos j = 1, donde j^2 = 1:
#      opt[1] = min(opt[1], opt[1 - 1^2] + 1) = min(inf, 0 + 1) = 1
#    Resultado: opt[1] = 1

# 3. Calculamos opt[2]:
#    - Probamos j = 1, donde j^2 = 1:
#      opt[2] = min(opt[2], opt[2 - 1^2] + 1) = min(inf, 1 + 1) = 2
#    Resultado: opt[2] = 2

# 4. Calculamos opt[3]:
#    - Probamos j = 1, donde j^2 = 1:
#      opt[3] = min(opt[3], opt[3 - 1^2] + 1) = min(inf, 2 + 1) = 3
#    Resultado: opt[3] = 3

# 5. Calculamos opt[4]:
#    - Probamos j = 1, donde j^2 = 1:
#      opt[4] = min(opt[4], opt[4 - 1^2] + 1) = min(inf, 3 + 1) = 4
#    - Probamos j = 2, donde j^2 = 4:
#      opt[4] = min(opt[4], opt[4 - 2^2] + 1) = min(4, 0 + 1) = 1
#    Resultado: opt[4] = 1

# 6. Calculamos opt[5]:
#    - Probamos j = 1, donde j^2 = 1:
#      opt[5] = min(opt[5], opt[5 - 1^2] + 1) = min(inf, 1 + 1) = 2
#    - Probamos j = 2, donde j^2 = 4:
#      opt[5] = min(opt[5], opt[5 - 2^2] + 1) = min(2, 1 + 1) = 2
#    Resultado: opt[5] = 2

# 7. Calculamos opt[6]:
#    - Probamos j = 1, donde j^2 = 1:
#      opt[6] = min(opt[6], opt[6 - 1^2] + 1) = min(inf, 2 + 1) = 3
#    - Probamos j = 2, donde j^2 = 4:
#      opt[6] = min(opt[6], opt[6 - 2^2] + 1) = min(3, 2 + 1) = 3
#    Resultado: opt[6] = 3

# 8. Calculamos opt[7]:
#    - Probamos j = 1, donde j^2 = 1:
#      opt[7] = min(opt[7], opt[7 - 1^2] + 1) = min(inf, 3 + 1) = 4
#    - Probamos j = 2, donde j^2 = 4:
#      opt[7] = min(opt[7], opt[7 - 2^2] + 1) = min(4, 3 + 1) = 4
#    Resultado: opt[7] = 4

# 9. Calculamos opt[8]:
#    - Probamos j = 1, donde j^2 = 1:
#      opt[8] = min(opt[8], opt[8 - 1^2] + 1) = min(inf, 4 + 1) = 5
#    - Probamos j = 2, donde j^2 = 4:
#      opt[8] = min(opt[8], opt[8 - 2^2] + 1) = min(5, 1 + 1) = 2
#    Resultado: opt[8] = 2

# 10. Calculamos opt[9]:
#     - Probamos j = 1, donde j^2 = 1:
#       opt[9] = min(opt[9], opt[9 - 1^2] + 1) = min(inf, 2 + 1) = 3
#     - Probamos j = 2, donde j^2 = 4:
#       opt[9] = min(opt[9], opt[9 - 2^2] + 1) = min(3, 2 + 1) = 3
#     - Probamos j = 3, donde j^2 = 9:
#       opt[9] = min(opt[9], opt[9 - 3^2] + 1) = min(3, 0 + 1) = 1
#     Resultado: opt[9] = 1

# 11. Calculamos opt[10]:
#     - Probamos j = 1, donde j^2 = 1:
#       opt[10] = min(opt[10], opt[10 - 1^2] + 1) = min(inf, 1 + 1) = 2
#     - Probamos j = 2, donde j^2 = 4:
#       opt[10] = min(opt[10], opt[10 - 2^2] + 1) = min(2, 3 + 1) = 2
#     - Probamos j = 3, donde j^2 = 9:
#       opt[10] = min(opt[10], opt[10 - 3^2] + 1) = min(2, 1 + 1) = 2
#     Resultado: opt[10] = 2

# Resultado final:
# opt[10] = 2, que representa la cantidad mínima de términos cuadrados para escribir 10.
