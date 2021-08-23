#Solucion

persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
    

while (1):
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    contenedor = input('¿Quieres añadir más información (Si/No)? ')        #S I
    contenedor = contenedor.lower()                                        #s i 
    contenedor = contenedor.strip()                                        #si
    if(contenedor == "si" or contenedor == "yes"):
        break