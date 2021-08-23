libros = (input("Libro (* para terminar) : "))
lineas = 0
digitos = "123456789"
cantidadDigitos = 0

while (libros != "*"):
    for caracter in libros:
        if (caracter in digitos):
            cantidadDigitos += 1
    if (libros == "/"):
        lineas += 1
        print("Hay ", cantidadDigitos, " digitos numéricos en la linea.")
        cantidadDigitos = 0
    libros = (input("Libro : "))
print("Se leyeron ", lineas, " lineas completas.")

        