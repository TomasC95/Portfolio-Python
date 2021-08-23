
meses = {
  1: 'Enero' , 2 : 'Febrero',
  3 : 'Marzo',4 :'Abril' , 
  5 : 'Mayo', 6: ' Junio',
  7 : 'Julio', 8: 'Agosto' ,
  9 : 'Septiembre', 10: 'Octubre',
  11 :'Noviembre', 12: 'Diciembre'
}

dia = int(input("Día : "))
mes = int(input("Número del mes : "))
año = int(input("Año : "))

print("La feceha ingresada es ", dia,"/", meses[mes] , "/", año )