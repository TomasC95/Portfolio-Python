cesta = {}
continuar = True

while continuar:
    articulo = input('¿Qué artículo quieres introducir? ')
    precio = int(input('¿Qué precio tiene el artículo ingresado? '))
    cesta[articulo] = precio
    print(articulo)

    aux = input('¿Quieres añadir más articulos (Si/No)? ')
    if(aux == 'si'):
        continuar = True
    else:
        continuar = False

    continuar = input('¿Quieres añadir más articulos (Si/No)? ') == "Si"


{"Papa": 50, "Zanahoria":70}
costo = 0
print("Lista de la compra : ")
for articulo, precio in cesta.items():
    print(articulo, '\t', precio)
    costo += precio # costo = costo + precio
print("Costo total: ", costo)