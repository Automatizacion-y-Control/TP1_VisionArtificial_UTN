# Caso real

## Archivo seleccionado

- Ruta: `assets/entradas/imagen_real.png`
- Estado: seleccionado y normalizado por nombre

## Justificacion de eleccion

La imagen real elegida presenta un objeto principal relativamente simple, bien delimitado y sobre un fondo con baja complejidad visual. Esto la convierte en un buen caso para el TP1 porque:

- facilita la separacion inicial entre objeto y fondo,
- permite aplicar Otsu con una probabilidad razonable de segmentacion util,
- contiene forma externa e interior aprovechables para analizar la respuesta morfologica,
- y mantiene un nivel de realismo suficiente para observar desajustes propios de una escena no sintetica.

## Lo que se espera observar

En este caso interesa verificar:

- si la conversion a grises conserva adecuadamente la estructura del objeto,
- si el umbral obtenido por Otsu separa de forma aceptable el objeto del fondo,
- como afectan la erosion y la dilatacion al contorno,
- como responde el hueco o zona interna del objeto ante apertura y cierre,
- y que diferencias aparecen al cambiar de kernel `3x3` a `5x1`.

## Riesgos tecnicos esperables

Aunque la imagen es adecuada para el TP, pueden aparecer dificultades tipicas del caso real:

- sombras suaves o gradientes de iluminacion,
- pequenas imperfecciones en el fondo,
- ruido fino alrededor del objeto,
- borde no perfectamente nitido.

Estos factores no invalidan la imagen; de hecho, aportan interes al analisis experimental.

## Estado dentro del backlog

Este caso forma parte directa del Sprint 2 y sera el primero en atravesar el pipeline completo del prototipo.
