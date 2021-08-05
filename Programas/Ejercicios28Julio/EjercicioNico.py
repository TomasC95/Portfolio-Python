# Registro de Vacunados por COVID-19
from statistics import mode

Identificaciones = list()
Dosis_Guardadas = list()
Edades = list()
Provincias = list()




for registro in range(1001):
    Identificacion = int(input("Número de ID : "))
    if Identificacion == 0:
        break
        continue
    Dosis = int(input("Número de Dosis (1-2) : "))
    while Dosis < 0 or Dosis > 2:
        Dosis = int(input("Error. Vuelve a ingresar el número de Dosis : "))
    Edad = int(input("Edad del paciente : "))
    Provincia = input("Provincia del paciente : ")
    Identificaciones.append(Identificacion)
    Dosis_Guardadas.append(Dosis)
    Edades.append(Edad)
    Provincias.append(Provincia)

print("La edad que mas vacunas recibió es : " + str(mode(Edades)))
print("La provincia que mas vacunas recibió es : " + str(mode(Provincias)))
print("La cantidad de personas que recibieron la 2da dosis es : " + str(mode(Dosis_Guardadas))) 
print("De " + str(len(Identificaciones)) + " personas ingresadas, un : " +  + " porciento completo el esquema.")

