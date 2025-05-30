import random

def juego_adivina_numero():
    
    numero_secreto = random.randint(1, 50)
    intentos = 5
    
    print("¡Bienvenido al juego Adivina el Número!")
    print("--------------------------------------")
    print(f"Tienes que adivinar un número entre 1 y 50.")
    print(f"Tienes {intentos} intentos. ¡Buena suerte!\n")
    
    while intentos > 0:
        entrada = input("Ingresa tu número: ")
        
        if entrada.isdigit():  
            numero = int(entrada)
            
            if numero < 1 or numero > 50:
                print("El número debe estar entre 1 y 50. Intenta de nuevo.")
                continue  
            
            if numero == numero_secreto:
                print(f"\n¡Felicidades! Adivinaste el número {numero_secreto}.")
                print(f"Lo lograste en {6 - intentos} intentos.")
                return  
            
            # Pistas
            if numero < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
            
            intentos -= 1
            print(f"Te quedan {intentos} intentos.\n")
            
        else:
            print("Por favor, ingresa solo números enteros.")

    print(f"\n¡Se acabaron los intentos! El número secreto era: {numero_secreto}")

juego_adivina_numero()