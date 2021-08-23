cesta = {}
continuar = True

while continuar:
    palabra = input(' Palabra : ')
    traduccion = input(' Traducción : ')
    cesta[palabra] = traduccion
    print(palabra, ":", traduccion)
frase = input(" Ingresa una frase en español : ")
for i in frase.split():
    if i in cesta:
        print(cesta[i], end=' ')
    else:
        print(i, end=' ')
