
# Validación de entrada numérica
while True:
    entrada = input("\nIngrese un número entero (0 para salir): ")
    
    if entrada.lstrip('-').isdigit():  
        numero = int(entrada)
    else:
        print("¡Error! Debe ingresar un número entero.")
        continue

    if numero == 0:
        print("Programa finalizado.")
        break

