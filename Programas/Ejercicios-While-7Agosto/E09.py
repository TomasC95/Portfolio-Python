numeros = int(input("Igrese números positivos(0 para terminar) : "))

while (numeros != 0):
    numeros = int(input("Igrese números positivos(0 para terminar) : "))
    if(numeros % 2 == 0):
        print("Numero Par")
        numeros = int(input("Igrese números positivos(0 para terminar) : "))
    elif(numeros % 2 < 0 or numeros % 2 > 0):
        print("Numero Impar")
        numeros = int(input("Igrese números positivos(0 para terminar) : "))