montos = float(input("Ingrese monto de compra (0 para terminar): $"))
total = 0

while (montos != 0):
    if (montos < 0):
        montos = float(input("Monto invalido, ingrese un monto mayor a 0 : $"))
    else:
        total  += montos
    montos = float(input("Ingrese monto de compra (0 para terminar): $"))
if (total > 1000):
    total -= total * 0.1
print("Monto total a pagar : $", total)    
