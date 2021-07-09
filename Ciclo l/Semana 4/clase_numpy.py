import os
os.system("cls")
print("\n")
# formas de importar una libreria en python:
# from math import exp
# si quiero importar una función en un archivo de la misma carpeta la forma sería:
# from (nombre del archivo) import (nombre de la función)

# También puedo importar una librería y asignarle un alias por ejemplo
import numpy as np

#arreglos empleando la librería numpy
x = np.array([1, 2, 3, 4, 5, 6])
y_python = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
y = np.array(y_python)

print(x)
print(y)
# para acceder a alguna posición de la matriz (empieza a cntar desde [0][0])
print(y[1][2])
# propiedades de los arreglos con numpy 
# ndim -> me retorna e número de dimensiones del arreglo
# size -> retorna la cantidad total de elemntos del arreglo
#shape -> retorna una tupla de enteros que indica el número de elementos almacenados en cada dimensión

print(y.shape)

# para adicionar, borrar y ordenar 
# a = np.append(x, 'valor')
# a = np.delete(x, 'valor')
# a = np.sort(x)

# Creación de un arreglo con arange('inicio', 'fin', pasos) si no se ingresa el valor de pasos, pasos == 1
z = np.arange(3, 30, 5) 
print(z)

# reshape -> me permite modificar la estructura de un arreglo, 'nombre_arreglo'.reshape(filas, columnas)
w = x.reshape(2, 3)
print(w)

# 
print("------------------- Slicing / Indexing -------------------")
q = np.arange(1, 15)
print(q)
print(q[0:3])
print(q[3:])
print("------------------- Condiciones-------------------")
print(q[q<6])
print(q[(q>5) & (q % 2 == 0)])
print("------------------- operaciones sobre arrays-------------------")
x = np.arange(2, 50, 3)
print(x)
print(x.sum())
print(x.min())
print(x.max())
print("------------------- Broadcasting(transmición)-------------------")
x1 = np.arange(1, 10)
print(x1)
x2 = x1 * 13
print(x2)

# operaciones estadisticoas
# mean, median, var, std ------------------> np.mean(x)

# Crear arreglos con elementos a) np.zeros((#, #))    b) np.ones((#, #)) 
# con algún número en especiifico  np.full((#, #), número esp)

# matriz identidad np.eye(#)
# matriz de valores aleatorios ------> np.random.random(#, #)
