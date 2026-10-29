from PIL import Image

img = Image.open("picture.png").convert("RGBA")
img = img.resize((256, 256), Image.LANCZOS)
#img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
img.save("picture_256.png")
