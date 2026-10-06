# GENERADOR DE PI v1.0

# Este script calcula el valor de Pi con el número de decimales que se indique y lo guarda en un archivo de texto.
# Corresponde al paso 1 del proyecto "Explorador de Pi".

# Fecha de creación: 2026-10-06
# Autor: Sergio Civera-Arroyo

import time
time_init = time.time()
nombre = "Pi"
decimales = 10_000_000 # Escribir el número de decimales que se desea calcular.

print("Vamos a calcular el valor de", nombre, "con", decimales, "decimales")
print("Hora de inicio:", time.strftime("%H:%M:%S"))
from mpmath import mp

# Establecemos la precisión a 1 millón de decimales
mp.dps = decimales + 2 # Agregamos 2 decimales extra para compensar errores de redondeo

pi = str(mp.pi) # Convertimos el valor de pi a cadena de texto
print("Los primeros 50 decimales de", nombre,"son:", pi[:52]) # Imprimimos los primeros 50 decimales de pi (incluyendo el "3.")

# Solo queremos los decimales, podemos hacer un pequeño truco con el slicing de cadenas
pi = pi[2:] # Eliminamos los dos primeros caracteres "3."

# Guardamos el valor de pi en un archivo de texto
with open("data/pi_decimales.txt", "w") as archivo:
    archivo.write(pi) # archivo es una variable que representa el archivo abierto en modo escritura ("w")
# NOTA: al usar with no hay que cerrar el archivo, Python lo hace automáticamente al salir del bloque with

print("Hora de finalización:", time.strftime("%H:%M:%S"))
print("Tiempo total de ejecución:", round(time.time() - time_init, 2), "segundos")
print("El valor de", nombre, "con", decimales, "decimales ha sido guardado en el archivo data/pi_decimales.txt.")
print("No es necesario ejecutar este script de nuevo.")