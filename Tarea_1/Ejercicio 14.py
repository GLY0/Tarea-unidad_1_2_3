"""Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el 
propio número y se representa por el número seguido de un signo de exclamación."""

def factorial(d):
    productoria = 1
    for i in range(2, d+1):
        productoria *= i
    return productoria
print(factorial(3))