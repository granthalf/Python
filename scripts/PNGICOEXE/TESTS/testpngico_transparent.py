from PIL import Image

with Image.open("picture.ico") as ico:
    print("Format :", ico.format)
    print("Taille :", ico.size)

    # Extraire explicitement la variante 256 x 256
    image_256 = ico.ico.getimage((256, 256))
    print("Format extrait :", image_256.format)
    print("Mode extrait :", image_256.mode)

    image_256.save("extrait_256.png")