def problema_soga(n):
    if n <= 1:
        return 0

    opt = [0] * (n + 1)

    opt[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i):
            opt[i] = max(opt[i], j * (i - j), j * opt[i - j])
    
    return opt[n]