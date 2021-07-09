import os
os.system("cls")

def punto5():
    divisores = 0
    i = 1
    while (i == 1):
        num5 = int(input(f"\n\t\t Ingrese el número de 2 digitos a validar:  "))
        if ((num5 / 10 >= 10) or (num5 / -10 >= 10)):
            print(f"\n\t\t La cantidad ingresada supera la esperada, intente de nuevo \n")
        else:
            break

    aux = num5
    if (num5 < 0):
        aux = aux*(-1) 

    while (i <= aux):
        if (aux % i == 0):
            divisores += 1
        i += 1

    if(num5 < 0 and divisores == 2):
        respuesta = f"\n\t\t\t {num5} es un número primo negativo \n"
    else:
        respuesta = f"\n\t\t\t {num5} No es un número primo negativo \n"
    return respuesta
print(punto5())
