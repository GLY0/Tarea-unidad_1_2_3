"""Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente."""

a=int(input("Mes(numero segun el orden del calendario):"))

if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("el mes tiene 31 dias")

elif a==2:
    print("el mes tiene 28 dias")

elif  a==4 or a==6 or a==9 or a==11:
    print("el mes tiene 30 dias")

else:
    print("incorrecto")