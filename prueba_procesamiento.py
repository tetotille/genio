from procesamiento import procesar
import cv2
from search import search
from coincidencias import contarCoincidencias
from PIL import Image
from clave import palabraClave

def busqueda(pregunta,palabras_claves):
    resultados = search(palabras_claves, 1)
    google = ""
    for resul in resultados:
        google += resul.name
        google = google+resul.description
    return google

def busquedaPregunta(pregunta = None, lista_palabras = None):
    google = busqueda(pregunta,pregunta)
    coincidencias(google,lista_palabras)

def coincidencias(google,lista_palabras):
    texto = google.lower()
    contarCoincidencias(texto, lista_palabras)

nombre = '1585545189.148222.jpg'
img = Image.open('./screens/' + nombre)
pregunta, opciones = procesar(img)
pregunta = pregunta.replace("\n"," ")

print("La pregunta es:\n" + pregunta)
print("\nOpciones: ")
for opcion in opciones: print(opcion)



palabras_claves = palabraClave(pregunta)

print("PALABRA CLAVE: "+palabras_claves)
google = busqueda(pregunta,palabras_claves)
contarCoincidencias(google.lower(),opciones)
