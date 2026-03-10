```
####################################################################################
#                                 PYTHON Scripts
#
#                         Part from my scripts, for some usings
#
####################################################################################

                                      PREPARATION

INSTALL PYTHON (WINDOWS)
PowerShell> winget configure -f https://aka.ms/python-config

IDE for coding: VSCode
(URL) https://code.visualstudio.com

CHECK INSTALLED PYTHON MODULES (example, CMD)
py -m pip list

PRE-REQUISITES
pip install pyinstaller
pip install Pillow
pip install pyzipper [optional]

NOTE: if pip is not recognized, you need to ensure your path should find pip*.exe (usually anything like "???\AppData\Local\Programs\Python\Python313\Scripts")

PROMPT
  a) use a console, for example CMD
  b) Mind for this sheet & these tiny scripts: any script needs to be in same directory as the file to use
  c) be sure any environement variable is well set, and/or go inside the directory with python scripts
  d) check the python running: [python --version] => if it's a fail, use [py] as [py --version]

NOTE: in the minut I'm writing, the version in my side is: 3.13.12

---

                                      SCRIPTS

0. {SVG2BASE64}, Convert a SVG file into a BASE64 file
  py -c "import base64,sys;print('data:image/svg+xml;base64,'+base64.b64encode(open(sys.argv[1],'rb').read()).decode())" file.svg

1. Directory {PNGICOEXE} => CREATE ICO FROM PNG / CHECK ICO / ICO IN EXE

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


SOURCE: I write this page using some informations and code requested sometimes to Copilot. AI helps to improve speed of delivery but I don't find a sufficient quality. I check each result before I validate.
```
