# pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
    pedidos_ordenados = sorted(pedidos, key=lambda x: x[1])

    pedidos_seleccionados = []

    fin_ultimo_pedido = float('-inf')

    for inicio, fin in pedidos_ordenados:
        if inicio >= fin_ultimo_pedido:
            pedidos_seleccionados.append((inicio, fin))
            fin_ultimo_pedido = fin
            
    return pedidos_seleccionados