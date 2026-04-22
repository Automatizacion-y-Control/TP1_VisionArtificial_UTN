# Prototipado - TP1 Vision Artificial

## Proposito

La carpeta `c_prototipado/` contiene los artefactos tecnicos necesarios para implementar, ejecutar y registrar el pipeline del TP1. Su objetivo es transformar los requisitos del trabajo practico en una base operativa reproducible, ordenada y trazable.

Esta carpeta no reemplaza a `d_presentacion/`. Su funcion es concentrar la implementacion, las entradas, las salidas intermedias y la documentacion de apoyo al desarrollo.

## Estructura actual

- `backlog.md`: organizacion del trabajo por epicas, historias, sprints e incrementos.
- `configuracion.md`: decisiones tecnicas y supuestos de implementacion.
- `pipeline_tp1.md`: mapeo entre los requisitos del TP y las etapas del prototipo.
- `estructura_salidas.md`: convencion de nombres y ubicacion de resultados.
- `casos_de_prueba.md`: definicion de los casos real y sintetico que se procesan en el prototipo.
- `imagen_real.md`: justificacion tecnica del caso real.
- `imagen_sintetica.md`: criterio de diseno y uso del caso sintetico.
- `analisis_kernel.md`: comparacion entre kernels `3x3` y `5x1`.
- `guia_reutilizacion.md`: orientacion para trasladar resultados a `d_presentacion/`.
- `scripts/`: scripts Python del prototipo.
- `assets/entradas/`: imagenes de entrada del caso real y recursos asociados a la figura sintetica.
- `assets/salidas/real/`: resultados generados para la imagen real.
- `assets/salidas/sintetica/`: resultados generados para la figura sintetica.

## Flujo general de trabajo

1. seleccionar o generar la imagen de entrada,
2. ejecutar el pipeline definido para el caso correspondiente,
3. guardar las salidas intermedias con nombres normalizados,
4. documentar observaciones tecnicas,
5. reutilizar los resultados en `d_presentacion/`.

## Uso de scripts

### Generacion del caso sintetico

Para regenerar la imagen sintetica controlada:

```powershell
py -3 c_prototipado\scripts\generar_imagen_sintetica.py
```

Salida esperada:

- `c_prototipado/assets/entradas/imagen_sintetica.png`

### Ejecucion del pipeline para la imagen real

```powershell
py -3 c_prototipado\scripts\pipeline_tp1.py --case real
```

Entradas utilizadas:

- `c_prototipado/assets/entradas/imagen_real.png`

Salidas generadas:

- `c_prototipado/assets/salidas/real/01_original.png`
- `c_prototipado/assets/salidas/real/02_grises.png`
- `c_prototipado/assets/salidas/real/03_binaria_otsu.png`
- `c_prototipado/assets/salidas/real/04_histograma_otsu.png`
- `c_prototipado/assets/salidas/real/05_erosion_3x3.png`
- `c_prototipado/assets/salidas/real/06_dilatacion_3x3.png`
- `c_prototipado/assets/salidas/real/07_apertura_3x3.png`
- `c_prototipado/assets/salidas/real/08_cierre_3x3.png`
- `c_prototipado/assets/salidas/real/09_erosion_5x1.png`
- `c_prototipado/assets/salidas/real/10_dilatacion_5x1.png`
- `c_prototipado/assets/salidas/real/11_apertura_5x1.png`
- `c_prototipado/assets/salidas/real/12_cierre_5x1.png`

### Ejecucion del pipeline para el caso sintetico

```powershell
py -3 c_prototipado\scripts\pipeline_tp1.py --case sintetica
```

Este comando garantiza primero la disponibilidad de:

- `c_prototipado/assets/entradas/imagen_sintetica.png`

Y luego genera:

- `c_prototipado/assets/salidas/sintetica/01_original.png`
- `c_prototipado/assets/salidas/sintetica/02_grises.png`
- `c_prototipado/assets/salidas/sintetica/03_binaria_otsu.png`
- `c_prototipado/assets/salidas/sintetica/04_histograma_otsu.png`
- `c_prototipado/assets/salidas/sintetica/05_erosion_3x3.png`
- `c_prototipado/assets/salidas/sintetica/06_dilatacion_3x3.png`
- `c_prototipado/assets/salidas/sintetica/07_apertura_3x3.png`
- `c_prototipado/assets/salidas/sintetica/08_cierre_3x3.png`
- `c_prototipado/assets/salidas/sintetica/09_erosion_5x1.png`
- `c_prototipado/assets/salidas/sintetica/10_dilatacion_5x1.png`
- `c_prototipado/assets/salidas/sintetica/11_apertura_5x1.png`
- `c_prototipado/assets/salidas/sintetica/12_cierre_5x1.png`

### Ejecucion completa

Para regenerar ambos casos:

```powershell
py -3 c_prototipado\scripts\pipeline_tp1.py --case all
```

## Relacion con el TP1

El prototipo debe cubrir, para imagen real y figura sintetica:

1. conversion a escala de grises,
2. binarizacion global con Otsu,
3. histograma con umbral marcado,
4. erosion con kernel `3x3`,
5. dilatacion con kernel `3x3`,
6. apertura con kernel `3x3`,
7. cierre con kernel `3x3`,
8. repeticion del bloque morfologico con kernel `5x1`,
9. comparacion de resultados y analisis del efecto del kernel.

## Estado actual

El prototipo ya dispone de:

- estructura documental y de carpetas,
- pipeline funcional para el caso real,
- caso sintetico reproducible por codigo,
- salidas morfologicas para kernels `3x3` y `5x1`,
- y documentacion de analisis reutilizable para la etapa de presentacion.

En consecuencia, `c_prototipado/` ya puede considerarse una base operativa cerrada para alimentar `d_presentacion/`.
