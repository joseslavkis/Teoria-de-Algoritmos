def minimizar_latencia(L_deadline, T_tareas):
    i = 0
    res = []
    tareas = []
    while i < len(L_deadline):
        deadline =  L_deadline[i]
        tiempo = T_tareas[i]
        tareas.append((deadline,tiempo))
        i += 1
    ordenado = sorted(tareas, key=lambda x: x[0])
    fecha = 0
    for tarea in ordenado:
        deadline, tiempo = tarea
        latencia = (fecha + tiempo) - deadline
        fecha += tiempo
        if latencia < 0:
            latencia = 0
        res.append((tiempo,latencia))
    return res