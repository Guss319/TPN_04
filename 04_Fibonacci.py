def Fibonacci(numero):
    lista=[0,1]
    tam=len(lista)
    i=0
    while tam < numero:
        agregar=lista[i]+lista[i+1]
        lista.append(agregar)
        i+=1
        tam=len(lista)
    return lista
valor=int(input("Ingrese un numero mayor a 1: "))
if valor>1:
    print(Fibonacci(valor))
