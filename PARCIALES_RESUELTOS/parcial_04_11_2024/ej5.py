# Resolver el problema de Osvaldo (ejercicio 3) pero por división y conquista. Indicar y justificar adecuadamente la
# complejidad del algoritmo implementado. Es probable que la complejidad de ambas soluciones no quede igual, no te
# estreses por ello.


def max_ganancia(p):
    if len(p) <= 1:
        return 0

    mid = len(p) // 2
    izquierda = p[:mid]
    derecha = p[mid:]

    ganancia_izquierda = max_ganancia(izquierda)
    ganancia_derecha = max_ganancia(derecha)

    min_izquierda = min(izquierda)
    max_derecha = max(derecha)
    ganancia_cruzada = max_derecha - min_izquierda

    return max(ganancia_izquierda, ganancia_derecha, ganancia_cruzada)


p = [7, 1, 5, 3, 6, 4]
print(max_ganancia(p))

#Generado con GPT:

# Para el array p = [7, 1, 5, 3, 6, 4]:
# izquierda = [7, 1, 5]
# derecha = [3, 6, 4]
# min_izquierda = 1 (el precio más bajo en la mitad izquierda)
# max_derecha = 6 (el precio más alto en la mitad derecha)
# ganancia_cruzada = 6 - 1 = 5
