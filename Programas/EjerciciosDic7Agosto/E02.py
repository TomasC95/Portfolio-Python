base_conocimiento = dict()

for i in range(70):
    nombre = input("Nombre : ")
    apellido = input("Apellido : ")
    edad = input("Edad : ")
    dic = {'Apellido' : apellido, 'Edad'   : edad}
    base_conocimiento[nombre] = dic

print(dic['Nombre'],dic['Apellido'], ' tiene', dic['Edad'], 'años')
