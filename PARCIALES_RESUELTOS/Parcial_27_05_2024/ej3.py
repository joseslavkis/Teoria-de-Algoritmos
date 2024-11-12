'''
Realizar un modelo de programación lineal que obtenga el mínimo Dominating Set de un Grafo no dirigido. En dicho
grafo, cada vértice tiene un valor (positivo), y se quiere que dicho Dominating Set sea el de mínima suma de dichos
valores.
'''

'''

variable x_i = 1 si el vértice i pertenece al Dominating Set, 0 en caso contrario
objetivo = minimize(sum(v_i*x_i))
restriccion => para un vertice i del grafo, x_i + sum(w_i) >=1, donde w_i es un vértice adyacente a i
'''