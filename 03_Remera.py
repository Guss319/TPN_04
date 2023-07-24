def Hacer_Remera(tam, mensaje):
    print("El tamaño de la remera es:", tam," y tiene la siguiente frase: ", mensaje)

def Remera_Grande(tam="L",mensaje="me gusta python"):
    print("el tamaño es:", tam, "y el mensaje es: ", mensaje)


talle=input("ingrese un talle: ").upper()
frase=input("ingrese una frase: ").upper()
Hacer_Remera(talle, frase)
Hacer_Remera(mensaje=frase,tam=talle )
Remera_Grande(frase)
Remera_Grande()
