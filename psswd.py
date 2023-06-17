# Importa el módulo random para poder generar números aleatorios
import random

# Solicita al usuario que introduzca la longitud de la contraseña deseada y almacena el valor en la variable length
length = int(input("Length of the password: "))

# Define una cadena que contiene todos los caracteres posibles (letras minúsculas, números, letras mayúsculas, y caracteres especiales) que pueden ser utilizados en la contraseña
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# Genera la contraseña utilizando la función choices() del módulo random, que permite seleccionar elementos con reemplazo de la cadena s
# El número de elementos seleccionados es igual a length, el valor introducido por el usuario
# La función join() convierte la lista resultante de caracteres en una cadena
password = "".join(random.choices(s, k=length))

# Imprime la contraseña generada
print(password)