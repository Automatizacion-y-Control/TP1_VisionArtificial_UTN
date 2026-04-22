# Casos de prueba del prototipo

## Proposito

Este documento identifica los dos casos obligatorios del TP1 y fija el criterio con el que seran procesados dentro del prototipo.

## Caso 1 - Imagen real

- Archivo de entrada: `assets/entradas/imagen_real.png`
- Tipo de caso: escena real capturada externamente
- Objetivo: evaluar el comportamiento del pipeline en una condicion no ideal, con posibles variaciones de iluminacion, textura y ruido.

Este caso permite analizar como responde la binarizacion con Otsu ante una imagen del mundo real y como las operaciones morfologicas modifican la forma del objeto segmentado.

## Caso 2 - Imagen sintetica reproducible

- Archivo de entrada: `assets/entradas/imagen_sintetica.png`
- Referencia adicional: `assets/entradas/imagen_sintetica_referencia.png`
- Tipo de caso: escena sintetica generada por codigo
- Objetivo: contar con un escenario controlado para validar el comportamiento teorico del pipeline.

Este caso se genera por script para asegurar reproducibilidad. La referencia inicial se conserva solo como apoyo visual y antecedente de diseno.

## Criterio comun de procesamiento

Ambos casos deben atravesar el mismo flujo base:

1. lectura de imagen,
2. conversion a escala de grises,
3. binarizacion global con Otsu,
4. histograma con umbral marcado,
5. operaciones morfologicas con kernel `3x3`,
6. repeticion del bloque morfologico con kernel `5x1`.

## Relacion con el backlog

- Sprint 2: implementacion y documentacion del caso real.
- Sprint 3: consolidacion del caso sintetico y su version generada por codigo.
- Sprint 4: comparacion de sensibilidad del kernel en ambos casos.
