def cambio(monedas, monto):
    dp = [float('inf')] * (monto + 1)
    dp[0] = 0

    used_coins = [-1] * (monto + 1)

    for moneda in monedas:
        for i in range(moneda, monto + 1):
            if dp[i - moneda] + 1 < dp[i]:
                dp[i] = dp[i - moneda] + 1
                used_coins[i] = moneda
    
    if dp[monto] == float('inf'):
        return []

    resultado = []
    current_monto = monto
    while current_monto > 0:
        moneda = used_coins[current_monto]
        resultado.append(moneda)
        current_monto -= moneda
    
    return resultado