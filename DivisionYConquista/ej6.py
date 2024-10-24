def multiplicar(a, b):
    a = str(a)
    b = str(b)
    
    if len(a) == 1 or len(b) == 1:
        return int(a) * int(b)

    n = max(len(a), len(b))
    m = n // 2

    high_a, low_a = int(a[:-m]), int(a[-m:])
    high_b, low_b = int(b[:-m]), int(b[-m:])

    z0 = multiplicar(low_a, low_b)
    z1 = multiplicar(low_a + high_a, low_b + high_b)
    z2 = multiplicar(high_a, high_b)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0