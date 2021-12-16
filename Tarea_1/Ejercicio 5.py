"""Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde."""

m= int(input("ingrese una cantidad determinada de minutos"))

def conversion():
    h = m//60
    M = m/60
    c = (M-h)*60
    b = int(c)
    print(m,"equivalea a",h,"horas con",b,"minutos")
conversion()