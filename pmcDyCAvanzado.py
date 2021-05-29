from utils import *
from pmcBasico import *

@timer_function
def pmcDyCAvanzado(puntos):
    puntosOrdenadosX = ordenarPorX(puntos)
    puntosOrdenadosY = ordenarPorY(puntos)
    return masCercanos(puntosOrdenadosX,puntosOrdenadosY)

def masCercanos(puntosOrdenadosX:list,puntosOrdenadosY:list):
    if len(puntosOrdenadosX) <= 16:
        return pmcBasicoOptimizado(puntosOrdenadosX)
    else:
        medio = (len(puntosOrdenadosX))//2 - 1 
        puntoMedio = puntosOrdenadosX[medio]
        m = puntoMedio[CX]
        puntosOrdenadosX1 = puntosOrdenadosX[:len(puntosOrdenadosX)//2]
        puntosOrdenadosX2 = puntosOrdenadosX[len(puntosOrdenadosX)//2:]
        puntosOrdenadosY1 = list()
        puntosOrdenadosY2 = list()
        for punto in puntosOrdenadosY:
            if punto[CX] < m:
                puntosOrdenadosY1.append(punto)
            else:
                puntosOrdenadosY2.append(punto)
        d1 = masCercanos(puntosOrdenadosX1,puntosOrdenadosY1)
        d2 = masCercanos(puntosOrdenadosX2,puntosOrdenadosY2) 
        d = min(d1,d2)
        franja = crearFranja(puntosOrdenadosY,m,d)
        d3 = recorrer(franja)
        return min(d,d3)


        

