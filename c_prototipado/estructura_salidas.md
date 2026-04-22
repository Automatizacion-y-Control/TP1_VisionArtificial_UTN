# Estructura y convencion de salidas

## Proposito

Este documento define como se organizaran y nombraran las salidas del prototipo para asegurar trazabilidad entre ejecucion, analisis y presentacion.

## Ubicacion de resultados

Las salidas se separaran por caso:

- `assets/salidas/real/`
- `assets/salidas/sintetica/`

## Convencion de nombres

Cada salida debe incluir un prefijo numerico de etapa y una descripcion breve del contenido.

### Bloque base por caso

- `01_original.png`
- `02_grises.png`
- `03_binaria_otsu.png`
- `04_histograma_otsu.png`
- `05_erosion_3x3.png`
- `06_dilatacion_3x3.png`
- `07_apertura_3x3.png`
- `08_cierre_3x3.png`

### Bloque de sensibilidad del kernel

- `09_erosion_5x1.png`
- `10_dilatacion_5x1.png`
- `11_apertura_5x1.png`
- `12_cierre_5x1.png`

## Criterios de organizacion

- El mismo nombre de etapa debe repetirse en `real/` y `sintetica/`.
- La numeracion debe seguir el orden logico del pipeline.
- Si se guarda la figura sintetica generada por codigo, debe quedar identificada como recurso de entrada o como salida inicial reutilizable.
- Si se generan archivos auxiliares, deben nombrarse de modo consistente y sin romper la secuencia principal.

## Relacion con el TP1

Esta convencion permite relacionar rapidamente cada archivo con un punto del trabajo practico y simplifica la incorporacion posterior de imagenes y figuras en `d_presentacion/`.
