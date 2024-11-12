# Implementar un algoritmo potencia(b, n) que nos devuelva el resultado de b^n en tiempo O(log n). Justificar
# adecuadamente la complejidad del algoritmo implementado. Ayuda: recordar propiedades matemáticas de la potencia.
# Por ejemplo, que a^h * a^k = a^(h+k).

def potencia(b, n):
    if n == 0:
        return 1
    elif n == 1:
        return b

    medio = potencia(b, n // 2)
    if n % 2 == 0:
        return medio * medio # b^n = b^(n/2) * b^(n/2)
    else:
        return b * medio* medio # b^n = b * b^((n-1)/2) * b^((n-1)/2)

print(potencia(2, 3))
