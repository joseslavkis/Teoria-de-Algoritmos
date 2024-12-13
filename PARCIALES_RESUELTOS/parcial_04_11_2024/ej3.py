# Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se
# predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de
# estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la
# casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto,
# es la de maximizar la ganancia dada por p[k] − p[j].

'''
max_ben[i] = max(max_ben[i-1], p[i] - min_precio[i])
min_precio[i] = min(min_precio[i-1], p[i])

Explicación: una vez que queres ver si el beneficio es maximo tenes 2 opciones:
1) Tomar el beneficio del dia anterior que era óptimo sin considerar la opción actual(max_ben[i-1])
2) Tomar la opción actual y restarle el precio minimo actual(que fue al valor que compraste la casa)

Y la ecuación de min_precio[i] es para ir guardando el minimo precio que se va viendo en cada iteración:
1) Tomar el minimo precio del dia anterior(min_precio[i-1])
2) Tomar el precio actual(p[i]) y ver si es menor que el minimo precio anterior(p[i])
Para este caso se usa min()
'''

def ej3(P):
    n = len(P)
    if n < 2: return 0, None, None
    max_ben = [0] * n
    min_precio = [0] * n
    min_precio[0] = P[0]
    for i in range(1,n):
        min_precio[i] = min(min_precio[i-1], P[i])
        max_ben[i] = max(max_ben[i-1], P[i] - min_precio[i])
    dia_venta = max_ben.index(max(max_ben))
    dia_compra = P.index(min_precio[dia_venta])
    return max(max_ben), dia_compra, dia_venta

#O(n) donde n es la cantidad de días


