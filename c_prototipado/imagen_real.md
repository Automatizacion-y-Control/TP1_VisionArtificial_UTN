# Caso real

## Archivo seleccionado

- Ruta: `assets/entradas/imagen_real.png`
- Estado: seleccionado y normalizado por nombre

## Ejecucion del caso real

Para procesar este caso se utiliza:

```powershell
py -3 c_prototipado\scripts\pipeline_tp1.py --case real
```

El comando genera todas las salidas intermedias en:

- `assets/salidas/real/`

Archivos resultantes:

- `01_original.png`
- `02_grises.png`
- `03_binaria_otsu.png`
- `04_histograma_otsu.png`
- `05_erosion_3x3.png`
- `06_dilatacion_3x3.png`
- `07_apertura_3x3.png`
- `08_cierre_3x3.png`
- `09_erosion_5x1.png`
- `10_dilatacion_5x1.png`
- `11_apertura_5x1.png`
- `12_cierre_5x1.png`

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

## Resultados obtenidos

### Segmentacion inicial

La conversion a grises conserva bien la estructura general del objeto y el metodo de Otsu produce una mascara util para el resto del pipeline. La segmentacion no es idealmente limpia como en un caso sintetico, pero resulta suficiente para observar el efecto de las operaciones morfologicas.

La cantidad de pixeles blancos en la binaria Otsu fue de `3508309`, lo que sirve como referencia para comparar el cambio producido por cada operacion.

### Morfologia con kernel `3x3`

Los resultados cuantitativos fueron:

- erosion `3x3`: `3433014`
- dilatacion `3x3`: `3590449`
- apertura `3x3`: `3478393`
- cierre `3x3`: `3538889`

Interpretacion:

- la erosion retrae el contorno y reduce pequenas regiones blancas,
- la dilatacion expande el objeto y refuerza la conectividad,
- la apertura limpia detalles externos y deja una superficie algo menor,
- el cierre incrementa levemente la superficie blanca, consistente con el relleno de pequenas discontinuidades.

### Morfologia con kernel `5x1`

Los resultados cuantitativos fueron:

- erosion `5x1`: `3445736`
- dilatacion `5x1`: `3575892`
- apertura `5x1`: `3482514`
- cierre `5x1`: `3535192`

Interpretacion:

- el kernel `5x1` produce un efecto menos uniforme que el `3x3`,
- la diferencia con el caso cuadrado es moderada, pero muestra una accion mas condicionada por la direccion horizontal,
- en una imagen real esta anisotropia aparece mezclada con irregularidades propias del borde y del fondo.

### Conclusion del caso real

Este caso confirma que el pipeline funciona sobre una imagen no ideal y que las operaciones morfologicas mantienen el comportamiento esperado aun en presencia de pequenas variaciones de iluminacion, textura y ruido. Precisamente por eso es un buen caso para el TP: no es artificiosamente perfecto, pero sigue siendo analizable.
