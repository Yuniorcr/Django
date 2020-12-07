import os
try:
    os.remove("hola2.txt")
except FileNotFoundError as identifier:
    print("el archivo no se encontro")
