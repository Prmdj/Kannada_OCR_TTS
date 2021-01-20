# Image to Text to Sppech conversion with intonation for regional language

### Libraries used:
1. Akshara-Jaana
2. gTTS

### Installation process
1. clone the repo
2. create a python3 virtual environment using the command : python -m venv <virtualenv_name>
3. install the necessary packages : pip install -r requirements.txt
4. install tessaract-ocr backend
5. install pdf2image backend
6. run the code: python KannadaImageToText.py ..\data\test.pdf ..\output\test.rtl && python KannadaTextToSpeech.py ..\output\test.rtl ..\output\test.mp3


output is stored in output folder
