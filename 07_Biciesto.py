
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

anio=int(input("ingrese un año: "))
if biciesto(anio):
    print(f"el año {anio} es biciesto")
else:
    print(f"el año {anio} no es biciesto")
