from utils import *

@timer_function
def pmcDyCAvanzado(puntos):
    puntosOrdenadosX = ordenarPorX(puntos)
    puntosOrdenadosY = ordenarPorY(puntos)
    return masCercanos(puntosOrdenadosX,puntosOrdenadosY)

def masCercanos(puntosOrdenadosX:list,puntosOrdenadosY:list):
    if len(puntosOrdenadosX) <= 32:
        return algoritmoBasico(puntosOrdenadosX)
    else:
        medio = (len(puntosOrdenadosX))//2 - 1
        puntoMedio = puntosOrdenadosX[medio]
        m = puntoMedio[CX]
        puntosOrdenadosX1 = puntosOrdenadosX[:len(puntosOrdenadosX)//2]
        puntosOrdenadosX2 = puntosOrdenadosX[len(puntosOrdenadosX)//2:]
        puntosOrdenadosY1 = list()
        puntosOrdenadosY2 = list()
        for punto in puntosOrdenadosY:
            if punto[CX] < m or (punto[CX] == m and punto[CY]<puntoMedio[CY]):
                puntosOrdenadosY1.append(punto)
            else:
                puntosOrdenadosY2.append(punto)
        r1 = masCercanos(puntosOrdenadosX1,puntosOrdenadosY1)
        r2 = masCercanos(puntosOrdenadosX2,puntosOrdenadosY2) 
        if r1[0] < r2[0]:
            r = r1
        else:
            r = r2 
        franja = crearFranja(puntosOrdenadosY,m,r[0])
        r3 = recorrer(franja)
        if r3[0] < r[0]:
            r = r3
        return r

def algoritmoBasico(Puntos):
    min_dist = INF
    pi = (-1,-1)
    pj = (-1,-1)

    for i in range(0, len(Puntos)):
        for j in range(i, len(Puntos)):
            if i != j:
                m = min(min_dist, distancia(Puntos[i], Puntos[j]))
                if m < min_dist:
                    pi = Puntos[i]
                    pj = Puntos[j]
                    min_dist = m

    return min_dist, pi, pj       


