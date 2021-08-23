numeros = int(input("Números mayores que 1 : "))
cantidad = 0

while (numeros != 0):
    primos = True
    for x in range(2, numeros):
        if (numeros % x == 0) :
            primos = False
            break

    if(primos):
        cantidad += 1
    numeros = int(input("Números mayores que 1 : "))
    print("cantidad de números primos : ", cantidad )
    
