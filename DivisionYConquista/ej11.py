def mas_de_dos_tercios(arr):
    if not arr:
        return False
    candidato = encontrar_candidato(arr)
    return verificar_candidato(arr, candidato)

def encontrar_candidato(arr):
    conteo = 0
    candidato = None
    for num in arr:
        if conteo == 0:
            candidato = num
        conteo += (1 if num == candidato else -1)
    return candidato

def verificar_candidato(arr, candidato):
    conteo = sum(1 for num in arr if num == candidato)
    return conteo > (2 * len(arr)) // 3