kg = float(input("Ingrese su peso en KG con decimales: "))
estatura = float(input("Ingrese su estatura en Metros con decimales: "))
imc = kg / estatura**2

print("Su indice de masa corporal es: " + str(imc))