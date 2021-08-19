# Ejercicios de este Lin : http://patriciaemiguel.com/ejercicios/python/2019/03/10/ejercicios-buclewhile-python.html
total = 0
numeros = int(input("Numeros : "))

while numeros != 0 :
    total = numeros + total
    numeros = int(input("Numeros : "))
print(total)
    