from random import randint
from math import sqrt

MAX = 10**9
INF = float('inf')

def generarPuntos(n):
    puntos = list()
    for i in range(2**n):
        x,y = randint(0,max), randint(0,max)
        punto = (x,y)
        puntos.append(punto)
    return puntos

def ordenarPorX(puntos):
    return puntos.sort(key = lambda x: x[0])

def ordenarPorY(puntos):
    return puntos.sort(key = lambda y: y[1])

def distancia(punto1,punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    x = (x2-x1)**2
    y = (y2-y1)**2
    return sqrt(x+y)

def aIzquierda(puntos,m):
    puntosAIzq = list()
    for i in range(0,m):
        puntosAIzq.append(puntos[i])
    return puntosAIzq

def aDerecha(puntos,m):
    puntosADer = list()
    for i in range(m,len(puntos)):
        puntosADer.append(puntos[i])
    return puntosADer

def crearFranja(puntos,m,d):
    franja = list()
    for i in puntos:
       if puntos[i][0] in (m-d,m+d):
           franja.append(puntos[i][0])
    return franja 

def recorrer(d,franja):
    for i in franja:
        for j in (i+1,len(franja)):
            ydiff = franja[j][1] - franja[i][1]
            if not ydiff > d:
                dist = distancia(franja[j],franja[i])
                if dist < d:
                    d = dist
    return d
    

