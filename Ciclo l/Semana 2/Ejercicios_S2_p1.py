import os
os.system("cls")

#               Ejercicios Semana 2_ Parte 1

numero = int(input(f"\n\tIngrese un numero entero:\t"))

#   1. Leer un número entero y determinar si es un número terminado en 4.

if (numero % 10 == 4):
    print(f"\n\t1 - El numero {numero} termina en 4")
else:
    print(f"\n\t1 - El numero {numero} NO termina en 4")

#   2. Leer un número entero y determinar si tiene 3 dígitos.

if ((numero < 1000) & (numero > 99)):
    print(f"\n\t2 - El numero {numero} tiene 3 dígitos")
else:
    print(f"\n\t2 - El numero {numero} NO tiene 3 dígitos")

#   3. Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

if ((numero < 10) or (numero > 99)):
    print(f"\n\t3 - El numero {numero} No es de 2 dígitos")
elif ((((int(numero % 10) % 2)) == 0) & (((int(numero / 10) % 2)) == 0)):
    print(f"\n\t3 - El numero {numero} tiene ambos digitos pares")
else:
     print(f"\n\t3 - El numero {numero} NO tiene ambos digitos pares")

#   4. Leer un número entero de dos dígitos menor que 20 y determinar si es primo.

#   5. Leer un número entero de dos dígitos y determinar si es primo y además       
#      si es negativo.

def punto5():
    num5 = 0
    divisores = 0
    i = 0
    respuesta = ""
    while (num5 == 0):
        num5 = int(input(f"\n\t\t Ingrese el número de 2 digitos a validar:  "))
        if ((num5 < 10) or (num5 > 99)):
            print(f"\n\t\t La cantidad ingresada supera la esperada, intente de nuevo \n")
        else:
            break
    while (i <= num5):
        if (num5 % i == 0):
            divisores += 1
        i += 1

    if(num5 < 0 and divisores == 2):
        respuesta = f"{num5} es un número primo negativo"
    elif(num5 < 0 and divisores == 2):
        respuesta = f"{num5} No es un número primo negativo"
    
    return respuesta

print(punto5())


    

#   6. Leer un número entero de dos dígitos y determinar si los dos dígitos 
#      son iguales.

if ((numero < 10) or (numero > 99)):
    print(f"\n\t6 - El numero {numero} No es de 2 dígitos\n")
elif (int(numero % 10) == int(numero / 10)):
    print(f"\n\t6 - El numero {numero} tiene ambos digitos iguales\n")
else:
    print(f"\n\t6 - El numero {numero} tiene digitos diferentes\n")

#   7. Leer dos números enteros y determinar cuál es el mayor.

num1 = int(input(f"\n\tIngrese el primer numero entero:\t"))
num2 = int(input(f"\n\tIngrese el segundo numero entero:\t"))

if (num1 > num2):
    print(f"\n\t6 - {num1} es MAYOR a {num2}")
elif (num1 < num2):
    print(f"\n\t6 - {num2} es MAYOR a {num1}")
elif (num1 == num2):
    print(f"\n\t6 - Los numeros {num1} y {num2} son iguales")

#   8. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la  
#      suma de todos los dígitos.

if ((num1 < 10) or (num2 > 99) and (num1 < 10) or (num2 > 99)):
    print(f"\n\t8 - El numero {numero} No es de 2 dígitos\n")
else:
    def suma(num_1: int, num_2: int):
        sum= num_1 + num_2
        return  sum
    
    print(f"\n\t8 - La suma entre {num1} y {num2} es {suma(num1, num2)}")

#   9. Leer un número entero de tres dígitos y determinar en qué posición está el 
#      mayor dígito.
num9 = int(input(f"\n\tIngrese un numero entero de 3 digitos:\t"))

if ((num9 < 100) or (num9 > 999)):
    print(f"\n\t8 - El numero {num9} No es de 3 dígitos\n")
else:
    A = int(num9/100)
    B = int(num9/10) % 10
    C = num9 % 10

    print(f"\n\t\t1er Posición:\t {A} \n\t\t2da Posición:\t {B} \n\t\t3er Posición:\t {C}")
    if ((A > B) and (A > C)):
        print(f"\n\t9 - El MAYOR DIGITO se encuentra en la 1er Posición\n")
    elif ((A < B) and (B > C)):
        print(f"\n\t9 - El MAYOR DIGITO se encuentra en la 2da Posición\n")
    else:
        print(f"\n\t9 - El MAYOR DIGITO se encuentra en la 3er Posición\n")


#  10. Leer un número entero de tres dígitos y determinar si algún dígito es    
#      múltiplo de los otros.

    if ((B % A == 0) and (C % A == 0)):
        print(f"\n\t10 - {A} es multiplo de {B} y {C}\n")
    elif ((A % B == 0) and (C % B == 0)):
        print(f"\n\t10 - {B} es multiplo de {A} y {C}\n")
    elif ((A % C == 0) and (B % C == 0)):
        print(f"\n\t10 - {C} es multiplo de {A} y {B}\n")
    else:
        print(f"\n\t10 - Ningún dígito es múltiplo de los otros dos\n")

