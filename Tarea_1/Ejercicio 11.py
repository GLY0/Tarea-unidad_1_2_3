"""Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible 
por 4, pero no si es divisible por 100, excepto que también sea divisible por 400."""

year = int(input("año:"))

if 0==year%4 or 0!=year%100 and 0==year%400:
    print("este año es bisiesto")
else:
    print("error")