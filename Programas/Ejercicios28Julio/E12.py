# Ejercicio N°11 de este link https://aprendeconalf.es/docencia/python/ejercicios/bucles/

palabra = str(input("Escriba una palabra :  "))

for x in range(len(palabra),0,-1):
    print (palabra[x-1])

    