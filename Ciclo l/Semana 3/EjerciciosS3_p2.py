import os
import numpy as np
os.system("cls")

# Ejercicios de aplicación estructura iterativa for:

# 8. Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. 
# El programa deberá informar:

#        a) De cada triángulo la medida de su base, su altura y su superficie.
#        b) La cantidad de triángulos cuya superficie es mayor a 12.

print(f"\n\t 8. Determina la superficie de un triangulo a partir de la base y altura ingresadas")
k8 = 0
while (k8 == 0):
    parejas = int(input(f"\n\t\t Ingrese el número de parejas de datos:  "))
    if (parejas > 5):
        print(f"\n\t\t La cantidad ingresada supera la esperada, intente de nuevo \n")
    else:
        break

# Bases = []
# Alturas = []
# Posicion = []
# Superficie = []

# def Triangulos(datos_parejas):
#     for x in range(datos_parejas):
#         print(f"\n\t\t Ingrese la información de la pareja {x+1} en cm")
#         base = int(input("\t\t\t Base [cm]:  "))
#         altura = int(input("\t\t\t Altura [cm]:  "))
#         Superficie.append((base * altura) / 2)
#         Posicion.append(x+1)
#         Bases.append(base)
#         Alturas.append(altura)

#     print("\n\n\t\t________________________________________________")
#     print("\n\t\t|  No.  |    Bases   |  Alturas   | Superficie |")
#     print("\t\t________________________________________________")
#     contador = 0
#     for Pos1, Bases1, Alturas1, Super1  in zip(Posicion, Bases, Alturas, Superficie):
#         print('\t\t|  {:^4} | {:^10} | {:^10} | {:^10} |'.format(Pos1, Bases1, Alturas1, Super1))
#         if(Super1 > 12):
#             contador +=1

#     return f"\n\n\t\t Hay {contador} triangulo(s) con superficie mayor a 12 \n\n"

# print(Triangulos(parejas))

# os.system("pause")
# os.system("cls")

# 9. Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

# print(f"\n\t 9. Imprime la suma de los últimos 5 valores ingresados")
# print(f"\n\t\t Ingrese a continuación 10 npumeros a validar")
# numeros = []
# nueva = []
# def Suma(lista_numeros = 10):
#     for x in range(lista_numeros):
#         num = int(input(f"\t\t\t Número {x+1}:  "))
#         numeros.append(num)
#         nueva = numeros[-5::]

#     print(f"\n\t\t Lista creada:\t {numeros}")
#     print(f"\n\t\t Lista extraida:\t {nueva}\n")
#     suma_lista = 0

#     for x in nueva:
#         suma_lista += x

#     return f"\n\t\t La suma de los 5 últimos valores ingresados es {suma_lista}"

# print(Suma())

# os.system("pause")
# os.system("cls")

# 10. Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)

# print(f"\n\t 10. Imprime la tabla de multiplicar del 5 hasta el número 50")
# print(f"\n\t\t Ingrese un número del 1 al 10")
# cinco = []
# def Tabla_del_5(fin = 51):
#     print("\n\n\t\t\t____________________________")
#     for x in range(fin):
#         cinco.append(x*5)
#         print('\t\t\t|   5   *  {:^4}   =  {:^5} |'.format(x, cinco[x]))
#     print("\t\t\t----------------------------\n\n")
                 
#     return cinco
# Tabla_del_5()

# os.system("pause")
# os.system("cls")

# 11. Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la
# tabla de multiplicar del mismo (los primeros 12 términos)
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.
# print(f"\n\t 11. Imprime la tabla de multiplicar de un número seleccionado del 1 al 10 ")
# k11 = 0
# while (k11 == 0):
#     numero11 = int(input(f"\n\t\t Ingrese el número del 1 al 10 a validar:  "))
#     if (numero11 > 10):
#         print(f"\n\t\t La cantidad ingresada supera la esperada, intente de nuevo \n")
#     else:
#         break

# mult = []
# def Tabla_mult(fin = 13):
#     print("\t\t\t\t________________________")
#     for x in range(fin):
#         mult.append(x*numero11)
#         print(f"\t\t\t\t| {numero11}", "  *  {:^4}  =  {:^4} |".format(x, mult[x]))
#     print("\t\t\t\t------------------------\n")

#     return mult
# Tabla_mult()

# os.system("pause")
# os.system("cls")

# 12. Realizar un programa que lea los lados de n triángulos, e informar:
#       a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), 
#          isósceles (dos lados iguales), o escaleno (ningún lado igual)
#       b) Cantidad de triángulos de cada tipo.

# print(f"\n\t 12. Imprime el tipo de triangulo según sus lados (equilatero, isósceles, escaleno)")
# k12 = 0
# while (k12 == 0):
#     numero12 = int(input(f"\n\t\t Ingrese el número de triangulos a validar:  "))
#     if (numero12 > 5):
#         print(f"\n\t\t La cantidad ingresada supera la esperada, intente de nuevo \n")
#     else:
#         break

