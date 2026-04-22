# README - Scripts de c_prototipado

## Proposito de esta carpeta

La carpeta `c_prototipado/scripts/` contiene los scripts Python que resuelven la parte ejecutable del TP1. Su funcion no es reemplazar la explicacion teorica ni la documentacion de presentacion, sino proveer una implementacion concreta, reproducible y comentada del pipeline de procesamiento.

Actualmente la carpeta contiene dos scripts principales:

- `pipeline_tp1.py`
- `generar_imagen_sintetica.py`

Ambos trabajan en conjunto:

- `generar_imagen_sintetica.py` construye la imagen sintetica controlada,
- `pipeline_tp1.py` ejecuta el procesamiento completo sobre la imagen real, la imagen sintetica o ambas.

## Problemas que resuelven estos scripts

### `generar_imagen_sintetica.py`

Resuelve el problema de contar con una escena sintetica reproducible, construida por codigo y no dependiente de una imagen externa improvisada. Esto es importante porque el TP exige una figura sintetica con fondo negro y figuras geometricas, y ademas conviene que esa escena este pensada especificamente para mostrar el efecto de la morfologia.

### `pipeline_tp1.py`

Resuelve el problema de ejecutar de forma consistente y automatizada todas las etapas del TP:

1. lectura de la imagen,
2. conversion a escala de grises,
3. binarizacion global con Otsu,
4. generacion del histograma con umbral marcado,
5. erosion, dilatacion, apertura y cierre con kernel `3x3`,
6. repeticion de esas operaciones con kernel `5x1`,
7. guardado ordenado de todas las salidas.

En otras palabras, convierte el enunciado del TP en una rutina reproducible que genera evidencia visual concreta.

## Requisitos de ejecucion

Estos scripts requieren:

- Python 3
- `opencv-python` (`cv2`)
- `numpy`

No dependen de `matplotlib`, lo cual fue una decision deliberada para evitar fallos por dependencias no instaladas durante el prototipado.

## Estructura de rutas utilizada

Ambos scripts trabajan con rutas relativas al repositorio y asumen la siguiente organizacion:

- `c_prototipado/assets/entradas/`
- `c_prototipado/assets/salidas/real/`
- `c_prototipado/assets/salidas/sintetica/`

Entradas principales:

- `c_prototipado/assets/entradas/imagen_real.png`
- `c_prototipado/assets/entradas/imagen_sintetica.png`

Salida sintetica generada:

- `c_prototipado/assets/entradas/imagen_sintetica.png`

## Uso de los scripts

### Generar la imagen sintetica

```powershell
py -3 c_prototipado\scripts\generar_imagen_sintetica.py
```

Este comando:

- crea la carpeta de entrada si no existe,
- genera la escena sintetica,
- y la guarda como `imagen_sintetica.png`.

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

## Script 1 - `generar_imagen_sintetica.py`

## Objetivo

Construir por codigo una imagen sintetica especificamente pensada para el TP1.

La escena resultante no es decorativa ni arbitraria. Fue diseniada para dejar visibles situaciones utiles en el analisis morfologico:

- un hueco interno,
- bordes curvos,
- una brecha horizontal pequena,
- y ruido controlado.

## Estructura general

Este script es intencionalmente pequeno. Tiene tres funciones principales:

- definir rutas,
- construir la imagen,
- guardarla en disco.

## Variables globales del script

### `SCRIPT_DIR`

Es la ruta de la carpeta donde vive el script.

### `PROTO_DIR`

Es la carpeta padre de `scripts/`, es decir, `c_prototipado/`.

### `INPUTS_DIR`

Apunta a `c_prototipado/assets/entradas/`.

### `OUTPUT_PATH`

Define la ruta final donde se guarda la imagen sintetica:

- `c_prototipado/assets/entradas/imagen_sintetica.png`

## Funcion `build_synthetic_image(width=900, height=600)`

### Proposito

Construir en memoria la imagen sintetica como un arreglo NumPy de tres canales.

### Parametros

- `width`: ancho de la imagen
- `height`: alto de la imagen

### Retorno

Devuelve una imagen `np.ndarray` en formato BGR, lista para ser guardada o procesada.

### Como funciona

