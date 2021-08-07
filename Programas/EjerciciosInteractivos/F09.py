# Ingreso datos
inversion     = float(input("Ingrese una cantidad a invertir: "))
interes_anual = float(input("Ingrese el interes anual (en porcentaje): "))
porcentaje_interes_anual = interes_anual / 100.0
n_años        = int(input("Ingrese la cantidad de años: "))

# Procesamiento
resultado = (inversion * (1.00 + porcentaje_interes_anual) ** n_años) / 10000.00
print(resultado)

# Resultado
print("El capital obtenido de su inversión es: "+ str(resultado))

# Solución Original.
# cantidad = float(input("¿Cantidad a invertir? "))
# interes = float(input("¿Interés porcentual anual? "))
# años = int(input("¿Años?"))
# print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))