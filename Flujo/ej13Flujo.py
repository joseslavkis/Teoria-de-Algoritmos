'''(★★★) Carlos tiene un problema: sus 5 hijos no se soportan.
Esto es a tal punto, que ni siquiera están dispuestos a caminar juntos para ir a la escuela.
Incluso más: ¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus hermanos!
Sólo aceptan pasar por las esquinas, si es que algún otro pasó por allí.
Por suerte, tanto la casa como la escuela quedan en esquinas,
pero no está seguro si es posible enviar a sus 5 hijos a la misma escuela.
No se puede asumir que la ciudad tenga alguna forma en específico,
por ejemplo, no hay que asumir que todas las calles sean cuadradas.
Utilizando lo visto en la materia, formular este problema y resolverlo. Indicar y justificar la complejidad del algoritmo.'''


from grafo import Grafo

#recibo un grafo con las características propuestas bruh
def ej13(grafo):
    gr_ent = grafo.obtener_grados_entrada()
    gr_sal = grafo.obtener_grados_salida()
    fuente = None
    sumidero = None
    for v in grafo.obtener_vertices():
        if gr_ent[v] == 0:
            fuente = v
        if gr_sal[v] == 0:
            sumidero = v
    if not fuente or not sumidero: return
    flujo_maximo, flujo_aristas, grafo_residual_final = grafo.ford_fulkerson(fuente, sumidero)
    if flujo_maximo == 5:
        return True
    else:
        return False
    



