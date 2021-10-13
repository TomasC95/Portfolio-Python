import random 
from mapas import MAPAS

mapa_aleatorio = random.randrange(0,10)
entrada = MAPAS[1]
matriz = entrada.split('\n')
del matriz[0]
del matriz[-1]

posicion = len(matriz[0])

matriz_final        = [ ]
lista_parcial = list()

for l in range(9): 
    for i in matriz[l]:
        lista_parcial.append(int(i))
    matriz_final.append(lista_parcial)
    lista_parcial = []

print(matriz_final)