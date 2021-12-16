"""Escribir un programa que pregunte al usuario su nombre, y luego lo salude."""

print("como te llamas?")
x = input("escribe tu nombre aqui..")
text = "Un gusto saludarte {} !!"
print(text.format((x)))