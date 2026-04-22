# Guia de reutilizacion para d_presentacion

## Proposito

Este documento resume como aprovechar los artefactos generados en `c_prototipado/` para construir `d_presentacion/` sin reprocesar el trabajo.

## Insumos ya disponibles

### Documentacion de soporte

- `README.md`
- `configuracion.md`
- `pipeline_tp1.md`
- `casos_de_prueba.md`
- `imagen_real.md`
- `imagen_sintetica.md`
- `analisis_kernel.md`
- `estructura_salidas.md`

### Scripts reutilizables

- `scripts/pipeline_tp1.py`
- `scripts/generar_imagen_sintetica.py`

Estos scripts no necesitan modificarse para reutilizar los resultados ya generados; solo deben ejecutarse nuevamente si se desea recalcular salidas o regenerar la escena sintetica.

### Entradas

- `assets/entradas/imagen_real.png`
- `assets/entradas/imagen_sintetica_referencia.png`
- `assets/entradas/imagen_sintetica.png`

### Resultados listos para incorporar

Por cada caso ya existen:

- imagen original,
- conversion a grises,
- binaria con Otsu,
- histograma con umbral,
- erosion `3x3`,
- dilatacion `3x3`,
- apertura `3x3`,
- cierre `3x3`,
- erosion `5x1`,
- dilatacion `5x1`,
- apertura `5x1`,
- cierre `5x1`.

## Uso recomendado en la presentacion

### Seccion de metodologia

Tomar como base:

- `pipeline_tp1.md`
- `configuracion.md`

### Seccion de casos de estudio

Tomar como base:

- `imagen_real.md`
- `imagen_sintetica.md`
- `casos_de_prueba.md`

### Seccion de resultados

Tomar las imagenes desde:

- `assets/salidas/real/`
- `assets/salidas/sintetica/`

### Seccion de analisis

Tomar como base:

- `analisis_kernel.md`

## Beneficio de esta organizacion

Con esta estructura, `d_presentacion/` no necesita volver a calcular resultados ni reinterpretar el flujo tecnico desde cero. Solo necesita seleccionar, ordenar y redactar el material ya producido en `c_prototipado/`.
