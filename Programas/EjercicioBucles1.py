cuentas_cant = int(input("Cantidad de Cuentas a Realizar: "))
lista = list()

for x in range(cuentas_cant):
    base = int(input("Ingrese la base del ejercio " + str(x+1) + " :"))
    exp  = int(input("Ingrese el exponente del ejercicio " + str(x+1) + " :"))
    resultado = base**exp
    lista.append(resultado)
    print("El resultado número " + str(x+1) + " es " + str(resultado))


    

    
   

    
