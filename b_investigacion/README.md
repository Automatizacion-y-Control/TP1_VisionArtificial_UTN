# Investigacion - TP1 Vision Artificial

## Proposito de la carpeta

La carpeta `b_investigacion/` reune documentacion de soporte para el desarrollo del TP1 de Vision Artificial. Su funcion es consolidar el marco conceptual minimo necesario para comprender los requisitos del trabajo, justificar decisiones tecnicas durante el prototipado y facilitar la redaccion posterior de la presentacion final.

Estos documentos no constituyen la entrega del TP en si misma. Son material de base, organizado para consulta y reutilizacion.

## Criterio de organizacion

La carpeta se divide en dos tipos de documentos:

- Resumenes de clases y herramientas, que recuperan ideas vistas en catedra y su traduccion a OpenCV.
- Documentos tematicos, que desarrollan con mayor foco conceptos necesarios para el TP1.

## Archivos incluidos

### Resumenes de clase y herramienta

- `01_resumenOpenCv_03y04.md`: sintesis del uso de OpenCV y NumPy como entorno de trabajo para imagenes digitales.
- `02_resumenProcesamiento_05.md`: sintesis de la clase de procesamiento binario y operaciones morfologicas.

### Documentos tematicos

- `03_imagen_y_representacion.md`: fundamentos de imagen digital, pixel, matriz, canales y escala de grises.
- `04_segmentacion.md`: segmentacion binaria, umbralizacion, histograma y metodo de Otsu.
- `05_operacionesMorfologicas.md`: erosion, dilatacion, apertura, cierre e influencia del kernel.

### Material de apoyo

- `diccionario.md`: glosario de consulta con terminos relevantes para el TP1.
- `backlog.md`: plan de mejora documental aplicado sobre esta carpeta.

## Alcance academico

El enfoque de esta carpeta es tecnico y de apoyo. Cada documento busca ser autocontenido, pero sin reemplazar la documentacion oficial de OpenCV ni el material de catedra. Cuando un concepto se repite en mas de un archivo, se lo hace solo en la medida necesaria para mantener la lectura independiente de cada documento.

## Relacion con el TP1

El contenido de `b_investigacion/` respalda directamente el pipeline solicitado en los requisitos:

1. comprension de la imagen como matriz de datos,
2. conversion a escala de grises,
3. binarizacion global con Otsu,
4. analisis mediante histograma,
5. aplicacion de operaciones morfologicas,
6. evaluacion de la influencia del kernel.

Por lo tanto, esta carpeta funciona como base teorica y metodologica para construir `c_prototipado/` y `d_presentacion/`.
