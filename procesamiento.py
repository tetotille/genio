from __future__ import division   # fuerza aritmética no entera
from PIL import Image                      # funciones para cargar y manipular imágenes
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   # funciones para representación gráfica
import pytesseract
from time import time
from PIL import ImageFilter

import pyocr
import pyocr.builders
import sys

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
def procesar2(direccion):
    I = Image.open(direccion)

    I = formatoProcesamiento(I)
    titulo = I[420:580,44:497]
    primera_opcion = I[562:677,66:475]
    segunda_opcion = I[652:750,45:491]
    tercera_opcion = I[751:849,44:493]

    titulo=formatoImpresion(titulo)
    #primera_opcion=formatoImpresion(primera_opcion)
    #segunda_opcion=formatoImpresion(segunda_opcion)
    #tercera_opcion=formatoImpresion(tercera_opcion)

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
    #print(titulo_string+"\n"+primera_string+"\n"+segunda_string+"\n"+tercera_string)
    
    pregunta = titulo_string
    respuestas = set()
    respuestas.add(primera_string)
    respuestas.add(segunda_string)
    respuestas.add(tercera_string)
    return pregunta, respuestas

def procesar(I):
    #I = I.convert("L")
    I = formatoProcesamiento(I)
    #I = I[280:890,42:500]
    im = I[750:890,70:470]
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\teto_\AppData\Local\Tesseract-OCR\tesseract.exe'
    I=formatoImpresion(I)
    respuestas = pytesseract.image_to_string(I)
    respuestas = respuestas.split("\n\n")
    pregunta = respuestas.pop(0)
    for i in range(len(respuestas)):
        respuestas[i]=respuestas[i].lower()
    if pregunta[0]=="é": 
            pregunta=" "+pregunta[1:-1]+" "
    #print(pregunta)

    #print(respuestas)
    return pregunta, respuestas

def algo():  
    I = Image.open("imagen1.jpeg")
    #I.show()
    I1 = I.crop((30,230,510,890))
    #I.show()
    #a = I.quantize(100,1,100)
    #a.show()
    #I1 = I.filter(ImageFilter.EDGE_ENHANCE_MORE)
    #I1 = I1.filter(ImageFilter.CONTOUR)
    #I1 = I1.filter(ImageFilter.SMOOTH_MORE)
    #I1 = I1.quantize(100,1,100)
    #I1=I1.convert("CMYK")
    tools=pyocr.get_available_tools()
    if len(tools)==0:
        print("No OCR tool found")
        sys.exit(1)
    print(tools)
    tool = tools[0]
    respuestas = tool.image_to_string(I1,lang="esp",builder = pyocr.builders.TextBuilder())
    #respuestas = respuestas.split("\n\n")
    if len(respuestas)<4:
        I1 = I.crop((71,770,457,833))
        respuestas = respuestas + pytesseract.image_to_string(I1)
    print(respuestas)
    I1.show()
