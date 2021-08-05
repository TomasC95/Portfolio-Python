#vocales = ['a', 'e', 'i', 'o', 'u']
#palabra = input("Escriba una palabra para saber cuantas vocales contiene : ")

#for x in palabra:
#    if palabra == vocales[:]:
#        print("Su palabra contiene : " + vocales + " vocales. " )


word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")