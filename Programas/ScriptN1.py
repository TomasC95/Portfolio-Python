lista = range(10)

for elemento in lista:
    continue
    #print(elemento) 


# Armemoslo un poco mas realista
for elemento in range(10):
    #print(elemento*2)
    print("Nicolas")

# Sumar 10 veces 2 a un numero
numero = int(input("Ingrese un numero: "))

for x in range(10):
    numero = numero + 2


lista_numeros = list()
# Ingresar tres numeros y calcular su raiz cuadrada
for x in range(3):
    numero = int(input("Ingrese el numero" + str(x+1) + " :"))
    lista_numeros.append(numero)
    resultado = numero**(1.0/2.0)
    print("El resultado " + str(x+1) + " es " + str(resultado))

print(lista_numeros)
print(lista_numeros.count(4))


 