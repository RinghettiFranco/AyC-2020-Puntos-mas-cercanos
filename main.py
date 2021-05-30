from utils import *
from pmcDyCAvanzado import *
from pmcBasico import *
from pmcDyC import *

puntos = []
print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
for n in range(1,14):
    puntos = generarPuntos(n)
    print('Para n = ' + str(n) + ' tal que #puntos=2^n=2^' + str(n) + '=' + str(2**n)  + ':')
    print()
    r1 = pmcBasico(puntos)
    print('Resultado: ' + str(r1[0]) + ' entre los puntos ' + str(r1[1]) + ' y ' + str(r1[2]))
    print()
    r2 = pmcBasicoOptimizado(puntos)
    print('Resultado: ' + str(r2[0]) + ' entre los puntos ' + str(r2[1]) + ' y ' + str(r2[2]))
    print()
    r3 = pmcDyCSimple(puntos)
    print('Resultado: ' + str(r3[0]) + ' entre los puntos ' + str(r3[1]) + ' y ' + str(r3[2]))
    print()
    r4 = pmcDyCAvanzado(puntos)
    print('Resultado: ' + str(r4[0]) + ' entre los puntos ' + str(r4[1]) + ' y ' + str(r4[2]))
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------') 
for n in range(14,21):
    puntos = generarPuntos(n)
    print('Para n = ' + str(n) + ' tal que #puntos=2^n=2^' + str(n) + '=' + str(2**n)  + ':')
    print()
    r3 = pmcDyCSimple(puntos)
    print('Resultado: ' + str(r3[0]) + ' entre los puntos ' + str(r3[1]) + ' y ' + str(r3[2]))
    print()
    r4 = pmcDyCAvanzado(puntos)
    print('Resultado: ' + str(r4[0]) + ' entre los puntos ' + str(r4[1]) + ' y ' + str(r4[2]))
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')