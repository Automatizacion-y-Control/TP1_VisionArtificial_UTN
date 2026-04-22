# Diccionario de conceptos clave - TP1

## Proposito del documento

Este glosario reune terminos de consulta rapida vinculados al TP1. Su funcion es apoyar la lectura de los demas documentos de `b_investigacion/` y ofrecer definiciones breves, consistentes y orientadas al trabajo practico.

No busca reemplazar el desarrollo teorico de los documentos tematicos.

## A

### Anisotropia

Propiedad por la cual una operacion no actua del mismo modo en todas las direcciones. En morfologia aparece cuando el kernel tiene una geometria que privilegia un eje, como ocurre con un elemento estructurante de `5x1`.

### Apertura

Operacion morfologica compuesta por `erosion -> dilatacion`. Se utiliza para eliminar pequenos objetos o ruido externo preservando en lo posible la forma general de las estructuras principales.

## B

### Binarizacion

Proceso por el cual una imagen en escala de grises se transforma en una imagen con dos clases. Es la base sobre la que luego actuan las operaciones morfologicas.

### Binarizacion global

Metodo de umbralizacion que utiliza un unico valor para toda la imagen. En el TP1, la binarizacion global se realiza mediante el metodo de Otsu.

### Bimodalidad

Caracteristica de un histograma que presenta dos agrupamientos principales de intensidades. Es una condicion favorable para separar fondo y objeto mediante umbralizacion.

## C

### Cierre

Operacion morfologica compuesta por `dilatacion -> erosion`. Suele emplearse para rellenar pequenos huecos, suavizar discontinuidades y reforzar la conectividad de una region.

### Conversion a escala de grises

Transformacion que reduce una imagen color a un solo canal de intensidad luminosa. Constituye un paso previo habitual a la binarizacion.

## E

### Elemento estructurante

Matriz pequena que define la vecindad utilizada en una operacion morfologica. Tambien se denomina kernel.

### Erosion

Operacion morfologica que reduce las regiones blancas de una imagen binaria. Tiende a retraer bordes y eliminar detalles pequenos.

### Escala de grises

Representacion de una imagen mediante un unico canal de intensidad. Cada pixel suele tomar valores en el rango `0-255`.

## H

### Histograma

Representacion de la distribucion de intensidades de una imagen. Permite analizar la separacion entre clases y justificar la eleccion del umbral.

## I

### Imagen binaria

Imagen con dos niveles posibles por pixel, asociados normalmente a fondo y objeto. Es la forma de entrada mas habitual para la morfologia matematica.

### Imagen digital

Representacion numerica discreta de una escena visual. Se organiza como una matriz de pixeles.

## K

### Kernel

Sinonimo operativo de elemento estructurante. En el TP1 se analizan principalmente un kernel `3x3` y uno `5x1`.

## M

### Mascara binaria

Salida de la binarizacion que separa las regiones de interes del fondo. Funciona como base para el analisis estructural posterior.

### Metodo de Otsu

Algoritmo de umbralizacion automatica que determina un umbral global a partir del histograma, buscando separar la imagen en dos clases de manera estadisticamente conveniente.

### Morfologia matematica

Conjunto de operaciones destinadas a modificar la forma de los objetos presentes en una imagen binaria.

## N

### NumPy

Biblioteca de Python orientada al manejo de arreglos multidimensionales. OpenCV utiliza estas estructuras para representar imagenes.

## O

### Objeto de interes

Region de la imagen cuya deteccion o analisis resulta relevante para la tarea planteada.

### OpenCV

Biblioteca de codigo abierto para procesamiento de imagenes y vision por computadora. En Python se utiliza mediante el modulo `cv2`.

## P

### Pixel

Unidad minima de una imagen digital. Puede almacenar intensidad, color o pertenencia a una clase binaria.

### Pipeline

Secuencia de etapas de procesamiento en la que la salida de una fase pasa a ser la entrada de la siguiente.

## S

### Segmentacion

Proceso de dividir la imagen en regiones o clases con significado. En el TP1 se implementa mediante binarizacion.

## U

### Umbral

Valor de intensidad utilizado para decidir a que clase pertenece un pixel durante la binarizacion.

### Umbralizacion

Procedimiento general que utiliza uno o mas umbrales para separar pixeles en clases.

## V

### Varianza intraclase

Medida de dispersion de los valores dentro de cada clase. El metodo de Otsu busca minimizar esta magnitud para encontrar un umbral adecuado.

## Cierre

Los conceptos aqui reunidos forman un vocabulario minimo comun para interpretar los requisitos, justificar decisiones tecnicas y redactar luego la documentacion de presentacion del TP1.
