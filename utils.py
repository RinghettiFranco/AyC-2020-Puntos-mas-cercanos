from random import randint
from math import sqrt
import time

CX = 0
CY = 1 
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

# @brief Crea una franja en el plano que contiene puntos
# @param puntos Conjunto de puntos
# @param m Cota derecha de la franja
# @param d Cota izquierda de la franja
# @return Conjunto de puntos contenidos en la franja
def crearFranja(puntos, m, d):
    franja = list()
    for punto in puntos:
        if punto[CX] in (m-d, m+d):
           franja.append(punto)
    return franja 

# @brief Recorrido optimizado de la franja considerando los 7 puntos siguientes unicamente
# @param d
# @param franja
# @return 
def recorrer(franja):
    dist = INF
    pi = (-1,-1)
    pj = (-1,-1)
    for i in range(len(franja)):
        for j in range(i+1,min(i+7,len(franja))):
            distActual = distancia(franja[i],franja[j])
            if distActual < dist:
                dist = distActual
                pi = franja[i]
                pj = franja[j]
    return dist, pi, pj
    
def timer_function(function):
    def function_timer(*args, **kwargs):
        start = time.time_ns() 
        value = function(*args, **kwargs)
        end = time.time_ns() 
        runtime = end - start
        msg = "{func} tardó {time} nanosegundos en completar su ejecución."
        print(msg.format(func = function.__name__,time = runtime))
        return value
    return function_timer
