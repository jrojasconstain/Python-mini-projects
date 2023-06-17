# Importa el módulo random para generar números aleatorios
import random

# Imprime un mensaje de bienvenida y las reglas del juego
print("\nADIVINA EL NÚMERO\n")
print("Pensaremos en un número del 1 al 10 y tendrás 3 oportunidades de adivinar \nSi adivinas correctamente, ganarás $500 pesos")

# Genera un número aleatorio entre 1 y 10 y lo almacena en la variable number
number = random.randint(1,10)

# Crea un bucle que se ejecuta 3 veces (el usuario tiene 3 oportunidades para adivinar el número)
for i in range (3):
    
    # Este bloque try/except verifica si el valor ingresado por el usuario es un número entero válido
    try:
        # Solicita al usuario que introduzca un número y lo almacena en la variable guess
        guess = int(input("\nIngresa un número entre 1 y 10: "))
        
        # Verifica si el número ingresado está fuera del rango de 1 a 10
        if guess < 1 or guess > 10:
            print("Así no funcionará, intenta de nuevo con un número entre 1 y 10")
            continue
    except ValueError:
        # Si el usuario introduce algo que no es un número entero, imprime un mensaje de error y vuelve al inicio del bucle
        print("Así no funcionará, intenta de nuevo con un número entre 1 y 10")
        continue

    # Comprueba si el número ingresado por el usuario es igual al número aleatorio generado
    if guess==number:
        print("¡Adivinaste!")
        print(f"El número era  {number}. Has ganado $500")
        break
    else:
        # Si el número ingresado no es el correcto y el usuario ya ha realizado 3 intentos, imprime un mensaje de que el juego ha terminado
        if i==2:
            print(f"Lo sentimos, el número era {number}")
            print("No has adivinado :(")
        else:
            # Si el número ingresado no es el correcto y el usuario aún tiene intentos restantes, imprime un mensaje para que lo intente de nuevo
            print("Intentalo de nuevo")


    
