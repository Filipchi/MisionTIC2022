from tkinter import Tk, Text, Button, END, re
# re -> regex modulo para expresiones regulares
#END -> indice de texto, indica el final del string
class Interfaz:
    def __init__(self, ventana):
        # Inicializar las caracteristicas de la ventana
        self.ventana = ventana
        self.ventana.title('Calculadora Filipchi')
        #self.ventana.geometry('680x380')
        self.ventana.configure(background='black')

        # Creación de la caja de texto que muestra el resultado de la operación
        self.pantalla = Text(ventana, state="disabled", width=40, height=3, background="light sea green", 
                             foreground="white", font=("Helventica", 15))

        # Ubicar la pantalla dentro de la ventana (Gestor de geometrías en TK -> grid, place, pack)
        # crea una cuadricula invisible, ubica el elemento en la fila # y columna #, abarca # espacios y crea un margen(padding de #x y #y)
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Inicializar respuesta en string vacío
        self.operacion = ""

        #_______ Creación de Botones
        boton1 = self.crearBoton(7)
        boton2 = self.crearBoton(8)
        boton3 = self.crearBoton(9)
        boton4 = self.crearBoton(u"\u232B", escribir=False) # Para el simbolo de borrar: unicode
        boton5 = self.crearBoton(4)
        boton6 = self.crearBoton(5)
        boton7 = self.crearBoton(6)
        boton8 = self.crearBoton(u"\u00f7") # para el simbolo de división %
        boton9 = self.crearBoton(1)
        boton10 = self.crearBoton(2)
        boton11 = self.crearBoton(3)
        boton12 = self.crearBoton("*")
        boton13 = self.crearBoton(".")
        boton14 = self.crearBoton(0)
        boton15 = self.crearBoton("+")
        boton16 = self.crearBoton("-")
        boton17 = self.crearBoton("=", escribir=False, ancho=20, alto=2) # Botones con dimensión diferente a los demás

        # Ubicar los botones en la ventana con el gestor grid
        botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9,
                   boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]
        contador = 0

        for fila in range(1,5):  # Empieza en fila 1 porque la cero la ocupa la pantalla de resultado
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador += 1
        # Para ubicar el último botón (el de "=")
        botones[16].grid(row=5, column=0, columnspan=4)
        
        return

    # Función para crear botones, text= Muestra el argumento/parámetro de los botones
    # "Command" le dice al objeto botón qué es lo que debe de hacer, para ello se emplea el metodo click,
    #  el cual determina si e escribe o no el valor del boton
    #  Se emplea "Lambda" como funcion anómina para que la "Command" me retorne el resultado de la acción 
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helventica", 15),
                      command=lambda:self.click(valor, escribir))

    # Controlar el evento click           
    def click(self, texto, escribir):
        # con escribir=True, se muetra el valor del boton presionado en la pantalla, de lo contrario (2 excepciones)
        if not escribir:
            if texto == "=" and self.operacion != "":
                # reemplazar el simbolo de división estético por el que interpreta python "/"
                self.operacion = re.sub(u"\u00f7", "/", self.operacion) # reemplazar 
                resultado = str(eval(self.operacion)) # eval me permite evaluar una operación matemática
                self.operacion = "" # reseteamos la variable de la operación
                self.LimpiarPantalla() # Borramos la operación para mostrar el resultado
                self.MostrarEnPantalla(resultado)

            elif texto==u"\u232B":
                self.operacion=""
                self.LimpiarPantalla()
        
        else:
            self.operacion+=str(texto)
            self.MostrarEnPantalla(texto)
    
    # Metodo para borrar la pantalla
    def LimpiarPantalla(self):
        self.pantalla.configure(state="normal") # se debe habilitar el modo normal para poder usar la función delete
        self.pantalla.delete("1.0", END) #delete tiene un parmetro de inicio "1.0"(fila 1 col 0) y un final "END"
        self.pantalla.configure(state="disable") # Volvemos a desabilitar para que el usuario no pueda escribir 
        return

    # método para mostrar en pantalla
    def MostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor) # Inserta el nuevo elemento al final actual del string
        self.pantalla.configure(state="disable") 
        return

ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()
