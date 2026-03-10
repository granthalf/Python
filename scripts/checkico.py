from PIL import Image
from pathlib import Path

my_file_ico_name="picture.ico"
my_file_ico = Path(my_file_ico_name)

if my_file_ico.is_file():
    ico = Image.open(my_file_ico_name)
    print("Size found inside ICO :")
    for size in ico.info.get("sizes", []):
        print(size)

else:
       print("No ICO file found.")
