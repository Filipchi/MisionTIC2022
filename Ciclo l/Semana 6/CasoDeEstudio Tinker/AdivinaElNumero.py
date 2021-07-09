
from tkinter import Label, Tk, Text, Button, END, re
import os
os.system("cls")
# from random import random, randrange
# Este juego consiste en adivinar un número entre un rango, 
# En pantalla se dará una pista si el npumero que escogió el usuario es mayor o menor al número real

# *********************** Pendiente ***********************
# Colorear con rojo cada boton elegido que no sea la respuesta
# Implementar una pantalla que muestre el número de intentos
# *********************************************************
# numero_real = random.randrage(15) 

class Interfaz:
    def __init__(self, ventana):
        # Inicializar las caracteristicas de la ventana
        self.ventana = ventana
        self.ventana.title('Adivina El Número Filipchi')
        self.ventana.configure(background='black')

        # Creación de la caja de texto que muestra el resultado de la operación
        self.pantalla = Text(ventana, state="disabled", width=40, height=3, background="light sea green",
                             foreground="white", font=("Helventica", 15))

        # Ubicar la pantalla dentro de la ventana (Gestor de geometrías en TK -> grid, place, pack)
        # crea una cuadricula invisible, ubica el elemento en la fila # y columna #, abarca # espacios y crea un margen(padding de #x y #y)
        self.pantalla.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        # Inicializar respuesta en string vacío
        self.mensaje = ""

        boton1 = self.crearBoton(1)
        boton2 = self.crearBoton(2)
        boton3 = self.crearBoton(3)
        boton4 = self.crearBoton(4)
        boton5 = self.crearBoton(5)
        boton6 = self.crearBoton(6)
        boton7 = self.crearBoton(7)
        boton8 = self.crearBoton(8)
        boton9 = self.crearBoton(9)
        boton10 = self.crearBoton(10)
        boton11 = self.crearBoton(11)
        boton12 = self.crearBoton(12)
        boton13 = self.crearBoton(13)
        boton14 = self.crearBoton(14)
        boton15 = self.crearBoton(15)

        botones = [boton1, boton2, boton3, boton4, boton5, 
                   boton6, boton7, boton8, boton9, boton10,
                   boton11, boton12, boton13, boton14, boton15]
        contador = 0

        # Empieza en fila 1 porque la cero la ocupa la pantalla de resultado
        for fila in range(1, 4):
            for columna in range(5):
                botones[contador].grid(row=fila, column=columna, padx=4, pady=4)
                contador += 1

        self.intentos = Label(ventana, text='Número de Intentos: ', width=20,
                              height=2, bg='indianred2', fg='black', font=("Helventica", 12))
        self.intentos.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

        return

    def crearBoton(self, valor, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helventica", 15),
                      command=lambda: self.click(valor))

    def click(self, texto):
        if numero_real > texto:
            self.pantalla.configure(state="normal")
            self.pantalla.insert("El Número ")
            self.pantalla.configure(state="disable") 

        elif numero_real < texto:
            self.pantalla.configure(state="normal")
            self.pantalla.insert("El Número ")
            self.pantalla.configure(state="disable") 
        else:
            self.pantalla.configure(state="normal")
            self.pantalla.insert("Felicidades, lo haz adivinado")
            self.pantalla.configure(state="disable")
        

        # con escribir=True, se muetra el valor del boton presionado en la pantalla, de lo contrario (2 excepciones)

ventana_principal = Tk()
Adivina = Interfaz(ventana_principal)
ventana_principal.mainloop()
