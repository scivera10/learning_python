# EXPLORADOR DE PI v3.0

# Este script permite buscar patrones de números o letras entre los decimales de Pi y las letras generadas a partir de esos decimales.
# Corresponde al paso 3 del proyecto "Explorador de Pi".

# Fecha de creación: 2026-10-06
# Autor: Sergio Civera-Arroyo


def cargar_pi(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        pi = archivo.read()

    return pi

def cargar_pi_letras(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        pi_letras = archivo.read()

    return pi_letras


def buscar_patron(pi, patron):
    return pi.find(patron)


def main():

    pi = cargar_pi("data/pi_decimales.txt")
    pi_letras = cargar_pi_letras("data/pi_letras.txt")

    print("=" * 40)
    print("          EXPLORADOR DE π v3.0") 
    print("=" * 40)

    print(f"Decimales cargados: {len(pi):,}")
    print(f"Caracteres de letras cargados: {len(pi_letras):,}")

    while True:

        patron = input("\nPatrón a buscar (números o letras): ").strip()

        if patron.isdigit():
            posicion = buscar_patron(pi, patron)
            tipo = "decimal"

        elif patron.isalpha():
            patron = patron.upper()
            posicion = buscar_patron(pi_letras, patron)
            tipo = "letra"

        else:
            print("Debes introducir solamente números o solamente letras.")
            continue

        if posicion == -1:
            print(f"Patrón no encontrado.") 

        else:
            print(f"Encontrado en {tipo} {posicion + 1:,}")

        respuesta = input("\n¿Quieres realizar otra búsqueda? (s/n): ")
        respuesta = respuesta.strip().lower()
        if respuesta != "s":
            break
    print("\nHasta luego.")



main()