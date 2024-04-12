import speech_recognition as sr
from gtts import gTTS
import playsound
import os


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'temp.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def teach():
    speak("What do you want to do with it?")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

def codeeteach():

def writechanges():
    f = open("func.py", 'w')
