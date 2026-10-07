# BINGO_v1 en Python

# Autor: Sergio Civera-Arroyo
# Fecha de creacion: 2026-10-07
# Esta versión realiza las siguientes acciones:
    # 1. Crear un carton con varios numeros aleatorios
    # 2. Ir sacando bolas/numeros aleatorios sin repetir
    # 3. Comprobar que numeros del carton han salido
    # 4. Mostrar cada numero que sale
    # 5. Detectar cuando se completa el carton


# Importamos las herramientas para trabajar con numeros aleatorios
import random

# Importamos herramientas relacionadas con el tiempo
import time

# Imprime la cabecera
print("#" *40)
print("Bienvenido al juego de Bingo! (BINGO_v1)")
print("#" *40)

# ETAPA 1: Crear un carton con varios numeros aleatorios

# Creamos un cartón con 5 números aleatorios entre 1 y 50
carton = random.sample(range(1, 51), 5)

# Mostramos el carton por pantalla
print("\nTu cartón tiene los siguientes números:", carton, "\n")

# ETAPA 2: Ir sacando bolas/numeros aleatorios sin repetir

# Sacamos todas las bolas del tirón
bombo = random.sample(range(1, 51), 50)
# Guardamos el número que ha salido en una variable
bola_salida = []

# Guardamos los números que del cartón que hayan salido
aciertos = []

# Recorremos las bolas del bombo una a una
for bola in bombo:

# ETAPA 3: COMPROMBAR QUE NÚMEROS DEL CARTÓN HAN SALIDO
    if bola in carton:
        print(f"El {bola} está en tu cartón\n")

        # Guardamos el número acertado
        aciertos.append(bola)

# ETAPA 4: Mostrar cada numero que sale
    print("Ha salido la bola", bola, "\n")
    time.sleep(0.6)
    # Guardamos la bola que ya ha salido
    bola_salida.append(bola)

# ETAPA 5: Detectar cuando se completa el carton
    if len(aciertos) == len(carton):
        print("¡BINGO!")
        break