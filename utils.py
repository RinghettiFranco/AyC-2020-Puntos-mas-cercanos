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
    


#cmd = ""
#print("Para salir presione 0.")
#print("Para generar puntos  presione 1.")
#print("Para ordenarlos por su coordenada y presione 2.")
#while cmd != "0":
#    cmd = input("¿Qué desea hacer?: ")
#    if cmd == "1":
#        n = input("Seleccione el exponente: ")
#        generarPuntos(int(n))
#        print(puntos)
#    elif cmd == "2":
#        ordenarPorY()
#        print(puntos)

punto1 = (4,1)
punto2 = (7,5)
print(calcularDistancia(punto1,punto2))
    

