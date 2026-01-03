import os

carpeta = "C:/xampp/htdocs/DAMPieroOlivares/Primero/Programacion"

for ruta, subdirs, archivos in os.walk(carpeta):
    print("Ruta:", ruta)
    print("Subcarpetas:", subdirs)
    print("Archivos:", archivos)
    print("-" * 40)
    