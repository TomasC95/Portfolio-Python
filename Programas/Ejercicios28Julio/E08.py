palabra = input("Ingrese una palabra para saber si es un palíndromo : ")

for x in palabra:
    if palabra == palabra[::-1]:
        print("Su palabra es un palíndromo!")
    else:
        print("Su palabra NO es un palíndromo!")