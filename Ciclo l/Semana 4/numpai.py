
import os
from typing import Iterable
os.system("cls")
print("\n")
# Funcion anónima 
# print((lambda entrada : entrada ** 2)(8))

# función  map
h = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda entrada: entrada ** 3, h)))

# funcion filter
tupla = 1,2,3,4,5,6,7,32,4,6,9,6,3,44,22
def mayor_a_cinco (elemento):
    return elemento > 5

# print(list(filter(mayor_a_cinco, tupla)))
# print(list(filter(lambda entrada : entrada > 5, tupla)))
# filtra multiplos de n
# print(list(filter(lambda entrada: entrada % 2 == 0, tupla)))
# print(list(filter(lambda entrada: entrada % 3 == 0, tupla)))
# print(list(filter(lambda entrada: entrada % 5 == 0, tupla)))

# determinar la edad en el 2050 de una lista de personas a partir de su fecha de nacimiento
nacimiento = [1998, 1990, 1994, 1980, 1976, 2001]
# print(list(map(lambda entrada: 2050 - entrada, nacimiento)))

# funcion reduce, sirve como acomulador
# para realizar la suma de los parámetros numericos de un elemento Iterable
from functools import reduce

lista_a_sumar = [ i for i in range(2, 5)]
# print(reduce(lambda acomulador = 0, elemento = 0 : acomulador + elemento, lista_a_sumar))

# imprimir lista de lenguages 
lista_lenguages = ["python", "java", "ruby", "julia", "elixir", "clojure", "rust"]
# print(reduce(lambda acomulador = "", elemento = "" : acomulador + "-" + elemento, lista_lenguages))

# para unir nuevamente la lista 
# print("-".join(lista_lenguages))


# _________________________
# imprimir tabla de multiplicar
def multiplicar(const, n):
    print(f"\t\t {const} x {n} = {const*n}")

constante_12 = [12 for i in range(1, 11)]

print(list(map(multiplicar, constante_12, range(1, 11))))

print("\n")
