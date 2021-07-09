
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

# triangulos = {"Pareja1": {"Base 1": 1, "Altura 1": 1},
#               "Pareja2": {"Base 2": 1, "Altura 2": 1}}
Triangulos = []  # dicccionario PADRE
Pareja = {}      # Diccionario HIJO

def crea_triangulo():
    i = 0
    while (i < parejas):
        print(f"\n\t\t Ingrese la información de la pareja {i+1} en cm")
        base = float(input("\t\t\t Base [cm]:  "))
        altura = float(input("\t\t\t Altura [cm]:  "))
        Pareja.update({f"Base": base, f"Altura": altura})
        #Triangulos.update({f"Pareja {i+1}": Pareja})
        Triangulos.append(Pareja)
        #Triangulos = Triangulos.join(Pareja)
        print(Triangulos, Pareja, sep='\n')
        input()
        #Pareja.clear()
        print(Triangulos, Pareja, sep='\n')
        i += 1
    
    print(Triangulos)

    return Triangulos


def imprime_triangulo(triangulos_f):
    for i in triangulos_f:
        print("\t", i)
        for k in triangulos_f[i]:
            print("\t\t {:^10}: {:^10}" .format(k, triangulos_f[i][k]))


print(crea_triangulo())
print(imprime_triangulo(str(crea_triangulo)))
