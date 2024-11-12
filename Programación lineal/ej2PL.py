''''Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago (ejercicio 4 de PD).'''

import pulp

def juan_el_vago(trabajos):
    problema = pulp.LpProblem("Maximizar_Ganancias", pulp.LpMaximize)

    n = len(trabajos)
    x = [pulp.LpVariable(f"x{i}", cat='Binary') for i in range(n)]

    problema += pulp.lpSum(trabajos[i] * x[i] for i in range(n)), "Total_Ganancias"

    for i in range(n - 1):
        problema += x[i] + x[i + 1] <= 1, f"Restriccion_no_dos_dias_seguidos_{i}"

    problema.solve()

    valor_maximo = pulp.value(problema.objective)

    dias_a_trabajar = [i for i in range(n) if pulp.value(x[i]) == 1]

    return dias_a_trabajar, valor_maximo

trabajos = [100, 5, 50, 1, 1, 200]
dias_a_trabajar, valor_maximo = juan_el_vago(trabajos)

print("Días a trabajar:", dias_a_trabajar)
print("Valor máximo ganado:", valor_maximo)
