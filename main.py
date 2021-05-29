from utils import *
from pmcDyCAvanzado import *
from pmcBasico import *
from pmcDyC import *

lista = generarPuntos(6)
r1 = pmcBasico(lista)
r2 = pmcBasicoOptimizado(lista)
r3 = pmcDyC(lista)
r4 = pmcDyCAvanzado(lista)
print('Basico: ' + str(r1))
print('Basico optimizado: ' + str(r2))
print('Dividir y conquistar basico: ' + str(r3))
print('Dividir y conquistar avanzado: ' + str(r4))