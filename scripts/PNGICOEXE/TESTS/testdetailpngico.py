from PIL import Image, ImageOps, ImageChops

img = Image.open("picture.ico")
img = ImageOps.exif_transpose(img).convert("RGBA")
img = img.resize((256, 256), Image.Resampling.LANCZOS)

img.save("picture_output.ico", format="ICO", sizes=[(256, 256)])

with Image.open("picture_output.ico") as ico:
    decoded = ico.convert("RGBA")

# Comparer l'image originale et l'image relue
print("Identiques :", ImageChops.difference(img, decoded).getbbox() is None)

# Comparer avec l'image retournée verticalement
flipped = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
print("Identique au retournement vertical :",
      ImageChops.difference(flipped, decoded).getbbox() is None)

# Comparer avec une rotation de 180 degrés
rotated = img.transpose(Image.Transpose.ROTATE_180)
print("Identique à une rotation de 180° :",
      ImageChops.difference(rotated, decoded).getbbox() is None)