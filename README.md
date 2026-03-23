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
pip install Pillow [PNGICOEXE]
pip install pyzipper [PACKARCHIVE]


NOTE: if pip is not recognized, you need to ensure your path should find pip*.exe (usually anything like "???\Python\Python313\Scripts")
NOTE²: summup about python rtsp => 1/ a try on "pip install pygobject [PVHEADSET]" => 2/ raised "ERROR: Dependency 'girepository-2.0' is required but not found" => 3/ lib "libgirepository-1.0-dev"
       4/ lib included in "pip install gstreamer-bundle [PVHEADSET]" (so not need "install pygobject") => for log inforamtion, have a look on https://gstreamer.freedesktop.org/download/
       5/ set "PYGI_DLL_DIRS" as environmeent variable => then error "ImportError: Could not deduce DLL directories, please set PYGI_DLL_DIRS"
       This error is explained: no compatibility between "GStreamer + PyGObject" & Python for versions [3.12, 3.13, 3.14]
       pip uninstall gstreamer-bundle
       SOLUTION: instead of gstreamer, install FFMPEG (https://www.gyan.dev/ffmpeg/builds/), for windows something as "ffmpeg-release-full.7z", unpack then add to PATH ("FFMPEG_ENV", "C:\Users\1stname.name\Documents\ffmpeg\bin")

PROMPT
  a) use a console, for example CMD
  b) Mind for this sheet & these tiny scripts: any script needs to be in same directory as the file to use
  c) be sure any environement variable is well set, and/or go inside the directory with python scripts
  d) check the python running: [python --version] => if it's a fail, use [py] as [py --version]

NOTE: in the minut I'm writing, the version in my side is: 3.14.3

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


2. Directory {SELENIUM} => CHECK COOKIES => [browserhdl.py]


3. Directory {PACKARCHIVE} => a tiny program as a "command-line" in order to compress easily (with password) => [archive.py]


4. Directory {PVHEADSET} => A TINY SERVER RTSP FOR FORWARDING MEDIA FLOWS => [pvheadset.py]
    SERVER RTSP: START SERVER CATCHING "STEREO MIX"
        a) install FFMPEG as described in a NOTE, top of this document
        b) watch sounds availabe in Windows:             CMD> control mmsys.cpl,,1
        c) watch sounds availabe in Windows from FFMPEG: CMD> ffmpeg -list_devices true -f dshow -i "dummy:"
        d) recover all available informations about an input media: CMD> ffmpeg -f dshow -list_options true -i audio="Mixage stéréo (Realtek(R) Audio)"
        e) sound&video: CMD> ffmpeg -hide_banner -f dshow -list_devices true -i dummy:
        f) test video low: ffmpeg -f dshow -i video="Integrated Webcam":audio="Réseau de microphones (Realtek(R) Audio)" -t 5 test.mp4
        g) check informations about a flow: ffprobe rtsp://127.0.0.1:8554/live


SOURCE: I write this page using some informations and code requested sometimes to Copilot. AI helps to improve speed of delivery but I don't find a sufficient quality. I check each result before I validate.
```
