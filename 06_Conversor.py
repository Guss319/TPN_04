#Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir gramos a libras, centímetros a pulgadas y kilómetros a millas. 
#El programa debe permitir la conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462 libras = 1 gramo
def Convertir(dato,opcion):
    if opcion==1: #gramos a libra
        print (f"{dato} gramos = {dato*0.00220462} libras")
    else:
        if opcion==2: #libra a gramos
            print (f"{dato} libras = {dato/0.00220462} gramos")
        else:
            if opcion==3: #cm a pulgadas
                print (f"{dato} cm = {dato*0.393701} pulgadas")
            else:
                if opcion==4: #pulgadas a cm
                    print (f"{dato} pulgadas = {dato/0.393701} cm")
                else:
                    if opcion==5: #km a millas
                        print (f"{dato} km = {dato/1.60934} millas")
                    else:
                        if opcion==5: #millas a km
                            print (f"{dato} milla = {dato*1.60934} km")
        


opcion=int(input("Eliga una opcion: \n 1 gramos a libra \n 2 libra a gramos \n 3 cm a pulgadas \n 4 pulgadas a cm \n 5 km a millas \n 6 millas a km \n Opcion Nº "))
dato=float(input("ingrese el valor a convertir: "))
Convertir(dato,opcion)
    
