from PyPDF2 import PdfReader, PdfWriter

# Crea un objeto PdfReader
leer = PdfReader('Ley499.pdf')

# Crea un objeto PdfWriter
escribir = PdfWriter()

# Lee cada página y agrega al objeto PdfWriter
for numero in range(len(leer.pages)):
    pagina = leer.pages[numero]
    escribir.add_page(pagina)

# Nombre y ruta del archivo de salida
salida = "ruta_del_archivo_nuevo.pdf"

# Escribe el archivo de salida
with open(salida, "wb") as out_file:
    escribir.write(out_file)