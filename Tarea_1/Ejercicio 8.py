""" Escribe un programa que lea un número e indique si es par o impar."""

while(True):
    y = int(input("introduzca un valor numerico:"))
    y=y%2
    if y==0:
        print("su numero es par")
    else:
        print("su numero es impar")
    break