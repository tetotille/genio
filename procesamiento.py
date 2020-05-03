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
global numerodic
numerodic = {"cero":0,"uno":1,"dos":2,"tres":3,"cuatro":4,"cinco":5,"seis":6,
    "siete":7,"ocho":8,"nueve":9,"diez":10,"once":11,"doce":12,"trece":13,"catorce":14,"quince":15}
#COMENTARIO
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
def procesar(screenshot):
    global numerodic
    I = np.asarray(screenshot,dtype=np.float32)
    I=cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

    #ret, thresh1 = cv2.threshold(I, 140, 255, cv2.THRESH_BINARY)
    #I = thresh1
    #Image.fromarray(I.astype(np.float32)).show()
    titulo = I[244:320,28:282]
    primera_opcion = I[317:370,35:282]
    segunda_opcion = I[370:426,35:282]
    tercera_opcion = I[426:486,35:282]
    titulo = cv2.resize(titulo, (508,152), interpolation = cv2.INTER_AREA)

    primera_opcion = cv2.resize(primera_opcion, (770,219), interpolation = cv2.INTER_AREA)

    segunda_opcion = cv2.resize(segunda_opcion, (770,168), interpolation = cv2.INTER_AREA)
    tercera_opcion = cv2.resize(tercera_opcion, (770,180), interpolation = cv2.INTER_AREA)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\teto_\AppData\Local\Tesseract-OCR\tesseract.exe'
    pregunta = pytesseract.image_to_string(titulo)

    if pregunta[0]=="é" or pregunta[0]=="@" or pregunta[0] == "2":
        pregunta=""+pregunta[1:-1]+""

    primera_string = pytesseract.image_to_string(primera_opcion).lower()
    segunda_string = pytesseract.image_to_string(segunda_opcion).lower()
    tercera_string = pytesseract.image_to_string(tercera_opcion).lower()
    if primera_string in numerodic:
        primera_string = str(numerodic[primera_string])
    if segunda_string in numerodic:
        segunda_string = str(numerodic[segunda_string])
    if tercera_string in numerodic:
        tercera_string = str(numerodic[tercera_string])
    return pregunta, [primera_string,segunda_string,tercera_string]
