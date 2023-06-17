# Importa el módulo random para generar números aleatorios
import random

# Crea un bucle infinito
while True:
    # Imprime un menú de opciones para el usuario
    print(''' 1. Lanza el dado      2.Salir''')

    # Solicita al usuario que elija una opción y almacena la elección en la variable 'user'
    user = int(input("¿Qué quieres hacer?\n"))

    # Verifica si el usuario eligió la opción 1
    if user==1:
        # Si el usuario eligió lanzar el dado, genera un número aleatorio entre 1 y 6
        number=random.randint(1,6)
        # Imprime el número generado
        print(number, "\n")

    # Verifica si el usuario eligió la opción 2
    elif user==2:
        # Si el usuario eligió salir, rompe el bucle infinito y finaliza el programa
        break   

    # Si el usuario no eligió ni la opción 1 ni la opción 2, imprime un mensaje de error
    else: 
        print("Por favor, ingrese 1 o 2\n")
