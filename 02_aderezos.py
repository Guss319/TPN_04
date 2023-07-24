
def PedirAderezos():
    band= True
    while band:
        aderezos=(input("ingrese un aderezo para su sanguchito: ")).lower()
        
        if aderezos=="salir":
            band=False
        else:
            print ("el aderezo",aderezos,"fue agregado a su sanguchito")

PedirAderezos()

