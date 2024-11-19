import pyttsx3
import speech_recognition as sr




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('pitch', 2.8)  # Adjust the pitch value
engine.setProperty('rate', 193)
engine.setProperty('volume', 1)
def speak(text):
    print(f"Cortana: {text}")  # Debugging statement
    engine.say(text)
    engine.runAndWait()


import win32com.client

# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("Hello, I am speaking using Windows SAPI5!")

text="hi this is python"
speak(text)