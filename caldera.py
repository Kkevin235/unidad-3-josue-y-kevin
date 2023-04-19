import tkinter as tk
import tkinter.messagebox as messagebox

ventana = tk.Tk()
ventana.title("Control de Caldera de Fundición de Aluminio")
ventana.config(bg="red")  # Inicialmente, el fondo es rojo

# Función para cambiar el color del fondo de la ventana
def cambiar_color_fondo(encendido):
    if encendido:
        ventana.config(bg="green")
    else:
        ventana.config(bg="red")

# Función para encender la caldera
def encender_caldera():
    cambiar_color_fondo(True)

# Función para apagar la caldera
def apagar_caldera():
    cambiar_color_fondo(False)

# Función para arranque de banda
def arranque_banda():
    messagebox.showwarning("Arranque de Banda", "Se ha encendido el arranque de banda")

# Función para voltear caldera
def voltear_caldera():
    messagebox.showwarning("Voltear Caldera", "Se ha volteado la caldera")

# Función para encender la caldera
def encender_caldera():
    global temperatura
    cambiar_color_fondo(True)
    if temperatura == 0:
        temperatura = 659
    ventana.after(0, lambda: tk.messagebox.showinfo("Encender Caldera", "La caldera ha sido encendida."))

# Función para apagar la caldera
def apagar_caldera():
    global temperatura
    cambiar_color_fondo(False)
    if temperatura > 0:
        temperatura = 1
    ventana.after(0, lambda: tk.messagebox.showinfo("Apagar Caldera", "La caldera ha sido apagada."))

# Crear marco para botones
marco_botones = tk.Frame(ventana, bg="white", bd=1, relief=tk.SOLID)

# Crear botones y empaquetarlos en el marco
tk.Button(marco_botones, text="Encender", font=("Arial", 12), width=12, height=2, bd=0, command=encender_caldera).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(marco_botones, text="Apagar", font=("Arial", 12), width=12, height=2, bd=0, command=apagar_caldera).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(marco_botones, text="Arranque de Banda", font=("Arial", 12), width=18, height=2, bd=0, command=arranque_banda).pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(marco_botones, text="Voltear Caldera", font=("Arial", 12), width=14, height=2, bd=0, command=voltear_caldera).pack(side=tk.LEFT, padx=5, pady=5)

# Crear marco para los botones de temperatura y la etiqueta
marco_temperatura = tk.Frame(ventana, bg="white", bd=1, relief=tk.SOLID)

# Crear botones de temperatura y empaquetarlos en el marco
for simbolo in ["+", "-"]:
    tk.Button(marco_temperatura, text=simbolo, font=("Arial", 12), width=2, height=1, bd=0, command=lambda s=simbolo: cambiar_temperatura(s)).pack(side=tk.RIGHT, padx=5, pady=5)

# Crear etiqueta de temperatura y empaquetarla en el marco
etiqueta_temperatura = tk.Label(marco_temperatura, text="Temperatura actual: 660°C", font=("Arial", 12))
etiqueta_temperatura.pack(side=tk.LEFT, padx=5, pady=5)

# Función para cambiar la temperatura
def cambiar_temperatura(simbolo):
    global temperatura
    if simbolo == "+":
        temperatura += 1
    else:
        temperatura -= 1
    etiqueta_temperatura.config(text=f"Temperatura actual: {temperatura}°C")

# Empaquetar marcos en la ventana
marco_botones.pack(padx=10, pady=10)
marco_temperatura.pack(padx=10, pady=10)

# Iniciar la variable temperatura en 660
temperatura = 0
# Ejecutar el bucle principal de la ventana
ventana.mainloop()
