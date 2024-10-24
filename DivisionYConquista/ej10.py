def mas_de_la_mitad(arr):
    candidato = encontrar_candidato(arr)
    return verificar_candidato(arr, candidato)

def encontrar_candidato(arr):
    candidato, conteo = None, 0
    
    for num in arr:
        if conteo == 0:
            candidato = num
        conteo += (1 if num == candidato else -1)
    
    return candidato

def verificar_candidato(arr, candidato):
    conteo = sum(1 for num in arr if num == candidato)
    return conteo > len(arr) // 2