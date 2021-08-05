lista = list(range (1,11))
lista_str = str(lista)[1:-1]
for x in lista:
    lista.sort(reverse = True)

print(lista_str)