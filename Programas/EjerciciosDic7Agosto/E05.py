asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
creditos = 0

for curso, creditos in asignaturas.items():
    print(curso, " tiene ", creditos, " creditos.")
    creditos += creditos
print("Numero total de créditos del curso: ", creditos)