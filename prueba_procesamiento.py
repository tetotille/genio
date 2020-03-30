from procesamiento import procesar
import cv2
from search import search
from coincidencias import contarCoincidencias

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

nombre = 'screenshot1585520322.248481.png'
img = cv2.imread('./screenshots/' + nombre)
pregunta, opciones = procesar(img)

print("La pregunta es:\n" + pregunta)
print("\nOpciones: ")
for opcion in opciones: print(opcion)


print("Respuestas:")
busquedaPregunta(pregunta, opciones)