1. Crea un lienzo negro con `np.zeros`.
2. Dibuja un rectangulo principal relleno.
3. Dibuja un hueco negro dentro del rectangulo.
4. Dibuja un circulo grande separado.
5. Dibuja dos bloques con una brecha horizontal entre ellos.
6. Agrega pequenos puntos blancos como ruido controlado.

### Por que esta composicion es util

- El **rectangulo con hueco** permite observar el efecto del cierre.
- El **circulo** permite estudiar cambios sobre contornos curvos.
- La **brecha horizontal** permite observar mejor el comportamiento del kernel `5x1`.
- El **ruido controlado** permite evidenciar erosion y apertura.

## Funcion `save_synthetic_image(output_path=OUTPUT_PATH)`

### Proposito

Guardar en disco la imagen sintetica generada.

### Parametro

- `output_path`: ruta donde se guardara la imagen

### Retorno

Devuelve la ruta final (`Path`) donde la imagen fue escrita.

### Como funciona

1. Se asegura de que la carpeta destino exista con `mkdir(parents=True, exist_ok=True)`.
2. Llama a `build_synthetic_image()`.
3. Guarda la imagen con `cv2.imwrite`.
4. Si el guardado falla, lanza una excepcion.

## Funcion `main()`

### Proposito

Servir como punto de entrada cuando el script se ejecuta directamente.

### Como funciona

1. Llama a `save_synthetic_image()`.
2. Imprime por consola la ruta donde se genero la imagen.

## Observacion de diseno

Este script no define clases porque el problema que resuelve es simple y procedural: generar una unica imagen controlada. Introducir una clase aca no agregaria claridad.

## Script 2 - `pipeline_tp1.py`

## Objetivo

Implementar el pipeline completo del TP sobre los casos definidos.

Este es el script principal del prototipo. Es el responsable de traducir el enunciado del TP a una secuencia ejecutable, generando todas las salidas intermedias necesarias para documentar el trabajo.

## Estructura general

El script esta organizado en cinco bloques conceptuales:

1. definicion de rutas y configuraciones,
2. definicion de kernels y casos,
3. funciones auxiliares de lectura, conversion y guardado,
4. funciones de procesamiento morfologico,
5. orquestacion de la ejecucion.

## Imports principales

### `argparse`

Se usa para leer el argumento `--case` desde la linea de comandos.

### `importlib.util`

Se usa para cargar dinamicamente `generar_imagen_sintetica.py` sin convertir la carpeta `scripts/` en un paquete Python formal.

### `dataclasses.dataclass`

Se usa para definir una estructura simple e inmutable para representar cada caso de procesamiento.

### `pathlib.Path`

Se usa para manipular rutas de forma clara y robusta.

### `cv2`

Biblioteca principal de procesamiento de imagenes.

### `numpy`

Se usa para definir kernels y construir arreglos auxiliares.

## Clase `CaseConfig`

```python
@dataclass(frozen=True)
class CaseConfig:
    name: str
    input_path: Path
    output_dir: Path
```

### Que representa

No es una clase orientada a objetos compleja. Es una **dataclass** simple que agrupa los datos minimos necesarios para procesar un caso:

- nombre del caso,
- ruta de entrada,
- carpeta de salida.

### Por que se usa una `dataclass`

Porque evita manejar estos tres datos como tuplas anonimas o diccionarios sueltos. La estructura queda mas clara y mas facil de leer.

### Sobre constructores

La clase **no define un constructor manual** (`__init__`). Ese constructor es generado automaticamente por `@dataclass`. Como ademas `frozen=True`, las instancias quedan inmutables una vez creadas.

## Configuraciones globales del script

### `PROJECT_ROOT`

Ubica la raiz del repositorio a partir de la ruta del script.

### `INPUTS_DIR`

Apunta a `c_prototipado/assets/entradas/`.

### `OUTPUTS_DIR`

Apunta a `c_prototipado/assets/salidas/`.

### `SCRIPTS_DIR`

Apunta a la carpeta `c_prototipado/scripts/`.

### `REAL_CASE`

Instancia de `CaseConfig` para el caso real.

### `SYNTHETIC_CASE`

Instancia de `CaseConfig` para el caso sintetico.

### `KERNEL_3X3`

Kernel cuadrado de unos de tamano `3x3`.

### `KERNEL_5X1`

