from multiprocessing import Process, current_process

from utils import *
from pmcDyCAvanzado import *
from pmcBasico import *
from pmcDyC import *

if __name__ == '__main__':
    problemas = 0
    f = open("debug.txt", "w")
    for w in range(0, 100):
        puntos = []
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        for n in range(1,14):
            puntos = generarPuntos(n)

            print(f'Para n = {n} tal que #puntos=2^n=2^{n}={2**n}:\n')
            r1 = pmcBasico(puntos)
            print(f'Resultado: {r1[0]} entre los puntos {r1[1]} y {r1[2]}\n')
            r2 = pmcBasicoOptimizado(puntos)
            print(f'Resultado: {r2[0]} entre los puntos {r2[1]} y {r2[2]}\n')
            r3 = pmcDyCSimple(puntos)
            print(f'Resultado: {r3[0]} entre los puntos {r3[1]} y {r3[2]}\n')
            r4 = pmcDyCAvanzado(puntos)
            print(f'Resultado: {r4[0]} entre los puntos {r4[1]} y {r4[2]}\n')

            if r3[0] != r4[0]:
                problemas += 1
                f.write(f'Problema con {r3} y {r4} en la vuelta {w} con n={n}')
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------') 
        for n in range(14,21):
            puntos = generarPuntos(n)
            print(f'Para n = {n} tal que #puntos=2^n=2^{n}={2**n}:\n')
            r3 = pmcDyCSimple(puntos)
            print(f'Resultado: {r3[0]} entre los puntos {r3[1]} y {r3[2]}\n')
            r4 = pmcDyCAvanzado(puntos)
            print(f'Resultado: {r4[0]} entre los puntos {r4[1]} y {r4[2]}\n')

            if r3[0] != r4[0]:
                problemas += 1
                f.write(f'Problema con {r3} y {r4} en la vuelta {w} con n={n}\n')
            print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(f'Iteracion {w} - Hubo {problemas} problemas\n')
    f.close()