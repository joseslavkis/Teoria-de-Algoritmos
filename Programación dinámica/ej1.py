def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    ant = 0
    actual = 1
    for i in range(1, n+1):
        nuevo = ant + actual
        ant = actual
        actual = nuevo
    
    return actual