import os
os.system("cls")

def costo_anuncio (mensajes:list)->dict:
    letrasEconomicas = ["f","i","j","k","l","t","r"]
    precio = 0
    resultado = {}
    for i in mensajes:
        for j in i:
            if j in letrasEconomicas:
                precio = precio + 50
            else:
                precio = precio + 100
        resultado[i] = precio
        precio = 0
    return resultado

print(costo_anuncio(["foca loca", "Arepas jaime"]))
print(costo_anuncio(["Tiendas la locura","Galletas maria"]))