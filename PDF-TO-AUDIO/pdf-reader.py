'''
1.pip install pyttsx3
2.pip install PyPDF2
'''

# Import necessary libraries
import pyttsx3
from PyPDF2 import PdfReader

# Initialize the PDF reader with the specified PDF file
pdf_reader = PdfReader('PDF-TO-AUDIO/xx.pdf')

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Initialize an empty string to store the extracted text
text = ""

# Iterate through each page of the PDF
for page_num in range(len(pdf_reader.pages)):
    # Extract text from the current page and append it to the 'text' variable
    text += pdf_reader.pages[page_num].extract_text()

# Clean the extracted text by stripping whitespace and replacing newline characters
clean_text = text.strip().replace('\n', ' ')

# Print the cleaned text to the console
print(clean_text)

# Save the cleaned text as an audio file (MP3 format)
speaker.save_to_file(clean_text, 'PDF-TO-AUDIO/introduction.mp3')

# Run the text-to-speech engine to convert text to speech and save it as an audio file
speaker.runAndWait()

# Stop the text-to-speech engine
speaker.stop()
