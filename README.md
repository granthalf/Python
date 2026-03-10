####################################################################################
#                                 PYTHON Scripts
#
#                         Part from my scripts, for some usings
#
####################################################################################


CHECK INSTALLED PYTHON MODULES (example, CMD)
py -m pip list

PRE-REQUISITES
pip install pyinstaller
pip install Pillow
pip install pyzipper [optional]

PROMPT
  a) use a console, for example CMD
  b) Mind for this sheet & these tiny scripts: any script needs to be in same directory as the file to use
  c) be sure any environement variable is well set, and/or go inside the directory with python scripts
  d) check the python running: [python --version] => if it's a fail, use [py] as [py --version]

---

1. CREATE ICO / CHECK ICO / ICO IN EXE

  A. PNG => ICO
    a) Start from a PNG picture
    b) [pngto256.py] Size will be 256 x 256: from your picture, use "pngto256.py" to turn your picture into a resized pic 256x256 => [py pngto256.py]
    c) [pic2ico.py] Picture PNG will turn into a ico file => [py pic2ico.py]

  B. Check ICO file
    a) [checkico.py] Check the ICO file if the file has multi sizes inside (it is required: only 1 equals "it's not validated") => [py checkico.py]
    b) you can create a python exe program with this line code: [pyinstaller --onefile --icon=file.ico file.py]
    c) [checkicoinexe.py] Check the ico inside the exe file produced => [py checkicoinexe.py]

  C. VALIDATION ICO in EXE
    a) If you have found multi sizes, it's a win!
    b) If you have only 1 size, check all these steps again, and then try the refresh environment if it's run under windows.
  
  D. WINDOWS ENVIRONMENT: HOW TO REFRESH CACHE & CO
    a) run under a CMD [taskkill /IM explorer.exe /F]
    b) run under a CMD [del /A /Q "%localappdata%\IconCache.db"]
    c) run under a CMD [del /A /Q "%localappdata%\Microsoft\Windows\Explorer\iconcache*"]
    d) run under a CMD [start explorer.exe]
    e) Check if the ico is still displayed now. If the error is staying remaining, analyse why.


