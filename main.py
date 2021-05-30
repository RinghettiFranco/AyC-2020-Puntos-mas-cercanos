from utils import *
from pmcDyCAvanzado import *
from pmcBasico import *
from pmcDyC import *

puntos = []
print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
for n in range(1,5):
    puntos = generarPuntos(n)
    print('Para n = ' + str(n) + ' tal que #puntos=2^n=2^' + str(n) + '=' + str(2**n)  + ':')
    r1 = pmcBasico(puntos)
    print('Basico: ' + str(r1[0]) + ' entre los puntos ' + str(r1[1]) + ' y ' + str(r1[2]))
    r2 = pmcBasicoOptimizado(puntos)
    print('Basico optimizado: ' + str(r2[0]) + ' entre los puntos ' + str(r2[1]) + ' y ' + str(r2[2]))
    r3 = pmcDyCSimple(puntos)
    print('Dividir y conquistar simple: ' + str(r3[0]) + ' entre los puntos ' + str(r3[1]) + ' y ' + str(r3[2]))
    r4 = pmcDyCAvanzado(puntos)
    print('Dividir y conquistar avanzado: ' + str(r4[0]) + ' entre los puntos ' + str(r4[1]) + ' y ' + str(r4[2]))
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------') 

