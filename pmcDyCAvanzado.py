import utils

def pmcDyCAvanzado(puntos):
    puntosOrdenadosX = utils.ordenarPorX(puntos)
    puntosOrdenadosY = utils.ordenarPorY(puntos)
    return masCercanos(puntosOrdenadosX,puntosOrdenadosY,0,utils.MAX)

def masCercanos(puntosOrdenadosX:list,puntosOrdenadosY:list, ini:int,fin:int):
    if len(puntosOrdenadosX) <= 1:
        return utils.INF
    elif len(puntosOrdenadosX) == 2:
        return utils.distancia(puntosOrdenadosX[0], puntosOrdenadosX[1])
    else:
        m = (ini+fin)//2
        puntosOrdenadosX1 = utils.aIzquierda(puntosOrdenadosX,m)
        puntosOrdenadosX2 = utils.aDerecha(puntosOrdenadosX,m)
        puntosOrdenadosY1 = list()
        puntosOrdenadosY2 = list()
        for i in range(ini,fin):
            if puntosOrdenadosY[i] in puntosOrdenadosX1:
                puntosOrdenadosY1.append(puntosOrdenadosY[i])
            else:
                puntosOrdenadosY2.append(puntosOrdenadosY[i])
        d1 = masCercanos(puntosOrdenadosX1,puntosOrdenadosY1,ini,m)
        d2 = masCercanos(puntosOrdenadosX2,puntosOrdenadosY2,m+1,fin) 
        d = min(d1,d2)
        franja = utils.crearFranja(puntosOrdenadosY,m,d)
        d3 = utils.recorrer(d,franja)
        return min(d,d3)

puntos = [(1,1), (2,2), (4,4), (8,8), (16,16), (32,32)]
resultado = pmcDyCAvanzado(puntos)
print(resultado)
