# Caso sintetico

## Archivos del caso sintetico

- Referencia visual: `assets/entradas/imagen_sintetica_referencia.png`
- Imagen sintetica generada: `assets/entradas/imagen_sintetica.png`
- Script generador: `scripts/generar_imagen_sintetica.py`

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
