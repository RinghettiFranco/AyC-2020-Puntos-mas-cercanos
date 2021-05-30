from math import *
import copy
import time
from pmcBasico import *
from utils import *
 
INF = float('inf')

def algoritmoBasico(Puntos):
    min_dist = INF

    for i in range(0, len(Puntos)):
        for j in range(i, len(Puntos)):
            if i != j:
                m = min(min_dist, distancia(Puntos[i], Puntos[j]))
                if m < min_dist:
                    pi = Puntos[i]
                    pj = Puntos[j]
                    min_dist = m

    return min_dist, pi, pj     

def pmcDyC(P):
    n= len(P)
    if n <= 3:
       return algoritmoBasico(P)
       

    else:
        minDist = float('inf')
        mitad = n // 2
        xMedio, yMedio = P[mitad]
        pizq = P[:mitad]
        pder = P[mitad:]
        
        rIzq = pmcDyC(pizq)
        rDer = pmcDyC(pder)
        if rIzq[0] < rDer[0]:
            r = rIzq
        else:
            r = rDer 

        YN = list()

        Y = ordenarPorY(P)

        for i in range(len(Y)):
            x,_ = Y[i]
            if abs (x-xMedio) < minDist:
                YN.append(Y[i])
        
        r3 = recorrer(YN)
        if r3[0] < r[0]:
            r = r3

        return r

@timer_function
def pmcDyCSimple(P):
    Puntos = ordenarPorX(P)
    return pmcDyC (Puntos)






