import utils

def pmcDyCAvanzado(puntos):
    puntos = utils.ordenarPorX(puntos)
    return masCercanos(puntos,0,utils.MAX)

def masCercanos(puntos,ini,fin):
    cant = len(puntos)
    if cant == 1:
        return 0
    elif cant == 2:
        return utils.distancia(puntos[0], puntos[1])
    else:
        m = (ini+fin)//2
        puntos1 = utils.aIzquierda(puntos,m)
        puntos2 = utils.aDerecha(puntos,m)
        d1 = masCercanos(puntos1,ini,m)
        d2 = masCercanos(puntos2,m+1,fin) 
        d = min(d1,d2)
        franja = utils.crearFranja(puntos,2*d)
        d3 = utils.recorrer(franja)
        return min(d,d3)

