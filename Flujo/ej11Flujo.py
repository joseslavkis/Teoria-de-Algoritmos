# Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca.
# La biblioteca tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes.
# Implementar un algoritmo que nos permita obtener la forma de asignar libros a
# alumnos de tal forma que la cantidad de préstamos sea máxima.
# Dar la metodología, explicando en detalle cómo se modela el problema, cómo se lo resuelve
# y cómo se consigue la máxima cantidad de prestamos. ¿Cuál es el orden temporal de la solución implementada?


from grafo import Grafo
# el grafo ya viene con la forma en la que lo quiero tener
def asignar_libros(grafo):
    flujo_maximo, _, _ = grafo.ford_fulkerson('fuente', 'sumidero')
    return flujo_maximo
