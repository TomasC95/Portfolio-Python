cesta = {}
continuar = True

while continuar:
    articulo = input('¿Qué artículo quieres introducir? ')
    precio = input('¿Qué precio tiene el artículo ingresado? ')
    cesta[articulo] = precio
    print(articulo)
    continuar = input('¿Quieres añadir más articulos (Si/No)? ') == "Si"
costo = 0
print("Lista de la compra : ")
for articulo, precio in cesta.items():
    print(articulo, '\t', precio)
    costo += precio
print("Costo total: ", costo)