from PIL import Image

background = Image.open("./screens/1585550654.5471761.jpg")
overlay = Image.open("./screens/1585550839.7763247.jpg")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_imag = Image.blend(background, overlay, 0.5)
new_imag.save("overlaid", "PNG")
