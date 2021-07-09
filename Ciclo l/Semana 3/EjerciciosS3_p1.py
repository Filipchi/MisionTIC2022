import os
os.system("cls")

# Ejercicios de aplicación estructura iterativa while:

# 1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

# print(f"\n\t 1. Determina notas mayores/menores a 7 de un listado de 10 alumnos")
# print(f"\n\t\t Ingrese las 10 notas: ")

def notas(): 
    i = 0; mayores = 0; menores = 0
    while ( i < 2):
        nota = float(input(f"\t\t\t Nota {i+1}:  "))
        if (nota < 7):
            menores += 1
        else:
            mayores += 1
        i += 1

    return f"\n\t\t Hay {mayores} alumno(s) con nota mayor o igual a 7 \n\t\t Hay {menores} alumno(s) con notas menores a 7 \n"

# print(notas())

# os.system("pause")
# os.system("cls")

# 2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
k2 = 0
print(f"\n\t 2. Determina el promedio de n alturas definidas")
while (k2 == 0):
    cantidad = int(input(f"\n\t\t Ingrese el número de alturas a validar [en cm]:  "))
    if (cantidad > 10):
        print(f"\n\t\t La cantidad ingresada supera la esperada, intente de nuevo \n")
    else:
        break

def alturas(cantidad_f):
    i = 0; suma = 0
    while (i < cantidad_f):
        persona = int(input(f"\t\t\t Altura {i+1}:  "))
        suma += persona
        i += 1

    promedio = suma / cantidad_f

    return f"\n\t\t La altura promedio de las {cantidad} personas validadas es de {round(promedio, 2)} cm \n"

# print(alturas(cantidad))

# os.system("pause")
# os.system("cls")

# 3. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar  un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

print(f"\n\t 3. Informa los sueldos que cobra cada empleado")
numeroEmpleados = int(input(f"\n\t\t Ingrese el número de empleados a validar:  "))

def sueldoEmpleados(nEmpleados_f):
    i = 0; sueldoEntre = 0; sueldoMayor = 0; importe = 0
    while (i < nEmpleados_f):
        sueldo = float(input(f"\t\t\t Ingrese el sueldo del Empleado No.{i+1}:  "))
        if(sueldo < 100 or sueldo > 500):
            print(f"\n\t\t EL VALOR DIGITADO NO CUMPLE CON LOS CRITERIOS DEL SUELDO, intente nuevamente \n")
            continue

        if (sueldo <= 300):
            sueldoEntre += 1
        else:
            sueldoMayor += 1
        i += 1
        importe += sueldo

    return f"\n\t\t {sueldoEntre} Empleados cobran entre $100 y $300 \n\t\t {sueldoMayor} Empleados cobran mas de $300 \n\n\t\t El importe total en sueldos al personal es de ${importe} \n"

# print(sueldoEmpleados(numeroEmpleados))

# os.system("pause")
# os.system("cls")

# 4. Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)

print(f"\n\t 4. Imprime 25 términos de la serie 11 - 22 - 33 - 44 - etc. \n")
def imprime4 ():
    i4 = 0
    while (i4 < 25):
        print(f"\t\t ({i4 + 1}).  {(i4 + 1) * 11}. ")
        i4 += 1

    return f"\n\t\t Última Iteración:  {i4} \n"

# print(imprime4())

# os.system("pause")
# os.system("cls")

# 5. Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.

print(f"\n\t 5. Imprime los múltiplos de 8 hasta el valor 500. \n")
def imprime5 ():
    i5 = 1
    while (i5 <= 500):
        if ((i5 % 8) == 0):
            print(str(i5), end=" - ")
        i5 += 1
    return "fin"
print(imprime5())

os.system("pause")
os.system("cls")

# 6. Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales"). Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.



# 7. Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares. 
# Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1): if valor%2==0:

print(f"\n\t 3. Informa los sueldos que cobra cada empleado")
numeroEmpleados = int(input(f"\n\t\t Ingrese el número de empleados a validar:  "))

