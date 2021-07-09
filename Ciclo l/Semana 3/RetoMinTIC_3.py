import os
os.system("cls")
print(f"\n\t\t\t RETO MINTIC NO.3 \n")
print(f"\t Determina costo de mensaje por telegrama\n")

def costo_telegrama(mensajes:list)-> dict:
    letras = 0
    palabras = 1
    precio = 0
    resultado = {}
    for i in mensajes:
        for j in i:
            if j == " ":
                if letras <= 5:
                    precio += 100
                elif letras >= 5:
                    precio += 200
                letras = 0
                palabras += 1
            else:
                letras += 1
        if letras <= 5:
            precio += 100
        elif letras >= 5:
            precio += 200
        if palabras > 7:
            precio -= 300
        resultado[i] = precio
        precio = 0
        letras = 0
        palabras = 1
    return resultado

mensaje_1 = ["Un caluroso saludo", "Deseo que tenga un gran día"]
mensaje_2 = ["Bienvenidos tripulantes a misión tic 2022 es un placer que estén aprendiendo programación en la UTP", "Deseando que se encuentre muy bien envío un caluroso saludo con mucho amor", "Se pasa a informar que el día 5 de mayo de 2021 entrará a trabajar en el área de mantenimiento"]

print(costo_telegrama(mensaje_1))
print(costo_telegrama(mensaje_2))
