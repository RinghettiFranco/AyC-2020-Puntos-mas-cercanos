from math import *
from utils import *

# Probamos todos con todos, cual orgia de Liberace (?)
@timer_function
def pmcBasico(Puntos):
    min_dist = INF

    for i in Puntos:
        for j in Puntos:
            if i != j:
                m = min(min_dist, distancia(i, j))
                if m < min_dist:
                    pi = i
                    pj = j
                    min_dist = m

    print(f'Distancia minima: {min_dist} entre los puntos {pi} y {pj}')

    return min_dist

# Optimizacion aplicada considerando la propiedad de
# conmutatividad de la distancia. dist(x, y) = dist(y, x)
@timer_function
def pmcBasicoOptimizado(Puntos):
    min_dist = INF

    for i in range(0, len(Puntos)):
        for j in range(i, len(Puntos)):
            if i != j:
                m = min(min_dist, distancia(Puntos[i], Puntos[j]))
                if m < min_dist:
                    pi = Puntos[i]
                    pj = Puntos[j]
                    min_dist = m
    
    print(f'Distancia minima: {min_dist} entre los puntos {pi} y {pj}')

    return min_dist

def test():
    Puntos = generarPuntos(9) # Genero 2^9 puntos aleatorios
    pmcBasico(Puntos)
    pmcBasicoOptimizado(Puntos)

#test()