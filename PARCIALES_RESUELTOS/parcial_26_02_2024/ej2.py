# Todos los años la asociación de Tiro con Arco profesional realiza una preclasificación de los n jugadores que terminaron
# en las mejores posiciones del ranking para un evento exclusivo. En la tarjeta de invitación quieren adjuntar el número de
# posición en la que está actualmente y a cuántos rivales invitados logró superar en el ranking, en comparación al ranking
# del año pasado. Contamos con un listado que tiene el nombre del jugador y la posición del ranking del año pasado
# ordenado por el ranking actual. Implementar un algoritmo que dada la lista mencionada, devuelva (por ejemplo, en un
# diccionario) a cuántos rivales ha superado cada uno de los invitados. Para realizar esto de forma eficiente, recomendamos
# utilizar División y Conquista.
# Ejemplo: LISTA: [(A, 3), (B, 4), (C, 2), (D, 8), (E, 6), (F, 5)]. Se puede ver que el jugador A pasó del
# 3er lugar al 1er lugar, superando al jugador C. El jugador B llegó al segundo lugar y superó al jugador C. El jugador C
# no logró superar a ninguno de los invitados (si bien se encuentra en la tercera posición, ya tenía el año anterior mejor
# clasificación que el resto de invitados, por tanto no logró superar a ninguno), etc. . .

#Es el mismo ejercicio que conteo de inversiones solo que esta vez el arreglo no esta completo(puede no estar el 1 por ejemplo)

#La idea sería aplicar un ordenamiento antes de empezar a codear asi tenemos 2 arreglos para revisar las inversiones
#Este esta medio chatgpteado, era medio choto

def determinar_adelantos(arr): 
    arrAnterior = sorted(arr, key=lambda x: x[1])
    posiciones_actuales = {jugador: idx for idx, (jugador, _) in enumerate(arr)}
    adelantos = {jugador: 0 for jugador, _ in arr}
    
    def contar_inversiones(arr, ini, fin):
        if ini >= fin:
            return 0, arr[ini:fin+1] if ini == fin else []
        
        medio = (ini + fin) // 2
        inv_izq, izq_ordenado = contar_inversiones(arr, ini, medio)
        inv_der, der_ordenado = contar_inversiones(arr, medio + 1, fin)
        
        i = j = 0
        inversiones = inv_izq + inv_der
        merged = []
        
        while i < len(izq_ordenado) and j < len(der_ordenado):
            if posiciones_actuales[izq_ordenado[i][0]] <= posiciones_actuales[der_ordenado[j][0]]:
                merged.append(izq_ordenado[i])
                i += 1
            else:
                adelantos[der_ordenado[j][0]] += len(izq_ordenado) - i
                merged.append(der_ordenado[j])
                inversiones += len(izq_ordenado) - i
                j += 1
        
        merged.extend(izq_ordenado[i:])
        merged.extend(der_ordenado[j:])
        
        return inversiones, merged
    
    contar_inversiones(arrAnterior, 0, len(arrAnterior) - 1)
    
    return adelantos

arr = [('A', 3), ('B', 4), ('C', 2), ('D', 8), ('E', 6), ('F', 5)]
adelantos = determinar_adelantos(arr)
print(adelantos)
