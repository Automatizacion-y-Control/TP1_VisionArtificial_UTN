# Imagen digital y representacion matricial

## Alcance del documento

Este documento desarrolla los fundamentos de representacion de una imagen digital. Su objetivo es establecer la base conceptual necesaria para comprender por que OpenCV y NumPy pueden procesar imagenes como estructuras de datos.

## Imagen digital como estructura numerica

Una imagen digital es una representacion discreta de una escena visual. En lugar de trabajar con una superficie continua, el sistema almacena una grilla finita de muestras. Cada una de esas muestras corresponde a un pixel y contiene informacion visual cuantificada.

Desde una perspectiva computacional, una imagen es una estructura numerica organizada espacialmente. Esta idea es central en vision artificial porque todas las transformaciones posteriores actuan sobre esos valores.

## Pixel como unidad minima

El pixel es la unidad elemental de una imagen. Cada pixel posee una posicion dentro de la grilla y uno o varios valores asociados, segun el tipo de imagen.

De manera general:

- en una imagen en escala de grises, cada pixel almacena una intensidad,
- en una imagen color, cada pixel almacena tres componentes,
- en una imagen binaria, cada pixel representa la pertenencia a una de dos clases.

Esto implica que la imagen es discreta tanto en el espacio como en los valores que puede tomar.

## Representacion matricial

Las imagenes digitales se representan mediante matrices o arreglos multidimensionales.

- Imagen en escala de grises: `NxM`
- Imagen color: `NxMx3`

En estas expresiones, `N` representa la cantidad de filas y `M` la cantidad de columnas. En OpenCV y NumPy, la indexacion sigue la forma:

`imagen[fila, columna]`

o, si hay canales:

`imagen[fila, columna, canal]`

Esta notacion no es un detalle menor: explica como se accede a los datos y como se implementan las transformaciones sobre la imagen.

Las dimensiones y el tipo de dato de un arreglo NumPy pueden consultarse con `imagen.shape` e `imagen.dtype`. Para una imagen color de 1080x1920 pixeles, `shape` devuelve `(1080, 1920, 3)` y `dtype` devuelve `uint8`.

## Rango de intensidades y tipo de dato

En imagenes de 8 bits, cada componente toma valores enteros en el rango `0-255`. En OpenCV y NumPy el tipo de dato correspondiente es `uint8`. En una imagen de grises:

- `0` representa negro,
- `255` representa blanco,
- los valores intermedios representan distintos niveles de gris.

Este rango cuantizado es la base del histograma, de la umbralizacion y de toda decision posterior sobre intensidad.

El tipo de dato puede verificarse con `imagen.dtype`. Es importante tenerlo en cuenta porque ciertas operaciones, como restas entre imagenes, pueden producir desbordamiento si no se convierte el arreglo a un tipo con signo antes de operar.

## Imagen color y canales

Una imagen color se compone de tres canales. En muchos contextos se utiliza el modelo RGB, pero OpenCV trabaja internamente con el orden BGR. Cada canal puede entenderse como una matriz bidimensional con la intensidad correspondiente a ese color.

La imagen completa surge de la combinacion de esos tres canales. Esta estructura explica por que las imagenes color requieren mas informacion y tambien por que suelen convertirse a escala de grises antes de etapas de segmentacion.

## Imagen binaria

Una imagen binaria es una simplificacion extrema en la que cada pixel toma uno de dos valores posibles: `0` o `255`. Conceptualmente representa la pertenencia a dos clases, habitualmente fondo y objeto.

Esta representacion habilita directamente el uso de operaciones morfologicas, que actuan sobre la forma de las regiones resultantes.

## Conversion a escala de grises

La conversion a escala de grises reduce la imagen a un solo canal de intensidad luminosa. Esta simplificacion disminuye la complejidad del procesamiento y preserva una parte sustancial de la estructura visual.

El criterio usual no es un promedio simple, sino una ponderacion de canales definida por el estandar ITU-R BT.601 y asociada a la luminosidad percibida:

```
Y = 0.299 * R + 0.587 * G + 0.114 * B
```

El canal verde aporta mas al brillo observado que el rojo, y este mas que el azul. Esta ponderacion refleja la sensibilidad del sistema visual humano a cada longitud de onda. Los coeficientes suman exactamente 1.

En OpenCV, recordando que el orden de canales es BGR, la conversion se realiza con:

```python
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
```

Por esa razon, la escala de grises constituye una etapa adecuada de preparacion para la binarizacion.

## Coordenadas en la imagen

En procesamiento de imagenes, el origen del sistema de coordenadas se ubica en la esquina superior izquierda. La fila aumenta hacia abajo y la columna hacia la derecha.

Esta convencion difiere del plano cartesiano clasico, pero es la que gobierna el acceso a pixeles, el dibujo de figuras y la interpretacion de posiciones en OpenCV.

## Vinculo con el TP1

En el TP1 se procesaron dos imagenes, ambas cargadas como arreglos NumPy de tipo `uint8`:

- una imagen real, fotografia con dimensiones del orden de miles de pixeles por lado y tres canales BGR,
- una imagen sintetica, generada por codigo con dimensiones controladas, fondo negro y figuras geometricas de alto contraste.

Cada etapa del pipeline opera sobre esa matriz:

- la conversion a grises aplica la ponderacion ITU-R BT.601 y produce un arreglo `(N, M)`,
- la binarizacion con Otsu convierte ese arreglo en una mascara donde cada valor es `0` o `255`,
- las operaciones morfologicas modifican la forma de las regiones blancas actuando pixel a pixel segun la vecindad definida por el kernel.

En consecuencia, este documento constituye la base conceptual del pipeline implementado.
