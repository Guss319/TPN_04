def rango(anio):
    lista=[]
    for i in range( anio, 2023):
         if biciesto(i):
             lista.append(i)
    print(f"Estos son los años biciestos entre {anio} y 2023 \n", lista)

def biciesto(anio):
    band=True
    if anio % 4 ==0:
        if anio % 100==0:
            if anio % 400==0:
                band=True
            else:
                band=False
        else:
            band=True
    else:
        band=False
    return band

anio=int(input("ingrese un año menor a 2023: "))
if anio<2023:
    rango(anio)
else:
    print("el año ingresado no es menor a 2023")