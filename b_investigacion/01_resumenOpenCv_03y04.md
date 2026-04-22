# Resumen de Clases 03 y 04 - OpenCV y representacion de imagen

## Alcance del documento

Este resumen recupera los contenidos introductorios vinculados al uso de OpenCV y NumPy para trabajar con imagenes digitales. Su objetivo es registrar el marco instrumental con el que luego se implementan las etapas del TP1.

No desarrolla en profundidad segmentacion ni morfologia, ya que esos temas se tratan en documentos especificos de esta misma carpeta.

## OpenCV como herramienta de trabajo

OpenCV es una biblioteca de codigo abierto orientada al procesamiento de imagenes y a la vision por computadora. En Python se utiliza mediante el modulo `cv2`, que ofrece funciones para leer, convertir, mostrar, guardar y transformar imagenes.

Su relevancia para el TP1 es directa: permite implementar tanto la lectura de las imagenes como las operaciones de conversion, binarizacion y morfologia requeridas en los requisitos.

## Relacion entre OpenCV y NumPy

En Python, OpenCV representa las imagenes como arreglos multidimensionales de NumPy. Esto significa que una imagen no se manipula como un objeto abstracto, sino como una estructura de datos indexable y procesable matematicamente.

Desde este punto de vista:

- una imagen en escala de grises se modela como una matriz `NxM`,
- una imagen color se modela como una matriz `NxMx3`,
- cada posicion de la matriz corresponde a un pixel.

Esta relacion entre OpenCV y NumPy es clave porque conecta la teoria de imagen digital con su implementacion concreta.

## Representacion matricial de la imagen

El enfoque de trabajo presentado en clase parte de considerar a la imagen como una matriz de intensidades o de canales de color. En OpenCV y NumPy, el acceso tipico a un pixel sigue la forma:

`imagen[fila, columna]` o `imagen[fila, columna, canal]`

El origen de coordenadas se ubica en la esquina superior izquierda. La fila crece hacia abajo y la columna hacia la derecha. Esta convencion es importante para interpretar resultados, dibujar figuras sinteticas y manipular regiones de interes.

## Funciones basicas trabajadas

Entre las funciones iniciales mas relevantes se encuentran:

- `cv2.imread()`, para cargar imagenes desde archivo,
- `cv2.imshow()`, para visualizar resultados en una ventana,
- `cv2.waitKey()`, para mantener la visualizacion hasta una interaccion del usuario,
- `cv2.imwrite()`, para guardar salidas procesadas.

Estas herramientas constituyen el punto de partida de cualquier pipeline basico de procesamiento.

## Generacion de imagenes sinteticas

Otro aspecto importante introducido en estas clases es la posibilidad de construir figuras sinteticas con OpenCV. Mediante primitivas geometricas como rectangulos, circulos, lineas y poligonos, es posible crear imagenes artificiales con condiciones controladas.

Esto resulta especialmente util para el TP1 porque el enunciado solicita trabajar no solo con una imagen real, sino tambien con una figura sintetica. La generacion por codigo permite controlar:

- el fondo,
- las formas presentes,
- el contraste,
- la ubicacion de los objetos,
- y la ausencia o presencia intencional de ruido.

## Conversion a escala de grises

OpenCV implementa la conversion a escala de grises mediante funciones de cambio de espacio de color, como `cv2.cvtColor(..., cv2.COLOR_BGR2GRAY)`. Esta operacion reduce la imagen a un solo canal de intensidad y constituye el paso previo natural a la binarizacion.

Desde el punto de vista teorico, esta conversion se apoya en una ponderacion de canales que aproxima la percepcion humana de brillo. Por eso no se trata de un simple promedio entre componentes de color.

## Utilidad de este resumen para el TP1

Este documento sirve para fijar el marco de trabajo instrumental del TP1. En particular, deja establecidas tres ideas centrales:

1. una imagen es una estructura matricial manipulable,
2. OpenCV provee las funciones necesarias para operar sobre ella,
3. NumPy es la base de representacion y construccion de datos visuales.

Sobre esta base se apoyan luego la segmentacion y las operaciones morfologicas.
