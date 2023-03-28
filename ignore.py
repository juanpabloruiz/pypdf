import os
import PyPDF4

# Ruta del directorio con archivos PDF de entrada
input_directory = "dir"

# Ruta del directorio para guardar archivos PDF de salida
output_directory = "dir"

# Iterar sobre todos los archivos PDF en el directorio de entrada
for file_name in os.listdir(input_directory):
    if file_name.endswith(".pdf"):
        # Construir rutas completas de entrada y salida
        input_path = os.path.join(input_directory, file_name)
        output_path = os.path.join(output_directory, file_name)

        # Abrir archivo PDF de entrada
        pdf_reader = PyPDF4.PdfFileReader(input_path)

        # Crear objeto para escribir PDF de salida
        pdf_writer = PyPDF4.PdfFileWriter()

        # Iterar sobre cada página del PDF de entrada
        for page_num in range(pdf_reader.getNumPages()):
            # Obtener página actual
            page = pdf_reader.getPage(page_num)

            # Obtener caja de media página
            media_box = page.mediaBox
            media_box_upper = media_box.getUpperRight_x(), media_box.getUpperRight_y() - (media_box.getUpperRight_y() * 0.1)
            media_box.setUpperRight(media_box_upper)

            media_box_lower = media_box.getLowerLeft_x(), media_box.getLowerLeft_y() + (media_box.getUpperRight_y() * 0.1)
            media_box.setLowerLeft(media_box_lower)

            # Agregar página modificada al objeto PdfFileWriter
            pdf_writer.addPage(page)

        # Escribir archivo de salida
        with open(output_path, "wb") as out_file:
            pdf_writer.write(out_file)

        # Cerrar archivos
        out_file.close()
        pdf_reader.stream.close()
