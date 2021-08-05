Materias = ["Matematica", "Psicologia", "Geografia", "Literatura", "Historia"]
Nota_Aprobacion = "6"
Repetir = []


for asignatura in (Materias):
    nota = input("Que nota obtuviste en " + asignatura + " : ")
    if(nota < Nota_Aprobacion):
        Repetir.append(asignatura)
    
print("Debes recursar las siguientes materias : " + ','.join(Repetir) + ". Suerte la proxima!")