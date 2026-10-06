# CONVERTIR PI A LETRAS v1.0

# Este script convierte los decimales de Pi a letras utilizando un alfabeto específico y guarda el resultado en un archivo de texto.
# Corresponde al paso 2 del proyecto "Explorador de Pi".

# Fecha de creación: 2026-10-06
# Autor: Sergio Civera-Arroyo

def pi_a_letras(pi):

    # Alfabeto utilizado para realizar la conversión.
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"    # Incluye la letra Ñ.

    # Variable donde iremos acumulando las letras resultantes.
    resultado = ""

    # Recorremos Pi desde la posición 0 hasta el final, avanzando de 2 en 2.
    for i in range(0, len(pi), 2):

        # Extraemos un bloque de 2 dígitos de PI.
        bloque = pi[i:i+2]

        # Convertimos el bloque de texto a número entero.
        numero = int(bloque)

        # Calculamos una posición válida dentro del alfabeto.
        # El operador % evita que el índice sea mayor que el número de letras disponibles.
        indice = numero % len(alfabeto)

        # Obtenemos la letra correspondiente a ese índice.
        letra = alfabeto[indice]

        # Añadimos la letra al resultado final.
        resultado += letra

    # Devolvemos el texto completo convertido.
    return resultado


# ============================================================
# PRUEBA DE LA FUNCIÓN
# ============================================================

# Cadena de prueba.
#pi = "041920150419211300161821040100"

# Convertimos la cadena numérica a letras.
#texto = pi_a_letras(pi)

# Mostramos el resultado de la prueba.
#print(texto)


# ============================================================
# EJECUCIÓN REAL DEL SCRIPT
# ============================================================

print("EJECUCIÓN REAL DEL SCRIPT")
print("#" * 40)
print("     CONVERTIR PI A LETRAS v1.0")
print("#" * 40)


# ------------------------------------------------------------
# 1. LEER EL ARCHIVO CON LOS DECIMALES DE PI
# ------------------------------------------------------------

# Abrimos el archivo en modo lectura ("r").
# Todo su contenido se guarda en la variable pi.
with open("data/pi_decimales.txt", "r", encoding="utf-8") as archivo:
    pi = archivo.read()


# Mostramos cuántos decimales se han leído.
print(f"\nEl archivo pi_decimales.txt contiene: {len(pi):,} decimales de pi.\n")


# ------------------------------------------------------------
# 2. CONVERTIR LOS DECIMALES DE PI A LETRAS
# ------------------------------------------------------------

# Llamamos a la función pi_a_letras().
# El resultado se guarda en la variable pi_letras.
pi_letras = pi_a_letras(pi)


# ------------------------------------------------------------
# 3. GUARDAR EL RESULTADO EN UN NUEVO ARCHIVO
# ------------------------------------------------------------

# Abrimos o creamos el archivo pi_letras.txt
# en modo escritura ("w").
# Después escribimos dentro todas las letras generadas.
with open("data/pi_letras.txt", "w", encoding="utf-8") as archivo:
    archivo.write(pi_letras)


# ------------------------------------------------------------
# 4. MOSTRAR EL RESULTADO FINAL
# ------------------------------------------------------------

# Informamos de cuántos decimales se han convertido
# y cuántas letras se han generado.
print(
    f"Se han convertido {len(pi):,} decimales de pi "
    f"a {len(pi_letras):,} letras y se han guardado "
    f"en el archivo pi_letras.txt.\n"
)