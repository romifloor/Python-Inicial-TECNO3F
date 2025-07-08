from tkinter import StringVar

display_var = None
display_text = ""
operacion_actual = None
primer_operando = 0

def inicializar_controlador(ventana):
    global display_var
    display_var = StringVar(master=ventana)

def actualizar_display(valor):
    global display_text
    display_text += str(valor)
    display_var.set(display_text)
    display_var._root.children["!entry"].config(fg="#07F50F", bg="#000000")

def limpiar_display():
    global display_text, operacion_actual, primer_operando
    display_text = ""
    operacion_actual = None
    primer_operando = 0
    display_var.set(display_text)
    display_var._root.children["!entry"].config(fg="#07F50F", bg="#000000")

def borrar_ultimo_caracter():
    global display_text
    display_text = display_text[:-1]
    display_var.set(display_text)

def resultado():
    global display_text
    entry = display_var._root.children["!entry"]
    
    try:
        if not display_text:
            display_var.set("Sergio Desaprobado")
            entry.config(fg="#FFFF00", bg="#000000")
            return
            
        total = str(eval(display_text))
        display_text = total
        display_var.set(total)
        display_text = ''
        entry.config(fg="#07F50F", bg="#000000")
        
    except:
        display_text = ""
        display_var.set("**ERROR**")
        entry.config(fg="#FF0000", bg="#FFFF00")

#eventos de teclado
def manejar_tecla_presionada(tecla, ventana):
    if tecla.keysym == "Return":
        resultado()
    elif tecla.keysym == "BackSpace":
        borrar_ultimo_caracter()
    elif tecla.char in '0123456789':
        actualizar_display(tecla.char)
    elif tecla.char in '+-*/.':
        actualizar_display(tecla.char)
