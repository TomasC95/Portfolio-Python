frutas = {
        'platanos' : 1.35,
        'manzana' : 0.80,
        'pera' : 0.85,
        'naranja' : 0.70
         }


fruta = input("Que fruta desea? : ")
kilos = int(input("Cuantos Kilos necesita? :"))

if fruta in frutas:
    print(kilos, " Kilos de ", fruta, " valen ", frutas[fruta]* kilos, "$")
else:
    print("No tenemos ", fruta, " no esta disponible.")

    