from procesamiento import procesar
import cv2
img = cv2.imread('./screenshots/screenshot1585519263.9247248.png')
pregunta, opciones = procesar(img)

print("La pregunta es:\n" + pregunta)
print("\nOpciones: ")
for opcion in opciones: print(opcion)
