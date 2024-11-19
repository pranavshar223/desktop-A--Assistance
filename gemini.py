import google.generativeai as genai
import pathlib
import textwrap
from IPython.display import display, Markdown
import os
from speak import speak

# Set up the API key
os.environ["API_KEY"] = 'AIzaSyBkPNNj4QODv69jYFBguNKQWB7RXgScNxY'
genai.configure(api_key=os.environ["API_KEY"])

# Define model and generation function
model = genai.GenerativeModel('gemini-1.5-flash-latest')
def GeminiAi(text):
    response = model.generate_content(text)
    return response.text

# Markdown formatting function
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Use the function and display the result
exit =1
while(exit):
    text = input(" NOVA : ")
    response_text = GeminiAi(text)
    result = to_markdown(response_text)
    display(response_text)
    exit=int(input("exit->0  continue -> 1"))
