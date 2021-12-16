"""Realiza un programa que pida dos números ‘a’ y ‘b’ e indique si su suma es positiva, negativa o cero."""

while(True):
    a = int(input("ingrese un primer valor numerico")) 
    b = int(input("ingrese un segundo valor numerico"))
    c = a + b 
    print(c)
    0==0 
    if (c<0):
        print("la suma entre ambos numeros es negativa")
    elif (c>0): 
        print("la suma entre ambos numeros es positiva")
    elif (c==0):
        print("la suma entre ambos numeros es igual a 0")
    break