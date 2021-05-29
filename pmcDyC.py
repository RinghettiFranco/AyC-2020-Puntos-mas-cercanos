from math import *
import copy
import time
from pmcBasico import *
from utils import *
 
INF = float('inf')

def menorDistanciaFranja(franja, d):
	
	min_val = d
	size= len(franja)
	
	for i in range(size):
		j = i + 1
		_,yi= franja[i]
		if(j < size):_,yj= franja[j]
		else: yj = INF
		while j < size and (yj -
							yi) < min_val:
			min_val = dist(franja[i], franja[j])
			j += 1
			if(j < size):_,yj= franja[j]
			else: yj = INF
			

	return min_val

def puntosMasCercanosRec(P, Q, n):
		
	if n <= 3:
		return pmcBasico(P)

	mitad = n // 2
	puntoMedio = P[mitad]
	Pl = P[:mitad]
	Pr = P[mitad:]
	dl = puntosMasCercanosRec(Pl, Q, mitad)
	dr = puntosMasCercanosRec(Pr, Q, n - mitad)
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

	franjaPorX.sort(key=lambda x:x[1])
	min_a = min(d, menorDistanciaFranja(franjaPorX, d))
	min_b = min(d, menorDistanciaFranja(franjaPorY, d))
	
	return min(min_a,min_b)


def pmcDyC(P):
	P.sort(key = lambda x: x[0])
	Q = copy.deepcopy(P)
	Q.sort(key = lambda y: y[1])

	return puntosMasCercanosRec(P, Q, len(P))


