# Operaciones morfologicas y sensibilidad al kernel

## Alcance del documento

Este documento desarrolla las operaciones morfologicas requeridas en el TP1 y analiza la influencia del elemento estructurante sobre el resultado.

## Morfologia matematica en imagenes binarias

Las operaciones morfologicas son tecnicas de procesamiento orientadas a modificar la forma de los objetos presentes en una imagen binaria. Su interes no se centra en el color ni en la intensidad original, sino en la geometria de las regiones obtenidas luego de la segmentacion.

Por esa razon, estas operaciones se aplican con sentido una vez que la imagen ya fue convertida en una mascara binaria.

## Elemento estructurante o kernel

El comportamiento morfologico depende del elemento estructurante, tambien llamado kernel. Se trata de una pequena matriz que define la vecindad utilizada para evaluar cada pixel y determina la forma local de la operacion.

En el TP1 aparecen dos casos de interes:

- kernel cuadrado de `3x3`,
- kernel rectangular de `5x1`.

El primero tiende a producir un efecto mas uniforme, mientras que el segundo introduce una respuesta direccional.

## Erosion

La erosion reduce las regiones blancas de la imagen binaria. En terminos visuales, retrae los bordes de los objetos y elimina detalles pequenos.

Entre sus efectos mas habituales se encuentran:

- reduccion del tamano de los objetos,
- eliminacion de ruido fino tipo sal,
- ruptura de conexiones delgadas,
- adelgazamiento de contornos.

Su utilidad principal en el TP1 es observar como una operacion local puede limpiar estructuras pequenas a costa de perder espesor en los objetos.

## Dilatacion

La dilatacion produce el efecto opuesto: expande las regiones blancas y avanza los contornos hacia afuera.

Entre sus efectos mas comunes se encuentran:

- aumento del tamano de los objetos,
- union de regiones proximas,
- cierre de pequenas brechas,
- relleno de discontinuidades menores.

Esta operacion permite analizar como la conectividad de los objetos cambia cuando se favorece su expansion.

## Apertura

La apertura es una operacion compuesta formada por la secuencia:

`erosion -> dilatacion`

Su objetivo tipico es eliminar pequenos objetos o ruido externo preservando, en la medida de lo posible, la forma general de las estructuras mas grandes.

Desde el punto de vista interpretativo, primero se remueven detalles finos mediante erosion y luego se recupera parcialmente el tamano de los objetos restantes con la dilatacion.

## Cierre

El cierre es la operacion compuesta inversa:

`dilatacion -> erosion`

Su efecto caracteristico es consolidar las regiones blancas, unir componentes cercanos y rellenar pequenos huecos o discontinuidades internas.

En comparacion con la apertura, el cierre no busca remover objetos pequenos externos, sino reforzar la continuidad de los objetos ya presentes.

## Sensibilidad al kernel y anisotropia

Cuando cambia el kernel, cambia tambien la forma en que la operacion interactua con la imagen. Un kernel cuadrado trata la vecindad de un modo mas equilibrado, mientras que uno rectangular de `5x1` privilegia una direccion.

Este fenomeno se vincula con la anisotropia, es decir, con la dependencia del resultado respecto de la orientacion del elemento estructurante. En la practica, esto significa que ciertos bordes, huecos o conexiones pueden verse mas afectados en un eje que en otro.

## Vinculo con el TP1

El TP1 exige aplicar erosion, dilatacion, apertura y cierre sobre dos tipos de imagenes y repetir parte del analisis con un kernel rectangular. Por lo tanto, este documento justifica:

1. por que la morfologia debe hacerse sobre imagen binaria,
2. que efecto visual se espera de cada operacion,
3. por que la forma del kernel modifica el resultado,
4. como interpretar la comparacion entre imagen real e imagen sintetica.

En ese sentido, este archivo constituye el soporte conceptual directo del nucleo experimental del trabajo.
