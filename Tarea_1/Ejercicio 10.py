"""Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” 
y “passwd#” se indica “Has entrado al sistema”, sino se da un error."""

nombre_de_usuario = input("ingresar el nombre de usuario")
contraseña = input("ingresar la contraseña")

if nombre_de_usuario == "pepe" and contraseña=="passwd#":
    print("has entrado al sistema")
else:
    print("error")