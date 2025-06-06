
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


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

    # Conteo de caracteres
    texto = input("Ingrese una palabra o frase: ")
    cantidad_caracteres = len(texto)
    print(f"\nLa palabra/frase tiene {cantidad_caracteres} caracteres.")

    # Factorial    
    if cantidad_caracteres < 0:
        print("No se puede calcular factorial de números negativos.")
    else:
        # Cálculo del factorial
        factorial = calcular_factorial(cantidad_caracteres)
        print(f"El factorial de {cantidad_caracteres} es: {factorial}")
        
        if factorial % 2 == 0:
            print("El resultado es PAR.")
        else:
            print("El resultado es IMPAR.")
    
    print("\n" + "="*50)  
