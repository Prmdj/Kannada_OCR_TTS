# Image to Text to Sppech conversion with intonation for regional language

### Libraries used:
1. Akshara-Jaana
2. gTTS

### Installation process
1. clone the repo
2. create a python3 virtual environment using the command : python -m venv <virtualenv_name>
3. install the necessary packages : pip install -r requirements.txt
4. install tessaract-ocr backend
   1. download tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe (64 bit) resp. from https://github.com/UB-Mannheim/tesseract/wiki
   2. under additional script data check Kannada Script
   3. under additional language data check Kannada
   4. add new environment variable path in system variable ex: C:\Program Files\Tesseract-OCR
5. install pdf2image backend
   1. download poppler-0.54_x86 from http://blog.alivate.com.au/poppler-windows/
   2. extract the zipped file to Program files ex: C:\Program Files\poppler-0.54_x86
   3. add new environment variable path in system variable ex: C:\Program Files\poppler-0.54_x86\bin
6. run the code: python KannadaImageToText.py ..\data\test.pdf ..\output\test.rtl && python KannadaTextToSpeech.py ..\output\test.rtl ..\output\test.mp3


output is stored in output folder
