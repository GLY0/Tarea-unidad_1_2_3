""" Calcular el perímetro y área de un círculo dado su radio."""

n = input("ingresa tu nombre:")
print("Hola",n)

while(True):
    print("""Elije una opcion
     1)Calcular el perimetro de un circulo"
     2) Calcular el area de un circulo"
     3) salir""")
    opcion = input()

    if opcion == "1":
        r = int(input("ingresa el valor del radio del circulo"))
        p = (2*3.14)
        print(p*r)
        

    elif opcion == "2":
        R = int(input("ingresar el valor del radio del circulo"))
        a = 3.14
        print(a*R**2)

    elif opcion == "3":
        print("Gracias por visitarnos",n,"=D")
        break    