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

    return min_dist     

def pmcRec(P, Q, n):
		
	if n <= 3:
		return algoritmoBasico(P)

	mitad = n // 2
	puntoMedio = P[mitad]
	Pl = P[:mitad]
	Pr = P[mitad:]
	dl = pmcRec(Pl, Q, mitad)
	dr = pmcRec(Pr, Q, n - mitad)
	d = min(dl, dr)
	franjaPorX = []
	franjaPorY = []
	x,_ = puntoMedio
	
	for i in range(n):
		x1,_ = P[i]
		x2,_ = Q[i]
		if abs(x1 - x) < d:
			franjaPorX.append(P[i])
		if abs(x2 - x) < d:
			franjaPorY.append(Q[i])

	franjaPorY.sort(key=lambda x:x[1])
	min_a = min(d, recorrer(franjaPorX))
	min_b = min(d, recorrer(franjaPorY))
	
	return min(min_a,min_b)

@timer_function
def pmcDyCComun(P):
	P.sort(key = lambda x: x[0])
	return pmcRec(P, P, len(P))


