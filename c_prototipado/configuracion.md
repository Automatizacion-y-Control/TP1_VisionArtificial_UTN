# Configuracion tecnica del prototipo

## Proposito

Este documento registra las decisiones tecnicas iniciales del prototipado para asegurar consistencia entre implementacion, resultados y posterior presentacion.

## Entorno previsto

- Lenguaje principal: Python 3
- Biblioteca de vision artificial: OpenCV (`cv2`)
- Biblioteca numerica: NumPy
- Biblioteca de graficacion para histogramas: Matplotlib

## Casos de estudio requeridos

El prototipo debe trabajar con dos escenarios:

- una imagen real,
- una figura sintetica generada por codigo.

Ambos casos deben atravesar el mismo pipeline base para que los resultados sean comparables.

## Kernels de trabajo

Los elementos estructurantes definidos por los requisitos son:

- kernel cuadrado `3x3`,
- kernel rectangular `5x1`.

El primero se utilizara para el bloque morfologico principal. El segundo se utilizara para el analisis de sensibilidad del kernel.

## Convenciones generales

- Las salidas se guardaran separadas por caso: `real/` y `sintetica/`.
- Cada etapa del pipeline tendra un nombre estable.
- Se evitara mezclar archivos temporales con resultados finales de cada corrida.
- Los scripts deberan priorizar reproducibilidad y claridad antes que complejidad innecesaria.

## Supuestos iniciales

- Las imagenes de entrada se almacenaran dentro de `assets/entradas/`.
- La figura sintetica podra generarse por script y tambien guardarse como salida reutilizable.
- El pipeline se implementara de modo que cada etapa pueda guardarse de manera independiente.

## Pendientes de configuracion

- definir el nombre final de la imagen real seleccionada,
- definir el script principal o la organizacion de scripts,
- establecer parametros auxiliares de visualizacion para histogramas y guardado.
