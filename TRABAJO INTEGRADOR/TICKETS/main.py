import json
import random
import os
import sys

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def generar_ticket():
    while True:
        limpiar_pantalla()
        print("Ingrese los datos para Generar un nuevo Ticket")
        nombre = input("Ingrese su Nombre: ")
        sector = input("Ingrese su Sector: ")
        asunto = input("Ingrese el Asunto: ")
        mensaje = input("Ingrese un Mensaje: ")

        numero_ticket = random.randint(1000, 9999)
        archivo = f"ticket_{numero_ticket}.json"

        ticket = {
            "nombre": nombre,
            "sector": sector,
            "asunto": asunto,
            "mensaje": mensaje,
            "numero": numero_ticket
        }

        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(ticket, f, ensure_ascii=False, indent=4)

        print("\n" + "="*40)
        print("         Se generó el siguiente Ticket")
        print("="*40)
        print(f"Nombre: {nombre}    N° Ticket: {numero_ticket}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print("Es importante que recuerdes tu N° de Ticket. Lo vas a necesitar para futuras consultas.")
        
        continuar = input("\n¿Desea generar un nuevo Ticket? (s/n): ").lower()
        if continuar != 's':
            break

def leer_ticket():
    while True:
        limpiar_pantalla()
        numero = input("Ingrese el número del Ticket: ")
        archivo = f"ticket_{numero}.json"

        if os.path.isfile(archivo):
            with open(archivo, "r", encoding="utf-8") as f:
                ticket = json.load(f)
            
            print("\n" + "="*40)
            print("            Información del Ticket")
            print("="*40)
            print(f"Nombre: {ticket['nombre']}")
            print(f"Sector: {ticket['sector']}")
            print(f"Asunto: {ticket['asunto']}")
            print(f"Mensaje: {ticket['mensaje']}")
        else:
            print("\nNo se encontró el número de ticket ingresado.")

        continuar = input("\n¿Desea leer otro Ticket? (s/n): ").lower()
        if continuar != 's':
            break

def salir():
    confirmar = input("¿Está seguro que desea salir? (s/n): ").lower()
    if confirmar == 's':
        print("Gracias por usar el sistema de tickets.")
        sys.exit()

def menu_principal():
    while True:
        limpiar_pantalla()
        print("Hola bienvenido al sistema de Tickets\n")
        print("1 - Generar un Nuevo Ticket")
        print("2 - Leer un Ticket")
        print("3 - Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            generar_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            salir()
        else:
            input("Opción inválida. Presione Enter para continuar.")

menu_principal()
