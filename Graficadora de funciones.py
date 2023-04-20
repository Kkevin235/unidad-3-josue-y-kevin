import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from tkinter import *
import numpy as np
import math

root = Tk()
root.geometry("700x600")
fig, ax = plt.subplots()

frame = Frame(root)
titulo = Label(frame, text="Grafica de funciones")
titulo.config(font=("Roboto",22))
titulo.pack(padx=10, pady=10, side=TOP)

izq = Frame(frame)
izq.pack(side=LEFT)

def graficar():
    ax.clear()
    funcion_e = funcion.get()
    funcionE = eval('lambda x: ' + funcion_e)
    x = np.linspace(int(funcionI.get()), int(funcionF.get()))
    y = funcionE(x)
    ax.plot(x, y)
    canvas.draw()

etiqueta_funcion = Label(izq, text="Función", font=("Roboto",12, "bold"))
etiqueta_funcion.pack(padx=4, pady=4)

funcion = StringVar()
entrada_funcion = Entry(izq, textvariable=funcion)
entrada_funcion.pack(padx=4, pady=4)

etiqueta_valorInicial = Label(izq, text="Valor inicial", font=("Roboto",12, "bold"))
etiqueta_valorInicial.pack(padx=4, pady=4)

funcionI = StringVar()
entrada_funcionInicial = Entry(izq, textvariable=funcionI)
entrada_funcionInicial.pack(padx=4, pady=5)

etiqueta_valorFinal = Label(izq, text="Valor final", font=("Roboto",12, "bold"))
etiqueta_valorFinal.pack(padx=4, pady=5)

funcionF = StringVar()
entrada_valorFinal = Entry(izq, textvariable=funcionF)
entrada_valorFinal.pack(padx=4, pady=6)

boton_Graficar = Button(izq, text="Graficar", command=graficar)
boton_Graficar.pack(padx=4, pady=8)

canvas = FigureCanvasTkAgg(fig, master=izq)
canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=True)

frame.pack()
root.mainloop()