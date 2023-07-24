##Escriba una función que muestre todos los números primos entre 1 y un número n que es ingresado por parámetro.
def primos(num):
    lista=[1]
    for i in range(2,num):
        contador=1
        divisor=2
        while divisor < i+1 and contador<3:
            if i % divisor == 0:
                contador+=1
            divisor+=1
        if contador==2:
            lista.append(i)
    print(lista)

n=int(input("ingrese un numero: "))
primos(n)    
