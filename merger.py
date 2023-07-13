import os
from PyPDF2 import PdfMerger

# Establecer la carpeta raíz
root_folder = 'Datos'

# Iterar sobre todas las subcarpetas en la carpeta raíz
for root, dirs, files in os.walk(root_folder):
    # Comprobar si la carpeta actual tiene exactamente 5 dígitos (es decir, es una de las carpetas que queremos)
    if len(os.path.basename(root)) == 5:
        # Crear una instancia de PdfMerger
        merger = PdfMerger()
        
        # Iterar sobre todos los archivos en la carpeta actual
        for file in files:
            # Comprobar si el archivo es un archivo PDF
            if file.endswith('.pdf'):
                # Agregar el archivo PDF a la fusión
                merger.append(os.path.join(root, file))

        # Guardar el archivo PDF fusionado con el nombre de la carpeta actual
        merger.write(os.path.join(os.path.dirname(root), os.path.basename(root) + '.pdf'))
        # Cerrar la instancia de PdfMerger
        merger.close()

