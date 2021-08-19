monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa: ")
if divisa.title() in monedas:
    print(monedas[divisa.title()])
else:
    print("La divisa no está.")