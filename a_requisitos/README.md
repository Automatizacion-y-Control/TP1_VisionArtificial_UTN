# 📚 Datos de la Cátedra

**Materia:** Visión Artificial  
**Carrera:** Licenciatura en Automatización y Control  
**Facultad:** Universidad Tecnológica Nacional – Facultad Regional Córdoba  

**Docentes:**
- Ing. González, Hernando Alexis  
- Ing. Miklosa, Pablo
 
**TP1** Operaciones Morfológicas  
**Año:** 2026  
---

## 📌 1. Procedimiento

---

### 🔷 1.1 Objetivo general

El propósito de esta actividad es que el estudiante logre implementar y analizar una secuencia de operaciones morfológicas aplicadas al procesamiento de imágenes.

Se busca comprender de manera empírica cómo estas transformaciones alteran la estructura de los objetos según el elemento estructurante utilizado.

Además, se deberá documentar cada etapa del proceso, describiendo los cambios visuales y justificando los resultados obtenidos mediante capturas intermedias.

---

### 🔷 1.2 Prerrequisitos

Para el desarrollo del trabajo se requiere:

- Conocimientos básicos de Python y OpenCV  
- Conceptos fundamentales de:
  - Binarización  
  - Histograma  
  - Morfología matemática  

---

## 🔷 1.3 Parte 1: Elección de Imagen y Generación de Figura

El estudio se realizará sobre dos tipos de fuentes para contrastar el comportamiento del algoritmo:

---

### 🟢 1. Imagen real

Seleccionar una fotografía propia o de un banco de imágenes.

📌 Objetivo:
- Analizar comportamiento en condiciones reales  
- Evaluar ruido, iluminación y complejidad  

---

### 🟢 2. Figura sintética

Diseñar mediante código una imagen artificial con fondo negro que contenga al menos dos figuras geométricas (por ejemplo: círculos, rectángulos) con diferentes colores.

📌 Objetivo:
- Tener control total del escenario  
- Validar comportamiento teórico  

---

## 🔷 1.4 Parte 2: Aplicación de Operaciones Morfológicas

El siguiente flujo de trabajo debe aplicarse de forma independiente tanto a la imagen real como a la figura sintética.

---

### 🔹 1. Conversión a escala de grises

Realizar la transformación del espacio de color.

📌 Requisitos:
- Describir el método técnico utilizado (ej: ponderación de canales)  
- Justificar por qué es un paso crítico previo a la binarización  
- Incluir la imagen resultante  

---

### 🔹 2. Binarización global mediante el método de Otsu

Generar una máscara binaria.

📌 Requisitos:
- Explicar el fundamento del algoritmo de Otsu  
- Describir cómo determina automáticamente el umbral óptimo  
- Incluir la captura de la máscara  

---

### 🔹 3. Análisis de histograma

Visualizar la distribución de niveles de gris de las imágenes originales.

📌 Requisitos:
- Marcar el umbral calculado por Otsu  
- Analizar si la binarización fue efectiva  
- Evaluar la bimodalidad del histograma  

---

### 🔹 4. Erosión

Aplicar la operación utilizando un elemento estructurante (kernel) cuadrado de 3x3.

📌 Requisitos:
- Describir el efecto sobre los bordes  
- Analizar la eliminación de ruido tipo “sal” (píxeles blancos aislados)  

---

### 🔹 5. Dilatación

Aplicar utilizando el mismo kernel 3x3.

📌 Requisitos:
- Explicar cómo expande las fronteras  
- Analizar cómo cierra pequeñas brechas o huecos  

---

### 🔹 6. Operaciones compuestas

---

#### 🔸 Apertura (Opening)

Ejecutar la secuencia:


Erosión → Dilatación


📌 Requisitos:
- Explicar su utilidad para eliminar objetos pequeños  
- Analizar impacto sobre objetos grandes  

---

#### 🔸 Cierre (Closing)

Ejecutar la secuencia:


Dilatación → Erosión


📌 Requisitos:
- Explicar cómo une componentes cercanos  
- Analizar cómo rellena huecos internos  

---

### 🔹 7. Análisis de sensibilidad del kernel

Repetir los pasos 4 a 6 utilizando un kernel rectangular de 5x1.

📌 Requisitos:
- Analizar cómo la forma del kernel afecta la morfología  
- Evaluar el comportamiento direccional (anisotropía)  
- Comparar resultados entre:
  - Imagen real  
  - Imagen sintética  

---

## 🔷 1.5 Entregables

---

### 📌 Código fuente

- Archivos `.py` correctamente estructurados  
- Código comentado siguiendo buenas prácticas  
- Entrega en formato comprimido  

---

### 📌 Informe técnico

Documento en formato PDF que debe incluir:

- Desarrollo completo del TP  
- Capturas de cada etapa  
- Explicaciones técnicas  
- Análisis de resultados  
- Conclusiones  

---

## 🔷 1.6 Fecha de entrega

Fecha límite:


22/04/2026


---

## 🔷 1.7 Consideraciones finales

El trabajo no se limita a la implementación del código, sino que requiere una comprensión profunda del efecto de cada operación sobre la imagen.

Se espera que el estudiante pueda:

- Interpretar resultados  
- Justificar decisiones  
- Relacionar teoría con práctica  

---

**Buena suerte con el desarrollo.**