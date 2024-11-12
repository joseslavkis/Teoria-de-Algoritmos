# El famoso ladrón Francesco Rizzoli (hermano del “árbitro” de la final del 2014), ha decidido hacer un atraco a un
# laboratorio farmacéutico. Allí puede robarse diferentes fármacos que se están estudiando (en formato líquido). Tiene un
# catálogo del valor de cada fármaco, que puede vender en el mercado negro. De cada fármaco hay una diferente cantidad
# disponible (medible en ml). Rizzoli sólo tiene posibilidad en su equipo de llevarse como máximo L ml en fármacos. Lo
# bueno es que sabe que puede fraccionar y poner proporciones de los fármacos; y en ese caso lo vendería en su valor
# proporcional. Implementar un algoritmo greedy que obtenga los fármacos (y cantidades) que Rizzoli debe robarse para
# obtener la máxima ganancia posible (el algoritmo debe ser óptimo, en esta familia no se aceptan los robos a medias).
# Justificar por qué el algoritmo propuesto es Greedy. Indicar y justificar la complejidad del algoritmo implementado.


# Bueno, es como el problema de la mochila fraccionada. Francesco podrá robar
# La estrategia greedy será la siguiente: agarrar todo lo que pueda del que tenga mayor relación precio/cantidad.
# Agarramos lo que podamos del que tenga mejor relacion y si la cantidad de uno sobrepasa los limites, tomamos la fracción que podamos sin pasarnos de L. 


#Asumo que precios es un diccionario, cantidades es otro diccionario y medicamentos es una lista
def medicamentos(medicamentos, L, cantidades, precios):
    medicamentos_ordenados = sorted(medicamentos, key=lambda x: precios[x]/cantidades[x], reverse=True)
    cantidad_actual = 0
    resultado = []
    for medicamento in medicamentos_ordenados:
        if cantidad_actual + cantidades[medicamento] <= L:
            resultado.append((medicamento, cantidades[medicamento]))
            cantidad_actual += cantidades[medicamento]
        else:
            cantidad_a_llevarse = L - cantidad_actual
            resultado.append((medicamento, cantidad_a_llevarse))
            cantidad_actual += cantidad_a_llevarse
    return cantidad_actual, resultado


# Es optimo porque a diferencia del problema de la mochila con greedy, podemos obtener raciones de las mejores remedios precio/cantidad que hay disponibles.
# Además, como se pueden fraccionar, no nos debemos conformar con agarrar otro medicamento de menor precio/cantidad pero que tenga una cantidad
# disponible menor al que tenia mejor relacion precio/cantidad (La regla greedy ya fue explicada arriba)




