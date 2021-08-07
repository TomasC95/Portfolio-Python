cuentas_cant = int(input("Cantidad de Cuentas a Realizar: "))
resultados_correctos = list()
resultados_alumno    = list()

porcentaje_aprobacion = 0.6
ejercicios_aprobados = 0

for x in range(cuentas_cant):
    base = int(input("Ingrese la base del ejercicio " + str(x+1) + " :"))
    exp  = float(input("Ingrese el exponente del ejercicio " + str(x+1) + " :"))
    resultado = base**exp
    resultados_correctos.append(resultado)
    r_obtenido = float(input("Resultado Obtenido en Papel: "))
    resultados_alumno.append(r_obtenido)
    if (r_obtenido == resultado):
        ejercicios_aprobados = ejercicios_aprobados + 1
        print("El resultado número " + str(x+1) + " es " + str(resultado),
        "Felicitaciones hiciste bien el ejercicio")
    else:
         print("El resultado obtenido en papel NO es correcto, volvé a intentarlo.")

# print(resultados_alumno) #Opcion mas para nosotros

numero_resultado = 1
for x in resultados_alumno:
    print("Resultado N" + str(numero_resultado) +   " = " + str(x) )
    numero_resultado = numero_resultado + 1

validacion = int(input("Acepta los resultados ingresados? Ingrese 1 por si y 0 por no"))
if(validacion == 1):
    if((ejercicios_aprobados/cuentas_cant) >= porcentaje_aprobacion):
        print("Felicitaciones, aprobaste!")
    else:
        print("Una lastima... recupera..!") 
else:
    print("Resultados descartados...")






    
    
    
