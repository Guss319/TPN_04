def multiplo3(numero):
    if numero % 3==0:
        return True
def multiplo5(numero):
    if numero % 5==0:
        return True
suma=0
for i in range(1,1000):
    band3=multiplo3(i)
    band5=multiplo5(i)
    if band3 or band5:
        suma=suma+i
print("La suma de todos los mmultiplos entre 1 y 1000 es: ", suma)
        
    

