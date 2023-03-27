import os
from PyPDF2 import PdfReader, PdfWriter

# Directorio con archivos PDF
directorio = "dir"

# Crea un objeto PdfWriter
escribir = PdfWriter()

# Itera sobre todos los archivos PDF en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".pdf"):
        # Crea un objeto PdfReader para cada archivo
        ruta_archivo = os.path.join(directorio, archivo)
        leer = PdfReader(ruta_archivo)

        # Agrega cada página al objeto PdfWriter
        for numero in range(len(leer.pages)):
            pagina = leer.pages[numero]
            escribir.add_page(pagina)

        # Nombre y ruta del archivo de salida
        ruta_salida = ruta_archivo

        # Escribe el archivo de salida
        with open(ruta_salida, "wb") as out_file:
            escribir.write(out_file)

        # Vacía el objeto PdfWriter para el siguiente archivo
        escribir = PdfWriter()
