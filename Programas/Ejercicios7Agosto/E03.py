mayor = -1
num = int(input("Numeros Positivos (0 para terminar : "))

while (num != 0 and num > 0):
    num = int(input("Numeros Positivos (0 para terminar) : "))
    if (num >= mayor):
        mayor=num
print("Mayor numero ingresado : ", mayor)