# Pipeline del TP1

## Proposito

Este documento vincula los requisitos del TP1 con las etapas concretas que debe ejecutar el prototipo.

## Pipeline general

El flujo de procesamiento definido para ambos casos es el siguiente:

`imagen original -> escala de grises -> binarizacion Otsu -> histograma -> erosion -> dilatacion -> apertura -> cierre -> repeticion con kernel 5x1`

## Mapeo con los requisitos

### 1. Conversion a escala de grises

Objetivo:
obtener una representacion monocanal apta para segmentacion.

Salida esperada:
imagen en grises guardada por caso.

### 2. Binarizacion global mediante Otsu

Objetivo:
separar objeto y fondo mediante un umbral global calculado automaticamente.

Salida esperada:
mascara binaria y valor de umbral utilizado.

### 3. Analisis de histograma

Objetivo:
visualizar la distribucion de intensidades y marcar el umbral de Otsu para evaluar la calidad de la segmentacion.

Salida esperada:
grafico del histograma con referencia al umbral.

### 4. Erosion con kernel `3x3`

Objetivo:
observar reduccion de bordes y eliminacion de ruido fino.

### 5. Dilatacion con kernel `3x3`

Objetivo:
observar expansion de regiones y cierre de pequenas brechas.

### 6. Apertura con kernel `3x3`

Objetivo:
analizar eliminacion de objetos pequenos o ruido externo.

### 7. Cierre con kernel `3x3`

Objetivo:
analizar relleno de huecos y refuerzo de conectividad.

### 8. Repeticion con kernel `5x1`

Objetivo:
comparar el comportamiento morfologico al modificar la geometria del elemento estructurante.

## Casos obligatorios

Todas las etapas anteriores deben aplicarse de forma independiente a:

- la imagen real,
- la figura sintetica.

## Valor del pipeline para el TP

Este pipeline no solo cubre la implementacion pedida, sino que produce las evidencias visuales necesarias para justificar cada etapa del trabajo practico y sostener luego el analisis comparativo.
