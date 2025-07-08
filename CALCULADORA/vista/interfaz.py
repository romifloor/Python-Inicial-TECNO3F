from tkinter import Tk, Entry, Button, PhotoImage, Label
import controlador.controlador as ctrl

def crear_ventana_principal():
    ventana = Tk()
    ventana.configure(background="#8EDAF8")
    ventana.title("Calculadora Basica")
    ventana.geometry("300x370")
    ventana.resizable(False, False)
    return ventana

def crear_logo():
    logo_casio = PhotoImage(file="img/casio.png").subsample(5, 5)
    return logo_casio

def configurar_botones(ventana, FUENTE, BTN_FONDO, BTN_FUENTE):
    botones = [
        # Fila 1
        ("7", 0, 2, 2, 1, 0, lambda: ctrl.actualizar_display(7)),
        ("8", 2, 2, 2, 1, 0, lambda: ctrl.actualizar_display(8)),
        ("9", 4, 2, 2, 1, 0, lambda: ctrl.actualizar_display(9)),
        # Fila 2
        ("4", 0, 3, 2, 1, 0, lambda: ctrl.actualizar_display(4)),
        ("5", 2, 3, 2, 1, 0, lambda: ctrl.actualizar_display(5)),
        ("6", 4, 3, 2, 1, 0, lambda: ctrl.actualizar_display(6)),
        # Fila 3
        ("1", 0, 4, 2, 1, 0, lambda: ctrl.actualizar_display(1)),
        ("2", 2, 4, 2, 1, 0, lambda: ctrl.actualizar_display(2)),
        ("3", 4, 4, 2, 1, 0, lambda: ctrl.actualizar_display(3)),
        ("0", 2, 5, 2, 1, 0, lambda: ctrl.actualizar_display(0)),
        # Operadores
        ("/", 6, 2, 2, 1, 0, lambda: ctrl.actualizar_display('/')),
        ("*", 8, 2, 2, 1, 0, lambda: ctrl.actualizar_display('*')),
        ("+", 8, 3, 2, 2, 33, lambda: ctrl.actualizar_display('+')),
        ("-", 6, 3, 2, 1, 0, lambda: ctrl.actualizar_display('-')),
        (".", 6, 4, 2, 1, 0, lambda: ctrl.actualizar_display('.')),
        # Especiales
        ("=", 6, 5, 4, 1, 0, ctrl.resultado),
        ("C", 6, 1, 2, 1, 0, ctrl.limpiar_display),
        ("<-", 8, 1, 2, 1, 0, ctrl.borrar_ultimo_caracter),
        ("(", 0, 5, 2, 1, 0, lambda: ctrl.actualizar_display('(')),
        (")", 4, 5, 2, 1, 0, lambda: ctrl.actualizar_display(')'))
    ]
    
    for texto, col, fila, cspan, rspan, ipady, comando in botones:
        Button(
            ventana, text=texto, fg=BTN_FUENTE, bg=BTN_FONDO,
            font=FUENTE, width=4, height=2, command=comando
        ).grid(
            column=col, row=fila, columnspan=cspan, rowspan=rspan,
            sticky="nsew", ipady=ipady
        )

def configurar_teclado(ventana):
    ventana.bind('<Return>', lambda e: ctrl.resultado())
    ventana.bind('<BackSpace>', lambda e: ctrl.borrar_ultimo_caracter())
    
    for tecla in '0123456789':
        ventana.bind(tecla, lambda e, t=tecla: ctrl.actualizar_display(t))
    
    for tecla in '+-*/.':
        ventana.bind(tecla, lambda e, t=tecla: ctrl.actualizar_display(t))


def crear_interfaz():
    # Constantes
    FUENTE = ("Arial", 16)
    BTN_FONDO = "#FFFFFF"
    BTN_FUENTE = "#000000"
    
    ventana = crear_ventana_principal()
    ctrl.inicializar_controlador(ventana)
    logo_casio = crear_logo()
    
    Entry(ventana, textvariable=ctrl.display_var, bg="#000000", fg="#07F50F", 
          width=25, font=FUENTE, justify="right", state='readonly',
          readonlybackground="#000000").grid(columnspan=10, ipady=10)
    
    # Logo
    Label(ventana, image=logo_casio, width=170, height=60
         ).grid(columnspan=6, column=0, row=1, sticky="nsew")
    
    # Botones
    configurar_botones(ventana, FUENTE, BTN_FONDO, BTN_FUENTE)
    
    ventana.logo_casio = logo_casio
    configurar_teclado(ventana)
    ctrl.display_var._root = ventana
    
    return ventana