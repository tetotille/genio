from procesamiento import procesar
import cv2
from search import search
from coincidencias import contarCoincidencias
import glob

def busqueda(titulo_string,palabra_clave):
    resultados = search(palabra_clave, 1)
    definitivo = ""
    for resul in resultados:
        definitivo = definitivo+resul.description
    return definitivo

def busquedaPregunta(titulo_string = None, lista_palabras = None):
    definitivo = busqueda(titulo_string,titulo_string)
    coincidencias(definitivo,lista_palabras)

def coincidencias(definitivo,lista_palabras):
    texto = definitivo.lower()
    contarCoincidencias(texto, lista_palabras)

images = [cv2.imread(file) for file in glob.glob("./screenshots/*.png")]

for img in images:
    pregunta, opciones = procesar(img)
    print("\n\n\nLa pregunta es:\n" + pregunta)
    print("\nOpciones: ")
    for opcion in opciones: print(opcion)
    print("Respuestas:")
    busquedaPregunta(pregunta, opciones)
print("\n\n\n")
