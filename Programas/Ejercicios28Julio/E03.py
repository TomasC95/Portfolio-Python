Materias = ["Matematica", "Psicologia", "Geografia", "Literatura", "Historia"]
Notas_Ingresadas = list()

for asignatura in (Materias):
    notas = input("Que nota has sacado en? " + asignatura + " : " )
    Notas_Ingresadas.append(notas)

for x in range(len(Notas_Ingresadas)):
    print("En " + Materias[x] + " has sacado un: " + Notas_Ingresadas[x])
    



    


    
