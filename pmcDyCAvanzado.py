import utils

def pmcDyCAvanzado(puntos):
    puntosOrdenadosX = utils.ordenarPorX(puntos)
    puntosOrdenadosY = utils.ordenarPorY(puntos)
    return masCercanos(puntosOrdenadosX,puntosOrdenadosY)

def masCercanos(puntosOrdenadosX:list,puntosOrdenadosY:list):
    if len(puntosOrdenadosX) <= 1:
        return utils.INF
    elif len(puntosOrdenadosX) == 2:
        return utils.distancia(puntosOrdenadosX[0], puntosOrdenadosX[1])
    else:
        medio = (len(puntosOrdenadosX)-1)//2
        puntoMedio = puntosOrdenadosX[medio]
        m = puntoMedio[0]
        puntosOrdenadosX1 = utils.aIzquierda(puntosOrdenadosX,m)
        puntosOrdenadosX2 = utils.aDerecha(puntosOrdenadosX,m)
        puntosOrdenadosY1 = list()
        puntosOrdenadosY2 = list()
        for punto in puntosOrdenadosY:
            if punto[0] < m:
                puntosOrdenadosY1.append(punto)
            else:
                puntosOrdenadosY2.append(punto)
        d1 = masCercanos(puntosOrdenadosX1,puntosOrdenadosY1)
        d2 = masCercanos(puntosOrdenadosX2,puntosOrdenadosY2) 
        d = min(d1,d2)
        franja = utils.crearFranja(puntosOrdenadosY,m,d)
        if franja:
            d3 = utils.recorrer(d,franja)
            return min(d,d3)
        else:
            return d


        

