# 📖 Transcriptor pdf2text

Es una herramienta automatizada desarrollada en Python que utiliza tecnología de reconocimiento visual (OCR) para leer masivamente documentos (como diccionarios) en PDF y extraer todo su contenido, generando archivos de texto plano.

## 🛠️ Cómo usar el programa (instrucciones paso a paso)

Este programa no requiere instalación. Solo sigue estos pasos:

1. **Descarga:** ve a la sección de **[Releases](../../releases/latest)** (a la derecha de esta página) y descarga el archivo `.zip`.
2. **Descomprime:** extrae la carpeta completa en tu ordenador (por ejemplo, en el Escritorio).
3. **Entrada:** coge todos los diccionarios en formato `.pdf` que necesites transcribir y mételos dentro de la carpeta llamada `diccionarios_pdf`.
4. **Ejecución:** haz doble clic en el archivo ejecutable (el `.exe`). Se abrirá una ventana negra que te irá informando del progreso. No te asustes, es normal.
5. **Avisos sonoros:** puedes minimizar la ventana y seguir trabajando en otras cosas. El programa te avisará por sonido:
   - Sonará **1 pitido** cada vez que termine de convertir un diccionario.
   - Sonarán **3 pitidos rápidos** indicando que el trabajo total ha finalizado.
6. **Resultados:** cuando escuches los 3 pitidos, pulsa cualquier tecla para cerrar la ventana. Ve a la carpeta `diccionarios_txt` y ahí tendrás todos tus archivos de texto limpios y listos para añadir al corpus.

---

## 💻 Para desarrolladores (código fuente)

A nivel de arquitectura, el script, que es muy sencillo, actúa como director de orquesta combinando librerías estándar de Python para la lógica, módulos externos como puente de conexión, y motores binarios independientes (`Poppler` [conversión PDF → imagen] y `Tesseract` [OCR en la imagen]) para el procesamiento pesado.

### Requisitos del Sistema
Para ejecutar o modificar el `script.py` desde el código fuente, necesitas tener instalado localmente:
* **Python 3.x**
* **Tesseract OCR** (Actualizar la ruta `tesseract_cmd` en el script).
* **Poppler** (Actualizar la variable `RUTA_POPPLER` en el script).

### Instalación de dependencias
Instala las librerías necesarias ejecutando en tu terminal:
```bash
pip install pdf2image pytesseract tqdm
