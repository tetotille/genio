from __future__ import division   # fuerza aritmética no entera
from PIL import Image                      # funciones para cargar y manipular imágenes
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   # funciones para representación gráfica
import pytesseract
from time import time
from PIL import ImageFilter
import pyautogui

import pyocr
import pyocr.builders
import sys

import cv2

def formatoProcesamiento(imagen):
    I1 = imagen.convert('L')

    a = np.asarray(I1,dtype=np.uint8)  # convierte el objeto I1 en una matriz de tipo float32
    return a

def formatoImpresion(imagen):
    return Image.fromarray(imagen.astype(np.uint8))
##Para guardar
#I.save("Nombre.jpg")
#start = time()
##################MAIN################
def procesar():
    screenshot = pyautogui.screenshot(region=(860, 50, 325, 620))
    screenshot.save("./Screens/"+str(time())+".jpg")
    I = np.asarray(screenshot,dtype=np.float32)
    I = cv2.resize(I, (540,1170), interpolation = cv2.INTER_AREA)
    I=cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(I, 140, 255, cv2.THRESH_BINARY)
    I = thresh1

    titulo = I[445:593,44:497]
    primera_opcion = I[598:692,68:475]
    segunda_opcion = I[700:794,68:475]
    tercera_opcion = I[794:900,68:475]

#    a = formatoImpresion(I)
#    a.show()
#    a = formatoImpresion(titulo)
#    a.show()
#    a = formatoImpresion(primera_opcion)
#    a.show()
#    a = formatoImpresion(segunda_opcion)
#    a.show()
#    a.show()
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\teto_\AppData\Local\Tesseract-OCR\tesseract.exe'

    titulo_string = pytesseract.image_to_string(titulo)
    if titulo_string[0]=="é" or titulo_string[0]=="@":
        titulo_string=""+titulo_string[1:-1]+""

    primera_string = pytesseract.image_to_string(primera_opcion)
    segunda_string = pytesseract.image_to_string(segunda_opcion)
    tercera_string = pytesseract.image_to_string(tercera_opcion)

    return titulo_string, [primera_string,segunda_string,tercera_string]
