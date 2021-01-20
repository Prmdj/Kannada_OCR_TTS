from gtts import gTTS 
import os
import sys

# The text that you want to convert to audio
_, input_file, output_file = sys.argv

print(f'Reading from text {input_file}')
with open(sys.argv[1], 'r', encoding='utf-8') as f:
  mytext = f.read()

# Language in which you want to convert 
language = 'kn'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
print(f'Saving mp3 file {output_file}')
# Saving the converted audio in a mp3 file named 
myobj.save(sys.argv[2]) 