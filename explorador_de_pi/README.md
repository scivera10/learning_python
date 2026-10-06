# Explorador de Pi

Proyecto creado mientras aprendo Python.

El objetivo del proyecto es trabajar con los decimales de π, transformarlos en letras y permitir la búsqueda de patrones numéricos o de texto.

## Funcionamiento

El proyecto está dividido en tres pasos:

### 1. Generar los decimales de Pi

El script:

`generar_pi_v1.0.py`

calcula π con el número de decimales indicado y guarda los decimales en:

`data/pi_decimales.txt`

Actualmente está configurado para generar **10.000.000 de decimales**.

### 2. Convertir los decimales a letras

El script:

`convertir_pi_letras_v1.py`

lee los decimales generados anteriormente y los procesa de dos en dos.

Cada bloque de dos dígitos se convierte en una letra utilizando el siguiente alfabeto:

`ABCDEFGHIJKLMNÑOPQRSTUVWXYZ`

El resultado se guarda en:

`data/pi_letras.txt`

### 3. Explorar Pi

El script:

`buscar_pi_v3.0.py`

permite buscar:

- Secuencias de números entre los decimales de π.
- Secuencias de letras entre el texto generado a partir de esos decimales.

El programa indica la posición en la que aparece por primera vez el patrón buscado.

## Estructura del proyecto

```text
explorador_de_pi/
├── generar_pi_v1.0.py
├── convertir_pi_letras_v1.py
├── buscar_pi_v3.0.py
├── data/
├── README.md
└── requirements.txt
```

## Requisitos

Este proyecto utiliza Python y la librería `mpmath`.

Para instalarla:

```bash
pip install mpmath
```

## Ejecución

Los scripts deben ejecutarse en este orden:

```bash
python generar_pi_v1.0.py
python convertir_pi_letras_v1.py
python buscar_pi_v3.0.py
```

El primer script genera los decimales de π.

El segundo convierte esos decimales en letras.

El tercero permite realizar búsquedas sobre ambos conjuntos de datos.

## Objetivo del proyecto

Este proyecto forma parte de mi aprendizaje de Python.

Con él he practicado conceptos como:

- Variables
- Funciones
- Bucles
- Condicionales
- Manipulación de cadenas
- Lectura y escritura de archivos
- Entrada de datos por teclado
- Uso de librerías externas
- Organización de un proyecto en varios scripts

## Autor

Sergio Civera-Arroyo

## Estado

Primera versión del proyecto.

El proyecto podrá evolucionar en el futuro a medida que vaya aprendiendo nuevos conceptos de Python.
