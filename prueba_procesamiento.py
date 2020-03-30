from procesamiento import procesar
import cv2
img = cv2.imread('./screens/1585539527.521269.jpg')
pregunta, opciones = procesar(img)

print("La pregunta es:\n" + pregunta)
print("\nOpciones: ")
for opcion in opciones: print(opcion)
