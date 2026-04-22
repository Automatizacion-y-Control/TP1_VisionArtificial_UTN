# Prototipado - TP1 Vision Artificial

## Proposito

La carpeta `c_prototipado/` contiene los artefactos tecnicos necesarios para implementar, ejecutar y registrar el pipeline del TP1. Su objetivo es transformar los requisitos del trabajo practico en una base operativa reproducible, ordenada y trazable.

Esta carpeta no reemplaza a `d_presentacion/`. Su funcion es concentrar la implementacion, las entradas, las salidas intermedias y la documentacion de apoyo al desarrollo.

## Estructura actual

- `backlog.md`: organizacion del trabajo por epicas, historias, sprints e incrementos.
- `configuracion.md`: decisiones tecnicas y supuestos de implementacion.
- `pipeline_tp1.md`: mapeo entre los requisitos del TP y las etapas del prototipo.
- `estructura_salidas.md`: convencion de nombres y ubicacion de resultados.
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

## Estado del Sprint 1

En este incremento se deja lista la base documental y estructural del prototipo. La implementacion de scripts y la generacion de resultados se desarrollaran en los siguientes sprints.
