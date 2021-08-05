cuentas_cant = int(input("Cantidad de Cuentas a Realizar: "))
lista = list()

for x in range(cuentas_cant):
    base = int(input("Ingrese la base del ejercicio " + str(x+1) + " :"))
    exp  = int(input("Ingrese el exponente del ejercicio " + str(x+1) + " :"))
    resultado = base**exp
    lista.append(resultado)
    r_obtenido = int(input("Resultado Obtenido en Papel: "))
    #print(r_obtenido)
    if (r_obtenido == resultado):
        print("El resultado número " + str(x+1) + " es " + str(resultado),
        "Felicitaciones hiciste bien el ejercicio")
    else:
        print("El resultado obtenido en papel NO es correcto, volvé a intentarlo.")

    
