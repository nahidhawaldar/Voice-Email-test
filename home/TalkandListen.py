import pyttsx3
from gtts import gTTS
import speech_recognition as sr
# this speaks the text sent as a parameter
def talk(text):
    engine = pyttsx3.init()  # text to speech initialized.Engine speaks the text out
    engine.say(text)
    engine.runAndWait()

# Speak Function Not Working Properly
def listen():
    print('INSIDE listen FNCTION')
    listener = sr.Recognizer()  # to understand what the user is saying.
    try:
        with sr.Microphone() as source:  # laptop's mic is the source for speech.
            print('Listening...')
            talk('Now Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)  # speech to text function
            print(info, '\n')
            return info
    except:
        pass