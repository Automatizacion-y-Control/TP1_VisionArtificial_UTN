# Caso sintetico

## Archivos del caso sintetico

- Referencia visual: `assets/entradas/imagen_sintetica_referencia.png`
- Imagen sintetica generada: `assets/entradas/imagen_sintetica.png`
- Script generador: `scripts/generar_imagen_sintetica.py`

## Ejecucion del caso sintetico

La imagen sintetica puede regenerarse manualmente con:

```powershell
py -3 c_prototipado\scripts\generar_imagen_sintetica.py
```

Y el pipeline completo se ejecuta con:

```powershell
py -3 c_prototipado\scripts\pipeline_tp1.py --case sintetica
```

El comando genera todas las salidas intermedias en:

- `assets/salidas/sintetica/`

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

## Funcion del caso sintetico en el TP

El caso sintetico no busca representar una escena realista, sino ofrecer una condicion controlada para validar el comportamiento teorico del pipeline. Su valor dentro del TP es metodologico: permite observar con mayor claridad el efecto de cada etapa sobre figuras definidas por geometria simple.

## Justificacion de uso como referencia

La imagen seleccionada aporta:

- fondo negro uniforme,
- contraste alto respecto de los objetos,
- presencia de formas geometricas diferenciables,
- y una composicion apta para pensar una reconstruccion por codigo.

## Decision de prototipado

En el Sprint 2 se incorporo una referencia visual sintetica. En el Sprint 3 esa referencia se reemplaza, para efectos del pipeline, por una escena propia generada por codigo. La nueva version sintetica fue diseniada para dejar visibles cuatro situaciones utiles para el TP:

- una figura rectangular con hueco interno,
- una figura circular independiente,
- una brecha horizontal pequena entre componentes,
- y pequenos puntos aislados como ruido controlado.

Este diseno vuelve mas defendible el caso sintetico porque cada detalle responde a un objetivo de analisis morfologico.

## Lo que se espera observar

Sobre el caso sintetico interesa evaluar:

- segmentacion binaria mas limpia que en la imagen real,
- comportamiento teorico mas estable de Otsu,
- efectos morfologicos mas faciles de interpretar,
- y comparacion clara entre kernel `3x3` y `5x1`.

## Estado dentro del backlog

Este caso queda consolidado en el Sprint 3 como escena sintetica reproducible, manteniendo la referencia original solo como apoyo de trazabilidad y comparacion.

## Resultados obtenidos

### Segmentacion inicial

La escena sintetica responde de manera muy estable a la conversion a grises y a la binarizacion con Otsu. La separacion entre fondo y objetos es limpia, como era esperable en una composicion de alto contraste y fondo uniforme.

La cantidad de pixeles blancos en la binaria Otsu fue de `95722`, valor que se toma como referencia para comparar el bloque morfologico.

### Morfologia con kernel `3x3`

Los resultados cuantitativos fueron:

- erosion `3x3`: `92638`
- dilatacion `3x3`: `98894`
- apertura `3x3`: `95698`
- cierre `3x3`: `95722`

Interpretacion:

- la erosion reduce bordes y elimina parte del ruido controlado agregado a la escena,
- la dilatacion expande las regiones y refuerza uniones cercanas,
- la apertura conserva casi toda la estructura principal y remueve detalles pequenos,
- el cierre deja la misma cantidad de pixeles blancos que la binaria original, lo que indica que la escena fue diseniada para ser estable frente a esa operacion.

### Morfologia con kernel `5x1`

Los resultados cuantitativos fueron:

- erosion `5x1`: `92598`
- dilatacion `5x1`: `98882`
- apertura `5x1`: `95710`
- cierre `5x1`: `95722`

Interpretacion:

- el kernel `5x1` conserva el comportamiento general esperado,
- su efecto direccional se aprecia mejor en las brechas y estructuras alineadas horizontalmente,
- la pequena diferencia numerica respecto de `3x3` es coherente con una escena controlada y limpia.

### Conclusion del caso sintetico

Este caso valida el comportamiento teorico del pipeline en condiciones controladas. Por eso funciona como contraparte del caso real: permite explicar con mas claridad el efecto de cada operacion y luego contrastarlo con la respuesta menos ideal de la imagen capturada.
