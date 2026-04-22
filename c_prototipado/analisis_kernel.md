# Analisis de sensibilidad del kernel

## Proposito

Este documento compara el efecto de los kernels `3x3` y `5x1` sobre los dos casos del prototipo. La comparacion se apoya en observacion visual de las salidas y en una metrica simple: cantidad de pixeles blancos resultantes luego de cada operacion.

La metrica no reemplaza el analisis cualitativo, pero ayuda a respaldar tendencias de expansion, contraccion y conservacion estructural.

## Casos comparados

- Caso real: `assets/salidas/real/`
- Caso sintetico: `assets/salidas/sintetica/`

## Metrica utilizada

Para cada salida binaria o morfologica se contabilizo la cantidad de pixeles blancos. Este valor permite estimar si una operacion:

- reduce superficie blanca,
- expande superficie blanca,
- o conserva en gran medida la estructura segmentada.

## Resultados del caso real

### Valores observados

| Salida | Pixeles blancos |
|---|---:|
| Binaria Otsu | 3508309 |
| Erosion `3x3` | 3433014 |
| Dilatacion `3x3` | 3590449 |
| Apertura `3x3` | 3478393 |
| Cierre `3x3` | 3538889 |
| Erosion `5x1` | 3445736 |
| Dilatacion `5x1` | 3575892 |
| Apertura `5x1` | 3482514 |
| Cierre `5x1` | 3535192 |

### Interpretacion

- La erosion reduce la cantidad de pixeles blancos con ambos kernels, como era esperable.
- La dilatacion incrementa la superficie blanca con ambos kernels, reforzando bordes y pequenas uniones.
- La apertura deja menos superficie blanca que la binaria original, consistente con la eliminacion de detalles pequenos.
- El cierre deja mas superficie blanca que la binaria original, consistente con el relleno de huecos o pequenas discontinuidades.

### Diferencias entre `3x3` y `5x1`

- En el caso real, el kernel `5x1` erosiona menos que el `3x3`, lo que sugiere una retraccion menos uniforme.
- Tambien dilata ligeramente menos, lo que indica una expansion mas condicionada por la direccion horizontal.
- La diferencia entre aperturas y cierres es menor que en el sintetico, porque la imagen real contiene variaciones naturales de borde, textura y ruido.

## Resultados del caso sintetico

### Valores observados

| Salida | Pixeles blancos |
|---|---:|
| Binaria Otsu | 95722 |
| Erosion `3x3` | 92638 |
| Dilatacion `3x3` | 98894 |
| Apertura `3x3` | 95698 |
| Cierre `3x3` | 95722 |
| Erosion `5x1` | 92598 |
| Dilatacion `5x1` | 98882 |
| Apertura `5x1` | 95710 |
| Cierre `5x1` | 95722 |

### Interpretacion

- La erosion reduce claramente la superficie blanca, lo que confirma la retraccion de contornos y la eliminacion de ruido pequeno.
- La dilatacion incrementa la superficie blanca, como se espera al expandir regiones.
- La apertura deja un valor muy cercano al de la binaria original, lo que indica que elimina detalles pequenos pero conserva la estructura principal.
- El cierre deja exactamente la misma cantidad de pixeles blancos que la binaria original en este caso sintetico, lo que sugiere que la escena fue diseniada de manera estable frente a esa operacion.

### Diferencias entre `3x3` y `5x1`

- Las diferencias numericas son pequenas, pero coherentes con el diseno de la escena.
- El kernel `5x1` actua con preferencia horizontal, por lo que su efecto es mas visible en las pequenas brechas alineadas en ese eje.
- En una escena controlada, la anisotropia se interpreta mejor porque hay menos ruido incidental que en el caso real.

## Comparacion general entre ambos casos

- El caso real muestra una respuesta mas irregular y mas sensible a detalles del fondo y del borde del objeto.
- El caso sintetico exhibe un comportamiento mas limpio y predecible, lo que facilita validar la teoria morfologica.
- El kernel `3x3` produce una accion mas uniforme sobre la vecindad.
- El kernel `5x1` introduce direccionalidad y, por lo tanto, un comportamiento anisotropico mas evidente cuando existen discontinuidades horizontales.

## Conclusiones utiles para el TP

1. El cambio de kernel no solo modifica la magnitud del efecto, sino tambien su direccion predominante.
2. En la imagen real, la influencia del kernel se mezcla con ruido, textura e iluminacion no ideal.
3. En la imagen sintetica, la respuesta del algoritmo se aproxima mejor al comportamiento teorico esperado.
4. La comparacion entre ambos casos justifica por que el TP pide trabajar tanto con una escena real como con una sintetica.
