from PIL import Image, ImageOps

import PIL
print(PIL.__version__)

def create_multi_icon(input_path, output_path):
    img = Image.open(input_path)
    
    # Appliquer l'orientation EXIF et la normaliser
    img = ImageOps.exif_transpose(img)
    
    # Convertir en RGBA
    img = img.convert("RGBA")
    
    # Retourner verticalement l'image
    img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    # Retourner les pixels verticalement avec une opération explicite
    img = img.crop((0, 0, img.width, img.height))
    pixels = img.load()
    for y in range(img.height // 2):
        y2 = img.height - 1 - y
        for x in range(img.width):
            pixels[x, y], pixels[x, y2] = pixels[x, y2], pixels[x, y]
        
    sizes = [(16, 16),(32, 32),(48, 48),(64, 64),(128, 128),(256, 256)]
    
    img.save(output_path, format="ICO", sizes=sizes)

create_multi_icon("picture_256.png", "picture.ico")
