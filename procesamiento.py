from __future__ import division   # fuerza aritmética no entera
from PIL import Image                      # funciones para cargar y manipular imágenes
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   # funciones para representación gráfica
import pytesseract
from time import time

####################################PROCESAMIENTO DE IMAGEN###################################
def formatoProcesamiento(imagen):
    #I1 = imagen.convert('L')
    #I1.show()
    a = np.asarray(imagen,dtype=np.float32)  # convierte el objeto I1 en una matriz de tipo float32
    return a
    
def formatoImpresion(imagen):
    return Image.fromarray(imagen.astype(np.uint8))
##Para guardar
#I.save("Nombre.jpg")
##################MAIN################
def procesar(direccion):
    I = Image.open(direccion)

    I = formatoProcesamiento(I)
    titulo = I[420:580,44:497]
    primera_opcion = I[562:677,66:475]
    segunda_opcion = I[652:750,45:491]
    tercera_opcion = I[751:849,44:493]

    titulo=formatoImpresion(titulo)
    primera_opcion=formatoImpresion(primera_opcion)
    segunda_opcion=formatoImpresion(segunda_opcion)
    tercera_opcion=formatoImpresion(tercera_opcion)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\teto_\AppData\Local\Tesseract-OCR\tesseract.exe'

    titulo_string = pytesseract.image_to_string(titulo)
    if titulo_string[0]=="é": 
        titulo_string=" "+titulo_string[1:-1]+" "
        
    primera_string = pytesseract.image_to_string(primera_opcion)
    primera_string=primera_string.lower()

    segunda_string = pytesseract.image_to_string(segunda_opcion)
    segunda_string=segunda_string.lower()

    tercera_string = pytesseract.image_to_string(tercera_opcion)
    tercera_string=tercera_string.lower()

    #titulo.show()
    #primera_opcion.show()
    #segunda_opcion.show()
    #tercera_opcion.show()
    print(titulo_string+"\n"+primera_string+"\n"+segunda_string+"\n"+tercera_string)
    
    pregunta = titulo_string
    respuestas = set()
    respuestas.add(primera_string)
    respuestas.add(segunda_string)
    respuestas.add(tercera_string)
    return pregunta, respuestas
