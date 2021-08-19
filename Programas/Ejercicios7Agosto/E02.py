# Ejercicios de este Lin : http://patriciaemiguel.com/ejercicios/python/2019/03/10/ejercicios-buclewhile-python.html

positivos = 0
numeros = int(input("Numeros (0 para terminar): "))

while (numeros != 0) :
    if (numeros > 0):
        positivos = positivos +1
        numeros = int(input("Numeros (0 para terminar): "))
print(positivos)