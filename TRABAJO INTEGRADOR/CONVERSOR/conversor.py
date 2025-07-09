from tkinter import Tk, Entry, Button, Label, StringVar, Frame, OptionMenu
import os

def convertir_temperatura():
    """Realizamos la conversión según las escalas seleccionadas"""
    valor = var_entrada.get()
    
    if not valor.replace('.', '', 1).isdigit():
        mensaje_error.set("Error: Ingrese solo números")
        return
    
    valor = float(valor)
    origen = var_origen.get()
    destino = var_destino.get()
    
    # Convertimos primero a Celsius 
    if origen == "°C (Celsius)":
        celsius = valor
    elif origen == "°F (Fahrenheit)":
        celsius = (valor - 32) * 5/9
    elif origen == "K (Kelvin)":
        celsius = valor - 273.15
    
    # Convertimos de Celsius a la escala destino
    if destino == "°C (Celsius)":
        resultado = celsius
    elif destino == "°F (Fahrenheit)":
        resultado = (celsius * 9/5) + 32
    elif destino == "K (Kelvin)":
        resultado = celsius + 273.15
    
    resultado_var.set(f"{resultado:.2f} {destino}")
    mensaje_error.set("")  

def limpiar_campos():
    """Limpiamos todos los campos usando StringVar"""
    var_entrada.set('')
    resultado_var.set('')
    mensaje_error.set('')

# Ventana principal
fondo_color = "#598eff"
texto_color = "white"

ventana = Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("400x280")  
ventana.configure(bg=fondo_color)  
ventana.resizable(False, False)
icon_path = os.path.join(os.path.dirname(__file__), 'img', 'termometro.ico')
ventana.iconbitmap(icon_path)


escalas = ["°C (Celsius)", "°F (Fahrenheit)", "K (Kelvin)"]
var_origen = StringVar(ventana)
var_origen.set(escalas[0])

var_destino = StringVar(ventana)
var_destino.set(escalas[1])

var_entrada = StringVar()
resultado_var = StringVar()
mensaje_error = StringVar()

# Interfaz de usuario
Label(ventana, text="Conversor de Temperatura", font=("Arial", 14, 'bold'),bg=fondo_color,fg=texto_color).pack(pady=10)

# Marco para entrada de valor y mensaje de error
frame_entrada = Frame(ventana,bg=fondo_color)
frame_entrada.pack(pady=5)

# Campo de entrada
Label(frame_entrada, text="Valor:",font=("Arial", 11),bg=fondo_color,fg=texto_color).grid(row=0, column=0, padx=5, sticky='e')
Entry(frame_entrada, textvariable=var_entrada, font=("Arial", 10), width=15).grid(row=0, column=1, padx=5)

# Mensaje de error 
Label(frame_entrada, textvariable=mensaje_error, fg="#F60000",font=("Arial", 9),bg=fondo_color).grid(row=1, columnspan=2, pady=(2, 0))

# Marco para selección de escalas
frame_escalas = Frame(ventana,bg=fondo_color)
frame_escalas.pack(pady=10)

Label(frame_escalas, text="De:",font=("Arial", 11),bg=fondo_color,fg=texto_color).grid(row=0, column=0, padx=5, sticky='e')
OptionMenu(frame_escalas, var_origen, *escalas).grid(row=0, column=1, padx=5)

Label(frame_escalas, text="a:",font=("Arial", 11), bg=fondo_color,fg=texto_color).grid(row=0, column=2, padx=5, sticky='e')
OptionMenu(frame_escalas, var_destino, *escalas).grid(row=0, column=3, padx=5)

# Botones
frame_botones = Frame(ventana,bg=fondo_color)
frame_botones.pack(pady=10)

Button(frame_botones, text="Convertir",font=("Arial", 10), command=convertir_temperatura, bg="#000000", fg="white", activebackground="#c3c9cf").grid(row=0, column=0, padx=5)
Button(frame_botones, text="Limpiar", font=("Arial", 10), command=limpiar_campos, bg="#000000", fg="white", activebackground="#c3c9cf").grid(row=0, column=1, padx=5)

# Resultado
Label(ventana, text="Resultado:", font=("Arial", 11),bg=fondo_color,fg=texto_color).pack(pady=(10, 0))
Label(ventana, textvariable=resultado_var, font=("Arial", 13,'bold'),bg=fondo_color,fg=texto_color).pack()

ventana.mainloop()


