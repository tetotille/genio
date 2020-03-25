from __future__ import division   # fuerza aritmética no entera
from PIL import Image                      # funciones para cargar y manipular imágenes
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   # funciones para representación gráfica
import pytesseract
from time import time

def formatoProcesamiento(imagen):
    I1 = imagen.convert('L')
    a = np.asarray(I1,dtype=np.float32)  # convierte el objeto I1 en una matriz de tipo float32
    return a
    
def formatoImpresion(imagen):
    return Image.fromarray(imagen.astype(np.uint8))
##Para guardar
#I.save("Nombre.jpg")
start = time()
##################MAIN################
I = Image.open("imagen1.jpeg")

I = formatoProcesamiento(I)
titulo = I[445:593,44:497]
primera_opcion = I[598:692,68:475]
segunda_opcion = I[652:750,45:491]
tercera_opcion = I[751:849,44:493]

titulo=formatoImpresion(titulo)
primera_opcion=formatoImpresion(primera_opcion)
segunda_opcion=formatoImpresion(segunda_opcion)
tercera_opcion=formatoImpresion(tercera_opcion)

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\teto_\AppData\Local\Tesseract-OCR\tesseract.exe'

titulo_string = pytesseract.image_to_string(titulo)
if titulo_string[0]=="é": 
    titulo_string="¿"+titulo_string[1:-1]+"?"
print(titulo_string)
primera_string = pytesseract.image_to_string(primera_opcion)
print(primera_string)
segunda_string = pytesseract.image_to_string(segunda_opcion)
print(segunda_string)
tercera_string = pytesseract.image_to_string(tercera_opcion)
print(tercera_string)
#titulo.show()
#primera_opcion.show()
#segunda_opcion.show()
#tercera_opcion.show()



I = formatoImpresion(I)

#######################FIN###########################
elapsed = time()-start
print("\n")
print(elapsed)
