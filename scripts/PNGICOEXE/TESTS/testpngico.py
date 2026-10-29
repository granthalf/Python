from PIL import Image

with Image.open("picture.ico") as ico:
    print("Format :", ico.format)
    print("Taille principale :", ico.size)
    print("Nombre d'images :", getattr(ico, "n_frames", 1))

    for size in ico.ico.sizes():
        print("Taille disponible :", size)

