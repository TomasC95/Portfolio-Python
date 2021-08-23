
pregunta=True
while pregunta:
    print("""
    1.Iniciar Programa
    2.Imprimir Listado
    3.Finalizar Programa
    """)
    pregunta= input("What would you like to do? ")
    if pregunta=="1":
      print("\nBienvenido al Programa")
    elif pregunta=="2":
      print("\n Argentina, Brasil, Chile, Uruguay")
    elif pregunta=="3":
      print("\n Hasta pronto") 
      pregunta = None
    else:
       print("\n Elija una opción correcta 1, 2 o 3")