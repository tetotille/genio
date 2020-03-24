# Importamos la libreria OpenCv
import cv2 #esta librería es un poquito más rápida que la de pytesseract

# Abrimos la imagen
im = cv2.imread("example_02.jpg")

#si no te anda, podés descargar de la página y ubicar en esta carpeta y este comando va antes del to_string
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'


# Utilizamos el método "image_to_string"
# Le pasamos como argumento la imagen abierta con Pillow
texto = pytesseract.image_to_string(im)

print(texto)
