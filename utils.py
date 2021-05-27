from random import randint
from math import sqrt
import time

MAX = 10**9
INF = float('inf')

# @brief Generador de puntos aleatorios
# @param n Numero entero
# @return Lista con 2^n puntos aleatorios
def generarPuntos(n):
    puntos = list()
    for i in range(2**n):
        x, y = randint(0, MAX), randint(0, MAX)
        punto = (x, y)
        puntos.append(punto)
    return puntos

def ordenarPorX(puntos):
    return sorted(puntos, key = lambda x: x[0])

def ordenarPorY(puntos):
    return sorted(puntos, key = lambda y: y[1])

# @brief Calcula la distancia euclidea entre dos puntos
# @param punto1 Punto del plano (x, y)
# @param punto2 Punto del plano (x, y)
# @return Distancia entre puntos
def distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    x = (x2-x1)**2
    y = (y2-y1)**2
    return sqrt(x+y)

# @biref Toma los m primeros puntos del conjunto
# @param puntos Conjunto de puntos
# @param m Cota superior del intervalo
# @return Conjunto de puntos en el intervalo [0, m)
def aIzquierda(puntos, m):
    puntosAIzq = list()
    for punto in puntos: 
        if punto[0] < m:
            puntosAIzq.append(punto)
    return puntosAIzq

# @biref Toma los ultimos m puntos del conjunto
# @param puntos Conjunto de puntos
# @param m Cota inferior del intervalo
# @return Conjunto de puntos en el intervalo [m, max]
def aDerecha(puntos, m):
    puntosADer = list()
    for punto in puntos:
        if punto[0] >= m:
            puntosADer.append(punto)
    return puntosADer

# @brief Crea una franja en el plano que contiene puntos
# @param puntos Conjunto de puntos
# @param m Cota derecha de la franja
# @param d Cota izquierda de la franja
# @return Conjunto de puntos contenidos en la franja
def crearFranja(puntos, m, d):
    franja = list()
    for punto in puntos:
        if punto[0] in (m-d, m+d):
           franja.append(punto)
    return franja 

# @brief Ni idea, este se los dejo
# @param d
# @param franja
# @return 
def recorrer(d, franja):
    for punto1 in franja:
        for i in (1,7):
            punto2 = franja[franja.index(punto1)+i]
            ydiff = punto2[1] - punto1[1]
            if not ydiff > d and not ydiff==0:
                dist = distancia(punto2, punto1)
                if dist < d:
                    d = dist
    return d
    
def timer_function(function):
    def function_timer(*args, **kwargs):
        start = time.time()
        value = function(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func} took {time} seconds to complete its execution."
        print(msg.format(func = function.__name__,time = runtime))
        return value
    return function_timer
