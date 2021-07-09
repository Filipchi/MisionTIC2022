import os
os.system("cls")

#               Ejercicios Semana 2 _ Parte 2

#   11. Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se 
#       encuentra el mayor dígito.

print(f"\n\tIngrese Tres (3) números enteros de 2 dígitos cada uno:\t")
num1 = int(input(f"\n\t\tI.   Primer número:\t"))
num2 = int(input(f"\n\t\tII.  Segundo número:\t"))
num3 = int(input(f"\n\t\tIII. Tercer número:\t"))

if ((num1 < 10) or (num1 > 99) or (num2 < 10) or (num2 > 99) or (num3 < 10) or (num3 > 99)):
    print(f"\n\t11 - Los números ingresados NO cumplen con el criterio\n")
else:
    A1 = int(num1/10)
    B1 = num1 % 10

    A2 = int(num2/10)
    B2 = num2 % 10

    A3 = int(num3/10)
    B3 = num3 % 10

    if(((A1 > A2) and (A1 > A3) and (A1 > B2) and (A1 > B3)) or ((B1 > A2) and (B1 > A3) and (B1 > B2) and (B1 > B3))):
        print(f"\n\t11 - El mayor dígito se encuentra en el número {num1}\n")

    elif((((A2 > A1) and (A2 > A3) and (A2 > B1) and (A2 > B3)) or ((B2 > A1) and (B2 > A3) and (B2 > B1) and (B2 > B3)))):
        print(f"\n\t11 - El mayor dígito se encuentra en el número {num2}\n")
    
    elif((((A3 > A1) and (A3 > A2) and (A3 > B1) and (A3 > B2)) or ((B3 > A1) and (B3 > A2) and (B3 > B1) and (B3 > B2)))):
        print(f"\n\t11 - El mayor dígito se encuentra en el número {num3}\n")
    else:
        print(f"\n\t11 - Por lo menos dos números comparten el dígito mayor\n")

#   12. Leer un número entero de suma de los otros dos.



#   13. Leer un número entero menor que 50 y positivo y determinar si es un número primo.



#   14. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al
#       penúltimo.

num4d = int(input(f"\n\tIngrese un numero entero de 4 digitos:\t"))

if ((num4d < 1000) or (num4d > 9999)):
    print(f"\n\t8 - El numero {num4d} No es de 4 dígitos\n")
else:
    A = int(num4d/1000)
    B = int(num4d/100) % 10
    C = int(num4d / 10) % 10
    D = num4d % 10

    if (B == C):
        print(f"\n\t14 - El numero {num4d} tiene el segundo y penultimo digito igual\n")
    else:
        print(f"\n\t14 - El numero {num4d} No tiene el segundo y penultimo digito igual\n")

# 15. Leer un número entero y determinar si es múltiplo de 7.

num15 = int(input(f"\n\tIngrese un numero entero:\t"))

if ((num15 % 7) == 0):
    print(f"\n\t8 - El numero {num15} es múltiplo de 7\n")
else:
    print(f"\n\t8 - El numero {num15} No es múltiplo de 7\n")

# 16. Leer un número entero menor que mil y determinar cuántos dígitos tiene.

num16 = int(input(f"\n\tIngrese un numero entero MENOR que 1000:\t"))

if(num16 >= 1000):
    print(f"\n\t8 - El numero {num16} es MAYOR que mil\n")
else:
    if (int(num16/10) == 0):
        print(f"\n\t8 - El numero {num16} es de un (1) dígito\n")
    elif (int(num16/100) == 0):
        print(f"\n\t8 - El numero {num16} es de dos (2) dígito\n")
    elif (int(num16/1000) == 0):
        print(f"\n\t8 - El numero {num16} es de tres (3) dígito\n")

# 17. Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares.

num17 = int(input(f"\n\tIngrese un numero entero de 4 digitos:\t"))

if ((num17 < 1000) or (num17 > 9999)):
    print(f"\n\t8 - El numero {num17} No es de 4 dígitos\n")
else:
    A = int(num17/1000)
    B = int(num17/100) % 10
    C = int(num17 / 10) % 10
    D = num17 % 10
    par = int(0)
    impar = int(0)

    if ((A % 2) == 0):
        par = par + 1
    else:
        impar = impar + 1
        
    if ((B % 2) == 0):
        par = par + 1
    else:
        impar = impar + 1
    
    if ((C % 2) == 0):
        par = par + 1
    else:
        impar = impar + 1
    
    if ((D % 2) == 0):
        par = par + 1
    else:
        impar = impar + 1

    if (par > impar):
        print(f"\n\t17 - El numero {num17} tiene mas dígitos PARES\n")
    elif (impar > par):
        print(f"\n\t17 - El numero {num17} tiene mas dígitos IMPARES\n")
    else:
        print(f"\n\t17 - El numero {num17} tiene la misma cantidad de dígitos pares e impares\n")

# 18. Leer tres números enteros y determinar si el último dígito de los tres números es igual.


