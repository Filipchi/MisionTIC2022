import os
os.system('cls')

import tkinter as tk

ventana = tk.Tk()
ventana.title('Nombre ventana')
ventana.geometry('680x680')
ventana.configure(background='royal blue')
# Elementos
etiqueta1  =tk.Label(ventana, text='PrimerLabel', bg='slate gray', fg='black')
etiqueta1.pack()
# etiqueta1.pack(fill=tk.X)

# Ubicar el label con coordenadas
etiqueta2 = tk.Label(ventana, text='SegundoLabel', bg='firebrick', fg='black')
etiqueta2.pack(padx= 20, pady= 60)
ventana.mainloop()
