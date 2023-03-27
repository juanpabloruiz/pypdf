from PyPDF2 import PdfWriter, PdfReader
import io

# Captura la salida del print en una variable
buffer = io.StringIO()
print("Hola mundo!", file=buffer)

# Crear un nuevo archivo PDF de salida
output = io.BytesIO()
writer = PdfWriter()

# Agregar una página al archivo de salida
page = writer.add_blank_page(612, 792) # Tamaño de página estándar de EE. UU. de 8.5 x 11 pulgadas
page.mergePage(PdfReader(buffer.getvalue().encode('utf-8')).getPage(0))
writer.addPage(page)

# Escribir el archivo de salida
writer.write(output)

# Escribir el archivo de salida a disco
with open("salida.pdf", "wb") as f:
    f.write(output.getbuffer())
