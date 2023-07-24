def Calculadora(numeroA, numeroB, operacion):
    if operacion==1:
        print (f"{numeroA} + {numeroB} = {numeroA+numeroB}")
    else:
         if operacion==2:
            print (f"{numeroA} - {numeroB} = {numeroA-numeroB}")
         else:
             if operacion==3:
                print (f"{numeroA} * {numeroB} = {numeroA*numeroB}")
             else:
                  if operacion==4:
                    print (f"{numeroA} / {numeroB} = {numeroA/numeroB}")



numeroA=float(input("ingrese un numero: "))
numeroB=float(input("ingrese un numero: "))
operacion=int( input("Seleccione una operacion \n 1 para suma, 2 para resta \n 3 para multiplicacion 4 para division \n"))
Calculadora(numeroA, numeroB, operacion)
