MAPAS ="""
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
"""


entrada = MAPAS
matriz  = entrada.split('\n')

lista_parcial = list()

'''
posicion = 0

for i in range(9):
    for j in range(10):
        if(entrada[posicion] != '\n'):
            lista_parcial.append(entrada[posicion])
            posicion = posicion + 1
    matriz.append(lista_parcial)
    lista_parcial.remove()


        #formo una lista con los 9 elementos de la fila
        #Sumo la lista a la super lista (matriz)
'''
        



matriz = [
        [0, 0, 3,  0, 2, 0,  6, 0, 0],
        [9, 0, 0,  3, 0, 5,  0, 0, 1],
        [0, 0, 1,  8, 0, 6,  4, 0, 0],
        [0, 0, 8,  1, 0, 2,  9, 0, 0],
        [7, 0, 0,  0, 0, 0,  0, 0, 8],
        [0, 0, 6,  7, 0, 8,  2, 0, 0],
        [0, 0, 2,  6, 0, 9,  5, 0, 0],
        [8, 0, 0,  2, 0, 3,  0, 0, 9],
        [0, 0, 5,  0, 1, 0,  3, 0, 0]]
    
vacio = None

for fila in range(9):
    for columna in range(9):
        if (matriz[fila][columna] == 0):
            matriz[fila][columna] = vacio
        print(matriz[fila][columna], end = ' ')
    print()