from tkinter import Tk, Entry, Button, Label, StringVar, Frame, OptionMenu

def convertir_temperatura():
    """Realiza la conversión según las escalas seleccionadas"""
    valor = var_entrada.get()
    
    if not valor.replace('.', '', 1).isdigit():
        mensaje_error.set("Error: Ingrese solo números")
        return
    
    valor = float(valor)
    origen = var_origen.get()
    destino = var_destino.get()
    
    # Convertir primero a Celsius 
    if origen == "Celsius":
        celsius = valor
    elif origen == "Fahrenheit":
        celsius = (valor - 32) * 5/9
    elif origen == "Kelvin":
        celsius = valor - 273.15
    
    # Convertir de Celsius a la escala destino
    if destino == "Celsius":
        resultado = celsius
    elif destino == "Fahrenheit":
        resultado = (celsius * 9/5) + 32
    elif destino == "Kelvin":
        resultado = celsius + 273.15
    
    resultado_var.set(f"{resultado:.2f} {destino}")
    mensaje_error.set("")  

def limpiar_campos():
    """Limpia todos los campos usando StringVar"""
    var_entrada.set('')
    resultado_var.set('')
    mensaje_error.set('')

# Ventana principal
ventana = Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("400x280")  
ventana.resizable(False, False)
# ventana.iconbitmap("img/termometro.ico")


escalas = ["Celsius", "Fahrenheit", "Kelvin"]
var_origen = StringVar(ventana)
var_origen.set(escalas[0])

var_destino = StringVar(ventana)
var_destino.set(escalas[1])

var_entrada = StringVar()
resultado_var = StringVar()
mensaje_error = StringVar()

# Interfaz de usuario
Label(ventana, text="Conversor de Temperatura", font=("Arial", 14, 'bold')).pack(pady=10)

# Marco para entrada de valor y mensaje de error
frame_entrada = Frame(ventana)
frame_entrada.pack(pady=5)

# Fila para el campo de entrada
Label(frame_entrada, text="Valor:").grid(row=0, column=0, padx=5, sticky='e')
Entry(frame_entrada, textvariable=var_entrada, width=15).grid(row=0, column=1, padx=5)

# Fila para el mensaje de error (debajo del Entry)
Label(frame_entrada, textvariable=mensaje_error, fg="red").grid(row=1, columnspan=2, pady=(2, 0))

# Marco para selección de escalas
frame_escalas = Frame(ventana)
frame_escalas.pack(pady=10)

Label(frame_escalas, text="De:").grid(row=0, column=0, padx=5, sticky='e')
OptionMenu(frame_escalas, var_origen, *escalas).grid(row=0, column=1, padx=5)

Label(frame_escalas, text="a:").grid(row=0, column=2, padx=5, sticky='e')
OptionMenu(frame_escalas, var_destino, *escalas).grid(row=0, column=3, padx=5)

# Botones
frame_botones = Frame(ventana)
frame_botones.pack(pady=10)

Button(frame_botones, text="Convertir", command=convertir_temperatura).grid(row=0, column=0, padx=5)
Button(frame_botones, text="Limpiar", command=limpiar_campos).grid(row=0, column=1, padx=5)

# Resultado
Label(ventana, text="Resultado:", font=("Arial", 10)).pack(pady=(10, 0))
Label(ventana, textvariable=resultado_var, font=("Arial", 12)).pack()

ventana.mainloop()
