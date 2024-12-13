# Implementar un modelo de programación lineal que permita determinar el clique de tamaño máximo dentro de un
# grafo. Indicar la cantidad de restricciones generadas en función de la cantidad de vértices y aristas.


#Aclaración, este ejercicio se podía hacer de manera más óptima. En vez de una B es B-.

'''
xi = 1 si el nodo i pertenece al clique
   = 0 si no pertenece

xi+xj <= 1 para c/par de nodos i,j que no estén conectados
sum(xi) <= len(grafo) para todo i
objetivo: maximizar sum(xi)
'''


#En mi resolución hay V^2 restricciones, pero se puede hacer con V restricciones.












