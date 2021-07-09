import os
os.system("cls")

#               Ejercicios Semana 2 _ Parte 3

#   19. A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. 
#       Si la cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50 % 
#       para las horas extras. Calcular el salario del trabajador dadas las horas trabajadas y la 
#       tarifa ingresadas por el usuario.



#   20. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran
#       tres camisas o más se aplica un descuento del 20 % sobre el total de la compra y si son
#       menos de tres camisas un descuento del 10%



#   21. Hacer un programa que pida al usuario las tres notas de un alumno(deben estar entre 0 y 5 
#       y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó o 
#       no(aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro 
#       del rango permitido.



#   22. Verificar si un texto que termina en punto es un palíndromo(capicúa). Un texto es
#       palíndromo si se lee lo mismo de izquierda a derecha o de derecha a izquierda. 
#       Ej: “Amor a roma”.

texto = str(input(f"\n\tIngrese el texto a validar PALINDROMO:\t"))
texto = texto.lower()
texto = texto.replace(" ", "")
print(f"\n\tTexto introducido:\t{texto}")
if (texto == texto["::-1"]):
    print(f"\n\tEl texto es palíndromo(capicúa)")
else:
    print(f"\n\tEl texto NO es palíndromo(capicúa)\n")


#   23. Diseñe una calculadora que sume, reste, multiplique y divida, la cual le pida al usuario
#       mediante input el valor del primer número, el valor del segundo número y la operación a
#       realizar, hay que tener en cuenta la validación de los valores de entrada.


