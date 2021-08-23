frase = input("Ingresa una frase : ")
letra = input("Ingresa una letra para encontrar su posición : ")
i = 0

while (i != len(frase)):
    if (letra != frase[]):
        print("No se encontro la posición", i)
        i+1
    else:
        print("Se encontro en la posición", i)

    break


