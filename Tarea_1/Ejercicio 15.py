"""Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número entero por teclado. A continuación va pidiendo números y va respondiendo si el número a 
adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número"""

secreto = int(input("Numero secreto: "))

numero = int(input("numero: "))

while numero!=secreto:
    if numero>secreto:
        print("El numero es menor")
    else:
        print("El numero es mayor")
    numero = int(input("numero: "))
print("acertaste!!")

    
    
    