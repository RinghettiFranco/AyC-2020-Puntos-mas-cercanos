from utils import *

@timer_function
def pmcDyCAvanzado(puntos):
    puntosOrdenadosX = ordenarPorX(puntos)
    puntosOrdenadosY = ordenarPorY(puntos)
    return masCercanos(puntosOrdenadosX,puntosOrdenadosY)

def masCercanos(puntosOrdenadosX,puntosOrdenadosY):
    if len(puntosOrdenadosX) <= 16:
        return algoritmoBasico(puntosOrdenadosX)
    else:
        n = len(puntosOrdenadosX)
        medio = n//2 - 1 
        puntoMedio = puntosOrdenadosX[medio]
        m = puntoMedio[CX]
        puntosOrdenadosX1 = puntosOrdenadosX[:n//2]
        puntosOrdenadosX2 = puntosOrdenadosX[n//2:]
        puntosOrdenadosY1 = list()
        puntosOrdenadosY2 = list()
        for punto in puntosOrdenadosY:
            if punto[CX] < m or (punto[CX]==m and punto[CY] < puntoMedio[CY]):
                puntosOrdenadosY1.append(punto)
            else:
                puntosOrdenadosY2.append(punto)
        d1 = masCercanos(puntosOrdenadosX1,puntosOrdenadosY1)
        d2 = masCercanos(puntosOrdenadosX2,puntosOrdenadosY2) 
        d = min(d1,d2)
        franja = crearFranja(puntosOrdenadosY,m,d)
        d3 = recorrer(franja)
        return min(d,d3)

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


