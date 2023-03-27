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

        # Itera sobre cada página del archivo
        for numero in range(len(leer.pages)):
            # Crea un objeto PdfReader para la página actual
            pagina = leer.pages[numero]
            reader = PdfReader()
            reader.addPage(pagina)

            # Extrae el texto del cuerpo de la página
            parts = []
            def visitor_body(text, cm, tm, fontDict, fontSize):
                y = tm[5]
                if y > 50 and y < 720:
                    parts.append(text)
            reader.extract_text(visitor_text=visitor_body)
            text_body = "".join(parts)

            # Agrega cada página al objeto PdfWriter
            escribir.add_page(pagina)

        # Nombre y ruta del archivo de salida
        ruta_salida = ruta_archivo

        # Escribe el archivo de salida
        with open(ruta_salida, "wb") as out_file:
            escribir.write(out_file)

        # Vacía el objeto PdfWriter para el siguiente archivo
        escribir = PdfWriter()
