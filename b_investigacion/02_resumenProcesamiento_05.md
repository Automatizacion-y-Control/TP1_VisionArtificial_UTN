# Resumen de Clase 05 - Procesamiento binario y morfologia

## Alcance del documento

Este resumen concentra los conceptos presentados en la clase dedicada al procesamiento de imagenes binarias y a las operaciones morfologicas. Su funcion es sintetizar el flujo de trabajo que luego se aplica en el TP1.

No reemplaza a los documentos tematicos sobre segmentacion y morfologia, sino que los antecede como una vision general del pipeline.

## Del color a la imagen binaria

La clase introduce una secuencia de procesamiento orientada a simplificar la imagen hasta obtener una representacion apta para el analisis estructural. Ese recorrido puede resumirse asi:

1. imagen original,
2. conversion a escala de grises,
3. umbralizacion,
4. generacion de imagen binaria,
5. refinamiento morfologico.

La idea central es que muchas operaciones geometricas no se aplican directamente sobre una imagen color, sino sobre una representacion binaria en la que el objeto de interes y el fondo queden separados.

## Binarizacion y umbralizacion

La binarizacion consiste en transformar una imagen de grises en una imagen con dos niveles de intensidad. Para ello se define un umbral que divide los pixeles en dos clases.

La clase repasa tres enfoques generales:

- umbralizacion fija,
- umbralizacion adaptativa,
- umbralizacion automatica mediante Otsu.

Para el TP1, el enfoque exigido es la binarizacion global con Otsu, ya que evita elegir manualmente el umbral y permite justificar la separacion a partir del histograma.

## Histograma como herramienta de analisis

El histograma describe la distribucion de niveles de gris presentes en una imagen. En el contexto de la umbralizacion, su importancia es doble:

- permite evaluar si existe una separacion razonable entre fondo y objeto,
- permite interpretar si el valor de umbral encontrado por Otsu resulta coherente.

Cuando el histograma presenta una tendencia bimodal, la aplicacion de Otsu suele ser mas efectiva. Cuando no existe esa separacion, la segmentacion puede ser mas inestable.

## Introduccion a la morfologia matematica

Una vez obtenida la imagen binaria, la clase presenta las operaciones morfologicas como herramientas para modificar la forma de los objetos. A diferencia de otras transformaciones centradas en intensidad o color, estas operaciones actuan sobre la estructura geometrica de las regiones blancas.

Las operaciones principales son:

- erosion,
- dilatacion,
- apertura,
- cierre.

Su comportamiento depende del elemento estructurante o kernel utilizado.

## Rol del kernel

El kernel define la vecindad con la que se analiza cada pixel y, por lo tanto, condiciona el resultado de la operacion. Un kernel cuadrado de `3x3` produce un efecto relativamente uniforme, mientras que un kernel rectangular de `5x1` introduce una componente direccional.

Esta diferencia es relevante para el TP1 porque uno de los objetivos es comparar como cambia la respuesta morfologica al modificar la geometria del kernel.

## Utilidad de este resumen para el TP1

Este documento deja fijado el encadenamiento conceptual que organiza el trabajo practico:

- primero se prepara la imagen,
- luego se segmenta,
- despues se observa su histograma,
- y finalmente se modifica su estructura con morfologia.

En ese sentido, funciona como puente entre los contenidos introductorios de herramienta y los documentos tematicos de segmentacion y operaciones morfologicas.
