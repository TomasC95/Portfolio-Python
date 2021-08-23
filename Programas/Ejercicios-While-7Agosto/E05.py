num_par = 0
num = int(input("Ingrese los números (-1 para terminar): "))

while (num != -1):
    if(num%2 == 0):
        num_par += 1
    suma = 0
    while (num != 0):
        digito = num % 10
        suma += digito
        num=num // 10
    print("Suma de sus dígitos:", suma)
    num=int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron", num_par, "números pares")