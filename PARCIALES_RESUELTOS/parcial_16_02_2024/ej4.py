# La Nación del Fuego está atacando al Reino de la Tierra en su capital, Ba Sing Se. Es conocido el eficiente sistema de
# riego de la ciudad, que le permite estar encerrada sin problemas. A la ciudad entran k ríos, y mediante un sistema
# de tuberías logran encausar el agua hacia los m puntos de riego. Gracias a un espía, la Nación del Fuego obtuvo un
# plano completo de la red, incluyendo cuánta agua puede transportar cada tubería, etc. . . El Señor del Fuego ha ideado
# un plan: infiltrar a un atacante que destruya un único punto de conexión de tuberías (no creen que poder tener más
# tiempo que para esto). La conexión debería ser la que reduzca lo máximo posible la cantidad de agua que llega a las
# zonas de riego. Implementar un algoritmo que determine cuál conexión de la red debería atacar la Nación del Fuego.
# Indicar y justificar la complejidad del algoritmo implementado.

#ACLARACIÓN: este ejercicio es bastante pseudocódigo, no voy a testear el algoritmo (y posiblemente tampoco ande).

#Lo importante es saber elegir cual arista debemos eliminar para reducir lo maximo posible el flujo.
#Las aristas del corte mínimo son aquellas que hacen de "frontera" entre los vértices alcanzables por 
# la fuente y los vértices alcanzables por el sumidero. Esto se debe a que estas aristas hacen de cuello de botella.
#Además, por el teorema del flujo máximo, el flujo que llega al sumidero (o que sale de la fuente, son equivalentes) 
# es igual a la capacidad de estas aristas.
#Por lo tanto deberemos eliminar una arista del corte mínimo, ¿Pero cual?. Bueno si tenemos una arista de capacidad 1
# que es cuello de botella no va a cambiar demasiado eliminarla. Osea va a pasar una unidad menos de flujo, ¡Que logro!
# En cambio si eliminamos del corte mínimo la arista de mayor peso, esta será el mayor cuello de botella de la red de flujo, 
# por lo tanto reduciremos la cantidad de flujo que pasa tanto como peso haya en esta arista. 

def eliminar_mejor_arista(grafo, fuente, sumidero):
    red_residual, flujos = grafo.ford_fulkerson(grafo, fuente, sumidero) #reitero, mi implementacion de ford_fulkerson no devuelve esto. Es pseudocodigo.
    alcanzables = encontrar_corte_minimo(red_residual, fuente) #Encontramos los alcanzables desde la fuente
    arista_seleccionada = None
    capacidad_max = 0
    for v in alcanzables:
        for w, capacidad in grafo.adyacentes(v):
            if v not in alcanzables and capacidad > capacidad_max:
                capacidad_max = capacidad
                arista_seleccionada = (v, w)
    return arista_seleccionada

def encontrar_corte_minimo(red_residual, fuente):
    visitados = set()
    dfs(red_residual, fuente, visitados)
    return visitados

def dfs(red_residual, v, visitados):
    visitados.add(v)
    for w, capacidad in red_residual.adyacentes(v):
        if w not in visitados and capacidad > 0: #para no agarrar aristas consumidas
            dfs(red_residual, w, visitados)

#Estos ejercicios con saber como sacar el corte mínimo (osea como codearlo) ya medio que tenes gran parte cubierta. El problema
# es entender conceptualmente en que difiere una arista consumida al 100% que no pertenece al corte mínimo y una arista del corte mínimo
# (que por definición tambien fue consumida 100%)
