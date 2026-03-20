import os
import re
import time
import winsound
from pdf2image import convert_from_path, pdfinfo_from_path
import pytesseract
from tqdm import tqdm

# --- RUTAS ---
DIRECTORIO_BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA_PDFS = os.path.join(DIRECTORIO_BASE, 'documentos_pdf')
CARPETA_SALIDA = os.path.join(DIRECTORIO_BASE, 'documentos_txt')
RUTA_POPPLER = os.path.join(DIRECTORIO_BASE, r'poppler-25.12.0\Library\bin')

# --- CONFIGURACIÓN DE TESSERACT ---
pytesseract.pytesseract.tesseract_cmd = os.path.join(DIRECTORIO_BASE, r'Tesseract-OCR\tesseract.exe')

def procesar_diccionario_a_txt(pdf_path, txt_path):
    nombre_archivo = os.path.basename(pdf_path)
    print(f"\n{'-'*50}")
    print(f"Procesando: {nombre_archivo}")
    print(f"{'-'*50}")
    
    print("[1/2] Analizando el documento...")
    info = pdfinfo_from_path(pdf_path, poppler_path=RUTA_POPPLER)
    total_paginas = info["Pages"]
    
    texto_completo = ""
    print(f"[2/2] Extrayendo texto a pleno rendimiento...")
    
    for num_pagina in tqdm(range(1, total_paginas + 1), desc="Progreso OCR", unit="pág"):
        imagen_pagina = convert_from_path(
            pdf_path, 
            first_page=num_pagina, 
            last_page=num_pagina, 
            dpi=300, 
            poppler_path=RUTA_POPPLER
        )[0]
        
        texto_pagina = pytesseract.image_to_string(imagen_pagina, config='--psm 3', lang='spa')
        texto_completo += texto_pagina + "\n"

    print("\nLimpiando texto (uniendo líneas cortadas)...")
    texto_limpio = re.sub(r'-\n+', '', texto_completo)
    texto_limpio = re.sub(r'(?<!\n)\n(?!\n)', ' ', texto_limpio)
    texto_limpio = re.sub(r'[ \t]+', ' ', texto_limpio)

    with open(txt_path, 'w', encoding='utf-8') as archivo_txt:
        archivo_txt.write(texto_limpio)
        
    print(f"✅ ¡ÉXITO! Diccionario guardado en: {os.path.basename(txt_path)}")

def main():
    if not os.path.exists(CARPETA_SALIDA):
        os.makedirs(CARPETA_SALIDA)

    archivos_pdf = [f for f in os.listdir(CARPETA_PDFS) if f.lower().endswith('.pdf')]
    total_archivos = len(archivos_pdf)
    
    print(f"¡Se han encontrado {total_archivos} documentos en la carpeta!")

    for indice, archivo in enumerate(archivos_pdf, start=1):
        print(f"\n>>> DICCIONARIO {indice} DE {total_archivos} <<<")
        ruta_pdf = os.path.join(CARPETA_PDFS, archivo)
        
        nombre_txt = archivo.replace('.pdf', '.txt')
        ruta_txt = os.path.join(CARPETA_SALIDA, nombre_txt)
        
        if os.path.exists(ruta_txt):
            print(f"⏭️ El archivo '{nombre_txt}' ya existe. ¡Nos lo saltamos para ahorrar tiempo!")
            continue
        
        # Si no existe, lo procesamos
        procesar_diccionario_a_txt(ruta_pdf, ruta_txt)
        
        # Pitido para avisar de la finalización
        winsound.Beep(1000, 500)

    print("\n🎉 ¡TODOS LOS documentos HAN SIDO PROCESADOS!")
    
    # Pitidos finales
    for _ in range(3):
        winsound.Beep(1500, 400)
        time.sleep(0.1)
        
    input("[Pulsa cualquier tecla para cerrar el programa]")

if __name__ == '__main__':
    main()
