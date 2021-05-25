from random import randint
from math import sqrt

max = 10**2

puntos = list()

def generarPuntos(n):
    for i in range(2**n):
        x,y = randint(0,max), randint(0,max)
        punto = (x,y)
        puntos.append(punto)


def ordenarPorY():
    puntos.sort(key = lambda y: y[1])

def calcularDistancia(punto1,punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    x = (x2-x1)**2
    y = (y2-y1)**2
    return sqrt(x+y)
    

    

