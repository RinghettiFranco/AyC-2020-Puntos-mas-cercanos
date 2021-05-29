from utils import *
from pmcDyCAvanzado import *
from pmcBasico import *
from pmcDyC import *

#lista = generarPuntos(12)
#r1 = pmcBasico(lista)
#r2 = pmcBasicoOptimizado(lista)
#r3 = pmcDyC(lista)
#r4 = pmcDyCAvanzado(lista)
#print('Basico: ' + str(r1))
#print('Basico optimizado: ' + str(r2))
#print('Dividir y conquistar basico: ' + str(r3))
#print('Dividir y conquistar avanzado: ' + str(r4))

lista = []
print('--------------------------------------------------------------------')
for n in range(1,14):
    lista = generarPuntos(n)
    print('Para n = ' + str(n) + ' tal que #puntos=2^n:')
    r1 = pmcBasico(lista)
    print('Basico: ' + str(r1))
    r2 = pmcBasicoOptimizado(lista)
    print('Basico optimizado: ' + str(r2))
    r4 = pmcDyCAvanzado(lista)
    print('Dividir y conquistar avanzado: ' + str(r4))
    print('--------------------------------------------------------------------') 

