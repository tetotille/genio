from PIL import Image

background = Image.open("screenshot1585458696.4355526.png")
overlay = Image.open("screenshot1585458619.8077714.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_imag = Image.blend(background, overlay, 0.5)
new_imag.save("overlaid", "PNG")
