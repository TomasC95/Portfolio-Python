suma = 0
digitos = 0
num = int(input("Numero Positivo :"))

while (num != 0):
    digitos = num % 10
    num //= 10
    suma += digitos
    
print("Suma de los digitos: {} ".format(suma))

