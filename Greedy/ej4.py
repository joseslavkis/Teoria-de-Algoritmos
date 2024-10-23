def charlas(horarios):
    horarios_ordenados = sorted(horarios, key=lambda x: x[1])

    charlas_seleccionadas = []

    fin_ultima_charla = float('-inf')

    for inicio, fin in horarios_ordenados:
        if inicio >= fin_ultima_charla:
            charlas_seleccionadas.append((inicio, fin))
            fin_ultima_charla = fin
            
    return charlas_seleccionadas