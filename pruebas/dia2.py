"""
    dia2
    Nombre: Luz Amairani Martinez Monroy
    Fecha: 03/02/2023
    Descripcion: Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde

"""

horas = float(input("Introduce tus horas de trabajo: "))
costo = float(input("Introduce lo que cobras por hora: "))
paga = horas * costo
print("Tu paga es", paga)