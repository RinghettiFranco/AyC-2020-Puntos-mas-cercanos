from math import *
import copy
import time
from pmcBasico import *
from utils import *
 
INF = float('inf')

def pmcRec(P, Q, n):
		
	if n <= 3:
		return pmcBasicoOptimizado(P)

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
	#franjaPorX.sort(key=lambda x:x[0])
	min_a = min(d, recorrer(franjaPorX))
	min_b = min(d, recorrer(franjaPorY))
	
	return min(min_a,min_b)

@timer_function
def pmcDyCComun(P):
	P.sort(key = lambda x: x[0])
	#Q = copy.deepcopy(P)
	#Q.sort(key = lambda y: y[1])
	return pmcRec(P, P, len(P))


