'''
Wikipedia Text To Audio Program
# Wikipedia: Python thrid-party library that makes it easy to access and parse data from Wikipedia
# GTTS(Google Text To Speech): Third-party Python library to interface with Google Translate's text-to-speech API
'''

# Import the gTTS (Google Text-to-Speech) library
from gtts import gTTS
# Import the os module to interact with the operating system
import os

# Define the text you want to convert to speech
text = 'Subscribe to PSD channel!'

# Create a gTTS object with the specified text, language ('en' for English), and slow speed (False for normal speed)
file = gTTS(text=text, lang='en', slow=False)

# Save the generated speech as an MP3 file with the name 'pchannel.mp3'
file.save('pchannel.mp3')

# Use the os.system() function to start playing the generated MP3 file
# The 'start' command is used to open the file with the default system application for playing audio
os.system('start pchannel.mp3')