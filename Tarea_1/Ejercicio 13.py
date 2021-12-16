"""Pedir un número por teclado y mostrar la tabla de multiplicar"""

x = int(input(" introdusca un valor numerico"))

text= "tabla de multiplicar del {}.. es" 
print(text.format(x))

for y in range(0,13):
    print(f"{x} * {y} = {x*y}")