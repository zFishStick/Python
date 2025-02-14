import numpy as np
from PIL import Image, ImageDraw

def circle_image(img):
    img = img.convert("RGBA")  # Assicura il formato RGBA

    # Ottieni altezza e larghezza
    height, width = img.size

    # Crea un'immagine in scala di grigi per la maschera
    lum_img = Image.new('L', [height, width], 0)

    # Disegna un cerchio bianco (255) sulla maschera
    draw = ImageDraw.Draw(lum_img)
    draw.pieslice([(0, 0), (height, width)], 0, 360, fill=255, outline="white")

    # Converti le immagini in array NumPy
    img_arr = np.array(img)
    lum_img_arr = np.array(lum_img)

    # Aggiungi la maschera come canale alfa all'immagine originale
    final_img_arr = np.dstack((img_arr[:, :, :3], lum_img_arr))

    # Converte nuovamente in immagine PIL
    return Image.fromarray(final_img_arr)
