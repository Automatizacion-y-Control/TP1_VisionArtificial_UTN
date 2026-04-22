# TP1 - Operaciones Morfologicas

**Materia:** Vision Artificial  
**Carrera:** Licenciatura en Automatizacion y Control  
**Facultad:** Universidad Tecnologica Nacional - Facultad Regional Cordoba  
**Alumno:** Cristian Gonzalo Vera  
**Legajo:** 420581  
**Ano:** 2026

## Informe final

El informe tecnico completo del TP1 se encuentra en formato PDF:

**[d_presentacion/TP1_Informe.pdf](d_presentacion/TP1_Informe.pdf)**

Incluye portada, fundamento teorico, metodologia, desarrollo de ambos casos (real y sintetico), comparacion entre kernels y conclusiones, con todas las imagenes del pipeline incorporadas.

---

## Proposito del repositorio

Este repositorio contiene el desarrollo completo del Trabajo Practico N. 1 de Vision Artificial, centrado en la aplicacion y analisis de operaciones morfologicas sobre una imagen real y una imagen sintetica.

El trabajo fue organizado en etapas separadas para mantener trazabilidad entre:

- lo pedido por el enunciado,
- la investigacion teorica de soporte,
- el prototipado tecnico,
- y la presentacion final del TP.

## Estructura del proyecto

### `a_requisitos/`

Contiene el enunciado y los requisitos del trabajo practico. Es la fuente de verdad sobre lo que debia resolverse.

Archivo clave:

- [a_requisitos/README.md](a_requisitos/README.md)

### `b_investigacion/`

Reune la documentacion teorica y conceptual utilizada como soporte para el desarrollo del TP. Incluye fundamentos de imagen digital, segmentacion, Otsu, histograma, morfologia, OpenCV y un glosario de conceptos.

Archivos destacados:

- [b_investigacion/README.md](b_investigacion/README.md)
- [b_investigacion/03_imagen_y_representacion.md](b_investigacion/03_imagen_y_representacion.md)
- [b_investigacion/04_segmentacion.md](b_investigacion/04_segmentacion.md)
- [b_investigacion/05_operacionesMorfologicas.md](b_investigacion/05_operacionesMorfologicas.md)

### `c_prototipado/`

Contiene la implementacion tecnica del pipeline del TP, las imagenes de entrada, las salidas intermedias generadas y la documentacion asociada al desarrollo experimental.

Incluye:

- documentacion del prototipo,
- scripts Python,
- caso real,
- caso sintetico reproducible por codigo,
- resultados para kernels `3x3` y `5x1`,
- analisis comparativo y guia de reutilizacion.

Archivos destacados:

- [c_prototipado/README.md](c_prototipado/README.md)
- [c_prototipado/scripts/README.md](c_prototipado/scripts/README.md)
- [c_prototipado/scripts/pipeline_tp1.py](c_prototipado/scripts/pipeline_tp1.py)
- [c_prototipado/scripts/generar_imagen_sintetica.py](c_prototipado/scripts/generar_imagen_sintetica.py)
- [c_prototipado/analisis_kernel.md](c_prototipado/analisis_kernel.md)

### `d_presentacion/`

Contiene la version final orientada a entrega y presentacion.

Incluye dos formatos principales:

- un documento final en Markdown,
- un notebook preparado para Colab.

Archivos destacados:

- [d_presentacion/README.md](d_presentacion/README.md)
- [d_presentacion/colab/tp1.ipynb](d_presentacion/colab/tp1.ipynb)

## Resultado final del trabajo

El proyecto ya resuelve los puntos principales del TP:

1. seleccion de una imagen real,
2. construccion de una imagen sintetica por codigo,
3. conversion de ambas imagenes a escala de grises,
4. binarizacion global mediante Otsu,
5. analisis de histograma con umbral marcado,
6. aplicacion de erosion, dilatacion, apertura y cierre con kernel `3x3`,
7. repeticion del analisis morfologico con kernel `5x1`,
8. comparacion entre caso real y sintetico,
9. comparacion de sensibilidad del kernel,
10. documentacion tecnica y presentacion final.

## Como recorrer el repositorio

Si se quiere entender el trabajo de principio a fin, el orden recomendado es:

1. leer [a_requisitos/README.md](a_requisitos/README.md),
2. revisar la base teorica en [b_investigacion/README.md](b_investigacion/README.md),
3. ver la implementacion y resultados en [c_prototipado/README.md](c_prototipado/README.md),
4. consultar la version final en [d_presentacion/README.md](d_presentacion/README.md),
5. abrir [d_presentacion/colab/tp1.ipynb](d_presentacion/colab/tp1.ipynb) para la version ejecutable.

## Ejecucion del prototipo

Los scripts principales se encuentran en `c_prototipado/scripts/`.

### Generar la imagen sintetica

```powershell
py -3 c_prototipado\scripts\generar_imagen_sintetica.py
```

### Procesar solo la imagen real

```powershell
py -3 c_prototipado\scripts\pipeline_tp1.py --case real
```

### Procesar solo la imagen sintetica

```powershell
py -3 c_prototipado\scripts\pipeline_tp1.py --case sintetica
```

### Procesar ambos casos

```powershell
py -3 c_prototipado\scripts\pipeline_tp1.py --case all
```

Para una descripcion detallada del funcionamiento interno de estos scripts, ver:

- [c_prototipado/scripts/README.md](c_prototipado/scripts/README.md)

## Licencia

Este repositorio utiliza una licencia academica de uso educativo en espanol. Ver:

- [LICENSE](LICENSE)
