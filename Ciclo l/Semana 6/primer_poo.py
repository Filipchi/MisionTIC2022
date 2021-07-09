import os
import random
os.system("cls")
# Para crear el constructor se debe emplear la palabra reservada "__init__"
class Ave:
    def __init__(self, especie, color, tamaño):
        self.especie = especie
        self.color = color
        self.tamaño = tamaño

# creación de elementos de la clase

fenix_1 = Ave("Calandria", "Amarillo", 2)
fenix_2 = Ave("Mielero", "Gris", 1)
fenix_3 = Ave("Saltarín", "Verde", 3)
fenix_4 = Ave("Pichofué", "Café", 4)

# print(f"\n\t\t El ave {fenix_1.especie} tiene un color {fenix_1.color} y un tamaño de {fenix_1.tamaño} unidades \n")

class CuentaBancaria:
    def __init__(self, saldoInicial):
        self.numeroCuenta = random.randint(1_000, 10_000)
        self.saldo = saldoInicial
    
    def retirar(self):
        monto = int(input(f"\t\t Ingrese el monto que desea retirar:  $ "))
        if(monto > self.saldo):
            print(f"\t\t\t ---------------------------")
            print(f"\t\t\t Fondos Insuficientes (${self.saldo}) ")
            print(f"\t\t\t ---------------------------")
        else:
            self.saldo -= monto
            print(f"\t\t\t ---------------------------")
            print(f"\t\t\t Transacción Exitosa !")
            print(f"\t\t\t El nuevo saldo de la cuenta {self.numeroCuenta} es de ${self.saldo}")
            print(f"\t\t\t ---------------------------")        
    
    def consignar(self):
        monto = int(input(f"\t\t Ingrese el monto que desea consignar:  $ "))
        self.saldo += monto
        print(f"\t\t\t ---------------------------")
        print(f"\t\t\t Transacción Exitosa !")
        print(f"\t\t\t El nuevo saldo de la cuenta {self.numeroCuenta} es de ${self.saldo}")
        print(f"\t\t\t ---------------------------")


    def consultarCuenta(self):
        print(f"\t\t\t -----------------------")
        print(f"\t\t\t Numero de Cuenta: {self.numeroCuenta}")
        print(f"\t\t\t Saldo Actual:     {self.saldo}")
        print(f"\t\t\t -----------------------")

cuenta1 = CuentaBancaria(80_000)

ans = True
while ans:
    print("""
    \t\t\t Bienvenido al Banco xyz
    \t\t\t -----------------------
    \t\t\t 1. Consultar Cuenta
    \t\t\t 2. Consignar 
    \t\t\t 3. Retirar
    \t\t\t 4. Salir
    \t\t\t -----------------------
    """)
    ans = str(input("\t\t\t ¿Qué desea realizar? "))
    if ans == "1":
      cuenta1.consultarCuenta()
    elif ans == "2":
      cuenta1.consignar()
    elif ans == "3":
      cuenta1.retirar()
    elif ans == "4":
      print("\n\t\t\t Es un gusto servirle \n")
      break
    elif ans != "":
      print("\n\t\t\t Error ! Intente nuevamente")
    os.system("pause")