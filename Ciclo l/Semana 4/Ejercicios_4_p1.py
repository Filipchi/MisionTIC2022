import os
os.system("cls")
from functools import reduce

print("\n\t\t\t Funciones para Colecciones de Datos\n")

#       Problema  # 1:
# Utilizar la función incorporada map() para crear una función que retorne una lista con la longitud de cada palabra(separadas por espacios) de una frase. La función recibe una cadena de texto y retornará una lista.

def problema1 ():
    frase = str(input("\t 1) Ingrese la frase a validar:  "))
    # respuesta = list(map(lambda entrada: len(entrada), frase1.split())) # JH
    respuesta = list(map(len, frase.split()))  # o también
    return respuesta

# print(problema1())

#       Problema  # 2:
# Crear una función que tome una lista de dígitos y devuelva al número al que corresponden.
# Por ejemplo[1, 2, 3] corresponde a el número ciento veintitrés(123). Utilizar la función reduce.

def problema2():
    cantidad = int(input("\t 2) Ingrese la cantidad de dígitos a validar:  "))
    digitos = [int(input(f"\t\t Ingrese el {x+1} dígito:  ")) for x in range(cantidad)]
    print("\t Digitos ingresados: ", digitos)
    respuesta = reduce(lambda y, z: y * 10 + z, digitos)
    return respuesta

# print(problema2())

#       Problema  # 3:
# Crear una función que retorne las palabras de una lista de palabras que comience con una letra en específico. Utilizar la función filter.

def problema3():
    frase = str(input("\t 3) Ingrese la frase a validar:  "))
    letra = str(input("\n\t\t Ingrese la letra inicial que desea filtrar: "))
    respuesta = list(filter(lambda x: x[0] == letra, frase.split()))
    return respuesta

# print(problema3())

#       Problema  # 4:
# Realizar una función que tome una lista de comprensión para devolver una lista de la misma longitud donde cada valor son las dos cadenas de L1 y L2 concatenadas con un conector entre ellas. Ejemplo: Listas: ['A', 'a']['B', 'b'] Conector: '-' Salida: ['A-a']['B-b']. Utilizar la función zip.

def problema4():
    longitud = int(input("\t 4) Ingrese la longitud de las listas:  "))
    print("\n\t Lista 1:")
    lista1 = [str(input(f"\t\t Ingrese el {x+1} elemento:  ")) for x in range(longitud)]
    print("\n\t Lista 2:")
    lista2 = [str(input(f"\t\t Ingrese el {x+1} elemento:  ")) for x in range(longitud)]
    # for L1, L2 in zip (lista1, lista2): print("{} - {}".format(L1, L2))
    return [L1 + "-" + L2 for (L1, L2) in zip(lista1, lista2)]

# print(problema4())

# La función enumarate es otra de las herramientas para manipulación de colecciones de datosl en Python. Consultar cuál es su finalidad y una vez teniendo claro su comportamiento, resolver los dos siguientes problemas propuestos:

#       Problema  # 5:
# Realizar una función que tome una lista y retorne un diccionario que contenga los valores de la lista como clave y el índice como el valor. Utilizar la función enumerate.

def problema5():
    longitud = int(input("\t 5) Ingrese la longitud de la lista:  "))
    lista = [str(input(f"\t\t Ingrese el {x+1} elemento:  ")) for x in range(longitud)]

    return {clave: valor for valor, clave in enumerate(lista)}

# print(problema5())

#       Problema  # 6:
# Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo valor es igual a su índice. Utilizar la función enumerate.

def problema6():
    longitud = int(input("\t 5) Ingrese la longitud de la lista:  "))
    lista = [str(input(f"\t\t Ingrese el {x+1} elemento:  ")) for x in range(longitud)]

    return len([num for count, num in enumerate(lista) if num == count])

# print(problema5())