# Lado1 = []; Lado2 = []; Lado3 = []; Tipo = []; Posicion = []
# def lado_triangulos(cantidad):
#     cant_escaleno = 0; cant_isosceles = 0; cant_equilatero = 0 
#     print(f"\n\t\t Ingrese los valores de cada lado del triangulo")
#     for x in range(cantidad):
#         print(f"\n\t\t\t Triangulo {x+1}:")
#         lado1 = float(input("\t\t\t\t Lado 1:  "))
#         lado2 = float(input("\t\t\t\t Lado 2:  "))
#         lado3 = float(input("\t\t\t\t Lado 3:  "))
#         if (lado1 == lado2 == lado3):
#             Tipo.append("Equilatero")
#             cant_equilatero += 1
#         elif ((lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3)):
#             Tipo.append("Escaleno")
#             cant_escaleno += 1
#         else:
#             Tipo.append("Isósceles")
#             cant_isosceles += 1

#         Lado1.append(lado1)
#         Lado2.append(lado2)
#         Lado3.append(lado3)  
#         Posicion.append(x) 

#     print("\n\n\t\t____________________________________________________________")
#     print("\t\t|  No.  |   Lado 1   |   Lado 2   |   Lado 3   |    Tipo    |")
#     print("\t\t____________________________________________________________")

#     for Pos1, L1, L2, L3, Tipos  in zip(Posicion, Lado1, Lado2, Lado3, Tipo):
#         print('\t\t|  {:^4} | {:^10} | {:^10} | {:^10} | {:^10} |'.format(Pos1+1, L1, L2, L3, Tipos))

#     mensaje = print(f"\n\n\t\t\tTriangulos Equilateros:  {cant_equilatero}",
#           f"Triangulos Isósceles:  {cant_isosceles}", f"Triangulos Escalenos:  {cant_escaleno} \n\n", sep="\n\t\t\t")
#     return mensaje

# lado_triangulos(numero12)
# os.system("pause")
# os.system("cls")

# 13. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
#     Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. 
#     Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

print(f"\n\t 12. Determina el cuadrante en el plano cartesiano de una pareja de números (x,y) ingresados")
k13 = 0
while (k13 == 0):
    numero13 = int(input(f"\n\t\t Ingrese el número parejas de coordenadas a validar:  "))
    if (numero13 > 5):
        print(f"\n\t\t La cantidad ingresada supera la esperada, intente de nuevo \n")
    else:
        break
Datosx = []
Datosy = []
Cuadrantes = []
Posicion = []
def coordenada(cantidad):
    cuadrante1 = 0
    cuadrante2 = 0
    cuadrante3 = 0
    cuadrante4 = 0
    sobre_eje = 0
    print(f"\n\t\t Ingrese el valor de cada punto")
    for x in range(cantidad):
        print(f"\n\t\t\t Coordenada {x+1}:")
        puntox = float(input("\t\t\t\t Punto x:  "))
        puntoy = float(input("\t\t\t\t Punto y:  "))
        if (puntox > 0 and puntoy > 0):
            Cuadrantes.append("Cuadrante 1")
            cuadrante1 += 1
        elif (puntox < 0 and puntoy > 0):
            Cuadrantes.append("Cuadrante 2")
            cuadrante2 += 1
        elif (puntox < 0 and puntoy < 0):
            Cuadrantes.append("Cuadrante 3")
            cuadrante3 += 1
        elif (puntox > 0 and puntoy < 0):
            Cuadrantes.append("Cuadrante 4")
            cuadrante4 += 1
        elif (puntox == 0 or puntoy == 0):
            Cuadrantes.append("Sobre el eje")
            sobre_eje += 1
        
        Datosx.append(puntox)
        Datosy.append(puntoy)
        Posicion.append(x)

    print("\n\n\t\t_____________________________________________________")
    print("\t\t|  No.  |  Puntos x  |  Puntos y  |     Cuadrante    |")
    print("\t\t_____________________________________________________")

    for Pos1, Px, Py, Cuad in zip(Posicion, Datosx, Datosy, Cuadrantes):
        print('\t\t|  {:^4} | {:^10} | {:^10} |   {:^12}   |'.format(Pos1+1, Px, Py, Cuad))

    mensaje = print(f"\n\n\t\t\tCuadrante 1:   {cuadrante1} punto(s)", f"Cuadrante 2:   {cuadrante2} punto(s)",
                    f"Cuadrante 3:   {cuadrante3} punto(s)", f"Cuadrante 4:   {cuadrante4} punto(s)",
                    f"Sobre el Eje:  {sobre_eje} punto(s) \n\n", sep="\n\t\t\t")
    return mensaje

coordenada(numero13)
os.system("pause")
os.system("cls")

# 14. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#       a) La cantidad de valores ingresados negativos.
#       b) La cantidad de valores ingresados positivos.
#       c) La cantidad de múltiplos de 15.
#       d) El valor acumulado de los números ingresados que son pares.



# 15. Se cuenta con la siguiente información:
#       Las edades de 5 estudiantes del turno mañana.
#       Las edades de 6 estudiantes del turno tarde.
#       Las edades de 11 estudiantes del turno noche.
#       Las edades de cada estudiante deben ingresarse por teclado.
#           a) Obtener el promedio de las edades de cada turno (tres promedios)
#           b) Imprimir dichos promedios (promedio de cada turno)
#           c) Mostrar por pantalla un mensaje que indique cuál de los tres turnos tiene un promedio de edades mayor.