Kernel rectangular horizontal de tamano `1x5`, que conceptualmente representa el `5x1` pedido por el TP pero en forma de matriz con cinco columnas y una fila.

## Funcion `parse_args()`

### Proposito

Leer el argumento `--case`.

### Que devuelve

Un `Namespace` de `argparse` con uno de estos valores:

- `real`
- `sintetica`
- `all`

### Que problema resuelve

Permite reutilizar el mismo script para distintos escenarios sin duplicar codigo.

## Funcion `load_synthetic_generator()`

### Proposito

Cargar dinamicamente el modulo `generar_imagen_sintetica.py`.

### Por que existe

Porque el pipeline necesita garantizar que la entrada sintetica exista antes de procesarla, pero sin depender de imports relativos complejos ni convertir la carpeta en paquete.

### Como funciona

1. Construye la ruta al archivo del generador.
2. Crea un `spec` con `importlib.util.spec_from_file_location`.
3. Carga el modulo en memoria.
4. Devuelve el modulo cargado.

## Funcion `ensure_output_dir(path)`

### Proposito

Crear la carpeta de salida si no existe.

### Problema que resuelve

Evita errores al intentar guardar resultados en directorios inexistentes.

## Funcion `load_image(image_path)`

### Proposito

Leer una imagen color desde disco.

### Retorno

Devuelve un `np.ndarray` en formato BGR.

### Comportamiento ante error

Si OpenCV no puede leer la imagen, se lanza `FileNotFoundError`.

## Funcion `save_image(path, image)`

### Proposito

Guardar una imagen en disco de manera controlada.

### Comportamiento ante error

Si `cv2.imwrite` falla, se lanza `RuntimeError`.

## Funcion `save_original(image, output_dir)`

### Proposito

Guardar la imagen original del caso con el nombre normalizado:

- `01_original.png`

### Por que existe

Centraliza la primera salida del pipeline y mantiene la convencion de nombres.

## Funcion `to_grayscale(image)`

### Proposito

Convertir la imagen color a escala de grises.

### Implementacion

Usa `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)`.

### Relacion con el TP

Este es el primer paso tecnico exigido por el enunciado.

## Funcion `apply_otsu(gray)`

### Proposito

Aplicar binarizacion global con Otsu.

### Retorno

Devuelve una tupla:

- umbral calculado,
- imagen binaria resultante.

### Implementacion

Usa `cv2.threshold` con:

- `cv2.THRESH_BINARY`
- `cv2.THRESH_OTSU`

## Funcion `create_histogram_image(gray, otsu_threshold)`

### Proposito

Generar una imagen de histograma sin depender de `matplotlib`.

### Problema que resuelve

En el entorno de prototipado, `matplotlib` no estaba disponible. Esta funcion produce una salida equivalente usando OpenCV y NumPy.

### Como funciona

1. Calcula el histograma con `cv2.calcHist`.
2. Lo normaliza respecto del valor maximo.
3. Crea un lienzo blanco.
4. Dibuja la curva del histograma como lineas sucesivas.
5. Dibuja una linea roja vertical en el umbral de Otsu.
6. Escribe el valor numerico del umbral sobre la imagen.

### Salida

Devuelve una imagen BGR lista para guardarse como:

- `04_histograma_otsu.png`

## Funcion `apply_morphology(binary, kernel)`

### Proposito

Aplicar sobre una mascara binaria las cuatro operaciones principales del TP.

### Retorno

Devuelve un diccionario con:

- `erosion`
- `dilatacion`
- `apertura`
- `cierre`

### Implementacion

Usa:

- `cv2.erode`
- `cv2.dilate`
- `cv2.morphologyEx(..., cv2.MORPH_OPEN, ...)`
- `cv2.morphologyEx(..., cv2.MORPH_CLOSE, ...)`

### Ventaja de este diseno

Agrupa resultados relacionados y permite luego guardarlos con una rutina comun.

## Funcion `save_kernel_results(results, output_dir, start_index, suffix)`

### Proposito

Guardar ordenadamente los resultados morfologicos de un kernel dado.

### Parametros

- `results`: diccionario devuelto por `apply_morphology`
- `output_dir`: carpeta destino
- `start_index`: numero inicial de la secuencia
- `suffix`: texto que identifica el kernel (`3x3` o `5x1`)

### Como funciona

