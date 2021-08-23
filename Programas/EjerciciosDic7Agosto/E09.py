# Diccionario 
facturas_pendientes = dict()    # Etiqueta ==> Nro Factura
                                # Valor    ==> Costo

def Imprimir_menu():
    print("\t\tMenu")
    print("1 ==> Anadir nueva factura")
    print("2 ==> Pagar una factura existente")
    print("3 ==> Terminar")    

while(True):
    Imprimir_menu()
    menu = int(input("Ingrese comando:"))
    #Filtro las opciones incorrectas
    if(menu < 1 or menu > 3):
        continue
    #Procesamiento
    if(menu == 1):
        #Solicito datos de la factura
        nro = int(input("Ingrese el numero de factura:"))
        val = int(input("Ingrese el importe de la factura:"))
        if(nro < 0 or val < 0):
            print("Factura invalida!")
            continue
        #Guardamos la factura
        facturas_pendientes[nro] = val
    elif(menu == 2):
        #Solicito el numero de factura
        nro = int(input("Ingrese el numero de factura:"))
        #¿Tengo la factura en mi base de conocimiento?
        if(nro is facturas_pendientes.titles()):
            #Pagar la factura
            del facturas_pendientes(nro)
        else:
            print("La factura no se encuentra en los registros!")
            continue
    elif(menu == 3):
        print("Gracias por utilizar el sistema.. :D")
        break
        
    


