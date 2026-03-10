#!/usr/bin/env python3
import sys
import os
import pyzipper
import array as arr

def encrypt_file(source_file, password):
    zip_name = source_file + ".zip"

    try:
        with pyzipper.AESZipFile(
            zip_name,
            'w',
            compression=pyzipper.ZIP_LZMA,
            encryption=pyzipper.WZ_AES
        ) as zf:
            zf.setpassword(password.encode())
            zf.setencryption(pyzipper.WZ_AES, nbits=256)
            zf.write(source_file, arcname=os.path.basename(source_file))

        print(f"[OK] File compressed with psswd : {zip_name}")

    except Exception as e:
        print(f"[ERROR] Impossible to compress file : {e}")


def decrypt_file(zip_file, password):
    output_dir = "./arch_extracted/" + zip_file + "_extracted"

    try:
        with pyzipper.AESZipFile(zip_file) as zf:
            zf.pwd = password.encode()
            zf.extractall(path=output_dir)

        print(f"[OK] File extracted in : {output_dir}")

    except RuntimeError:
        print("[ERROR] Incorrect Password.")
    except Exception as e:
        print(f"[ERROR] Impossible to uncompress file : {e}")

def main():
# Array(0, 1, 2, 3) & 1 is never use (mandatory, not optional) & 0 is never use (for having array2 = Arg2)
    tableauOptional = arr.array('i', [0, 0, 0, 0])
    optional = False
    
    if len(sys.argv) != 4:

        if len(sys.argv) <= 3 or not sys.argv[3].strip():
            tableauOptional[3] = 1
            optional = True

        if len(sys.argv) <= 2 or not sys.argv[2].strip():
            tableauOptional[2] = 1
            optional = True
        
        if len(sys.argv) <= 1 or not sys.argv[1].strip():
            optional = False
        
        if not optional:
            print("Usage : <archive.app> <file> <0 compress|1 uncompress> <password>")
            print("Default : <archive.app> <file> <0> <UnPack1t0>")
            print("APP : PYTHON=<python archive.py> | EXE=<archive>")
            sys.exit(1)
    
    if optional:
        file = sys.argv[1]
        if tableauOptional[2]:
            mode = "0"
        else:
            mode = sys.argv[2]
        if tableauOptional[3]:
            password = "UnPack1t0"
        else:
            password = sys.argv[3]
    else:
        file = sys.argv[1]
        mode = sys.argv[2]
        password = sys.argv[3]

    if not os.path.isfile(file):
        print("[ERROR] Input file is missing.")
        sys.exit(1)

    if mode == "0":
        encrypt_file(file, password)

    elif mode == "1":
        decrypt_file(file, password)

    else:
        print("[ERROR] Invalid : use 0 (compress) or 1 (uncompress)")
        sys.exit(1)


if __name__ == "__main__":
    main()

#INSTALL PYTHON
#Not Admin
#PowerShell> winget configure -f https://aka.ms/python-config
#
#MAKE EXE
#pip install pyinstaller
#pyinstaller --onefile file.py
#pyinstaller --onefile --icon=picture.ico archive.py
#
#Out:
#dist/
#   file.exe