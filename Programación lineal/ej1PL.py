''' Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).'''


import pulp # type: ignore

def mochila_max_valor(pesos, valores, W):
    n = len(pesos)

    problema = pulp.LpProblem("Problema_de_la_Mochila", pulp.LpMaximize)

    x = [pulp.LpVariable(f"x{i}", cat="Binary") for i in range(n)]

    problema += pulp.lpSum(valores[i] * x[i] for i in range(n)), "Valor_total"

    problema += pulp.lpSum(pesos[i] * x[i] for i in range(n)) <= W, "Restriccion_de_peso"

    problema.solve()

    print("Estado de la solución:", pulp.LpStatus[problema.status])

    objetos_seleccionados = [i for i in range(n) if pulp.value(x[i]) == 1]
    valor_maximo = pulp.value(problema.objective)
    
    return objetos_seleccionados, valor_maximo

pesos = [2, 10, 4, 5]
valores = [3, 4, 5, 6]
capacidad = 5

objetos_seleccionados, valor_maximo = mochila_max_valor(pesos, valores, capacidad)

print("Objetos seleccionados:", objetos_seleccionados)
print("Valor máximo:", valor_maximo)