Recorre las operaciones en un orden fijo:

1. erosion
2. dilatacion
3. apertura
4. cierre

y genera nombres como:

- `05_erosion_3x3.png`
- `10_dilatacion_5x1.png`

## Funcion `prepare_case_input(case)`

### Proposito

Garantizar que la entrada del caso exista antes de procesarlo.

### Comportamiento

- Si el caso es `real`, no hace nada.
- Si el caso es `sintetica`, carga el generador y crea la imagen sintetica automaticamente.

### Problema que resuelve

Evita que el usuario tenga que acordarse de generar manualmente la imagen sintetica antes de ejecutar el pipeline.

## Funcion `process_case(case)`

### Proposito

Ejecutar el pipeline completo de un caso.

### Este es el nucleo del script

La funcion realiza, en este orden:

1. crea la carpeta de salida,
2. garantiza la existencia de la entrada,
3. carga la imagen,
4. convierte a grises,
5. aplica Otsu,
6. genera histograma,
7. aplica morfologia con `3x3`,
8. aplica morfologia con `5x1`,
9. guarda todas las salidas,
10. informa por consola lo realizado.

### Por que es importante

Es la funcion que traduce directamente el enunciado del TP a una secuencia automatizada.

## Funcion `resolve_cases(case_name)`

### Proposito

Convertir el valor de `--case` en una tupla concreta de casos a procesar.

### Salidas posibles

- `real` -> solo caso real
- `sintetica` -> solo caso sintetico
- `all` -> ambos casos

## Funcion `main()`

### Proposito

Ser el punto de entrada del script.

### Como funciona

1. Lee argumentos.
2. Resuelve los casos solicitados.
3. Ejecuta `process_case` para cada uno.

## Flujo completo entre ambos scripts

Cuando se ejecuta:

```powershell
py -3 c_prototipado\scripts\pipeline_tp1.py --case sintetica
```

ocurre esta secuencia:

1. `pipeline_tp1.py` interpreta `--case sintetica`.
2. `resolve_cases()` devuelve `SYNTHETIC_CASE`.
3. `process_case()` llama a `prepare_case_input()`.
4. `prepare_case_input()` carga dinamicamente `generar_imagen_sintetica.py`.
5. El generador crea `imagen_sintetica.png`.
6. El pipeline procesa esa imagen y guarda todas las salidas.

## Decisiones de diseno importantes

### 1. Scripts pequenos y especializados

Se separo la generacion sintetica del pipeline principal para evitar mezclar responsabilidades.

### 2. Uso de `Path`

Todas las rutas se manejan con `pathlib`, lo que mejora legibilidad y reduce errores de concatenacion manual.

### 3. Convencion estricta de nombres

Las salidas tienen prefijos numericos para mantener el orden del pipeline y facilitar la reutilizacion en `d_presentacion/`.

### 4. Sin clases innecesarias

Solo se uso una `dataclass` simple porque era suficiente para encapsular configuraciones de caso. No hay jerarquias de clases ni constructores complejos porque el problema no lo necesitaba.

### 5. Fallo temprano ante errores

Las funciones de carga y guardado lanzan excepciones claras cuando algo falla. Esto evita errores silenciosos.

## Como leer estos scripts si se esta aprendiendo

La mejor estrategia es esta:

1. leer primero `generar_imagen_sintetica.py`,
2. luego leer en `pipeline_tp1.py`:
   - configuraciones globales,
   - `CaseConfig`,
   - `parse_args()`,
   - funciones de carga y guardado,
   - `apply_otsu()` y `apply_morphology()`,
   - `process_case()`,
   - `main()`.

De esa forma se entiende el flujo de lo simple a lo complejo.

## Relacion con otras carpetas del proyecto

- `a_requisitos/` define lo que habia que resolver.
- `b_investigacion/` aporta el marco teorico.
- `c_prototipado/scripts/` implementa el pipeline.
- `c_prototipado/assets/` guarda entradas y salidas.
- `d_presentacion/` reutiliza estas evidencias para construir la entrega final.

## Conclusiones

Estos scripts resuelven la parte ejecutable del TP de forma clara, reproducible y suficientemente modular. Su valor principal no esta solo en que "funcionan", sino en que transforman el enunciado del TP en un proceso concreto, verificable y reutilizable para la documentacion final.
