# Segmentacion de imagenes: binarizacion, histograma y metodo de Otsu

## Alcance del documento

Este documento desarrolla los fundamentos de segmentacion necesarios para el TP1, con foco en la binarizacion global, el analisis del histograma y el metodo de Otsu.

## Segmentacion como clasificacion de pixeles

La segmentacion es el proceso mediante el cual se divide una imagen en regiones o clases con significado. En el caso mas simple, la tarea consiste en separar el objeto de interes del fondo.

Desde esta perspectiva, segmentar equivale a clasificar pixeles segun un criterio. Ese criterio puede basarse en intensidad, color, textura o posicion. En el TP1, el criterio elegido es la intensidad en escala de grises.

## Binarizacion

La binarizacion es una forma elemental de segmentacion. Consiste en transformar una imagen de grises en una imagen con dos niveles posibles:

- `0` para una clase,
- `255` para la otra.

En general, una de esas clases representa el fondo y la otra representa el objeto de interes. La ventaja de esta representacion es que simplifica notablemente el analisis posterior y habilita el uso de operaciones morfologicas.

## Umbralizacion

Para binarizar una imagen se necesita un umbral `T`. La regla conceptual es simple:

- si la intensidad del pixel supera `T`, se lo asigna a una clase,
- si no lo supera, se lo asigna a la otra.

La dificultad no esta en la regla, sino en la eleccion del umbral. Segun como se determine ese valor, se distinguen distintos enfoques:

- umbralizacion fija, cuando el umbral se define manualmente,
- umbralizacion adaptativa, cuando varia segun la region de la imagen,
- umbralizacion automatica, cuando el algoritmo estima el umbral a partir de los datos.

## Histograma de niveles de gris

El histograma representa la distribucion de intensidades de la imagen. En el eje horizontal se ubican los niveles de gris y en el eje vertical la cantidad de pixeles correspondientes a cada nivel.

Su analisis es importante porque permite:

- observar como se distribuyen las intensidades,
- estimar si fondo y objeto estan bien diferenciados,
- justificar la calidad de una binarizacion,
- interpretar el valor de umbral elegido por Otsu.

El histograma, por lo tanto, no es solo una visualizacion auxiliar, sino una herramienta de analisis.

## Metodo de Otsu

El metodo de Otsu es una tecnica de umbralizacion global automatica. Su objetivo es encontrar el valor de umbral que mejor separa la imagen en dos clases, minimizando la varianza intraclase o, de manera equivalente, maximizando la separacion entre clases.

La principal ventaja del metodo es que evita seleccionar el umbral de forma manual. En lugar de ello, utiliza la informacion estadistica contenida en el histograma de la imagen.

Esto lo convierte en una herramienta especialmente apropiada para el TP1, donde se pide justificar la segmentacion sin recurrir a un ajuste arbitrario del umbral.

## Bimodalidad y calidad de segmentacion

El metodo de Otsu suele comportarse mejor cuando el histograma presenta una tendencia bimodal, es decir, cuando se distinguen dos agrupamientos principales de intensidades. En ese escenario, la separacion entre fondo y objeto es mas clara.

Sin embargo, si la imagen presenta ruido, iluminacion desigual o superposicion entre intensidades de fondo y objeto, la binarizacion puede perder eficacia. Esta limitacion es importante para interpretar por que la imagen real puede responder de manera distinta a la figura sintetica.

## Mascara binaria como salida util

El resultado de la binarizacion es una mascara binaria que separa las regiones de interes del fondo. Esa mascara no es todavia un resultado final: funciona como insumo para las etapas posteriores de analisis estructural y morfologia.

En otras palabras, la segmentacion constituye la condicion previa para que las operaciones morfologicas tengan sentido.

## Vinculo con el TP1

En el trabajo practico, este bloque teorico justifica tres acciones concretas:

1. convertir la imagen a escala de grises,
2. aplicar binarizacion global con Otsu,
3. analizar el histograma para evaluar la calidad de la separacion.

Por eso, este documento ocupa una posicion central dentro del soporte teorico del pipeline.
