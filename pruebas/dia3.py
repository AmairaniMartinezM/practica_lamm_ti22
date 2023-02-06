"""
    dia3
    Nombre: Luz Amairani Martinez Monroy
    Fecha: 05/02/2023
    Descripcion: Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

"""
nombre  = input("Introduce nombre de usuario: ")
numero = int(input("Introduce un numero entero: "))
print((nombre + "\n") * int(numero))
print("nombre de usuario:",nombre)
