# En un hospital, se tiene un conjunto de médicos y un conjunto de pacientes. Cada médico tiene un horario con franjas
# horarias disponibles para citas médicas. Nuestro objetivo es emparejar médicos con pacientes de manera que se maximice
# el número total de citas médicas programadas. Implementar un algoritmo que resuelva dicho problema de manera
# eficiente. Indicar y justificar la complejidad del algoritmo implementado.


#Cada médico tiene franjas horarias disponibles en las que cada uno podrá atender a un paciente, mientras que cada
#paciente como mucho podrá recibir una franja horaria (lo aclaro por simplificación, no tiene mucho sentido q un paciente al hilo se atienda 8 veces)
#Podemos armar un grafo bipartito en el que una componente bipartita sean los médicos y otra los pacientes. 
#La fuente se conectará a cada médico otorgandole un flujo igual al número de citas disponibles que este posee, y cada médico se conectará con
#un paciente a través de una arista de peso 1. Y bueno obviamente cada paciente se conectará al sumidero con una arista de peso 1(para
#representar que cada paciente se atiende una sola vez)


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo

def medicos(franjas_horarias, cant_pacientes):
    grafo = Grafo(True)
    grafo.agregar_vertice("fuente")
    grafo.agregar_vertice("sumidero")

    vertices_de_medicos = []
    for i, elem in enumerate(franjas_horarias):
        medico_id = f"medico_{i}"
        grafo.agregar_vertice(medico_id)
        vertices_de_medicos.append(medico_id)
        grafo.agregar_arista("fuente", medico_id, elem)

    vertices_de_pacientes = []
    aristas_pacientes_a_sumidero = []
    for i in range(cant_pacientes):
        paciente_id = f"paciente_{i}"
        grafo.agregar_vertice(paciente_id)
        vertices_de_pacientes.append(paciente_id)
        grafo.agregar_arista(paciente_id, "sumidero", 1)
        aristas_pacientes_a_sumidero.append(f"paciente_{i}", "sumidero")
    for medico in vertices_de_medicos:
        for paciente in vertices_de_pacientes:
            grafo.agregar_arista(medico, paciente, 1)

    flujo, _ = grafo.ford_fulkerson("fuente", "sumidero")
    resultado = 0
    cant_turnos_por_medico = []
    for elem in aristas_pacientes_a_sumidero:
        resultado += flujo[elem]
    
    for elem in vertices_de_medicos:
        cant_turnos_por_medico.append((elem, flujo[elem]))
    
    return resultado, cant_turnos_por_medico





