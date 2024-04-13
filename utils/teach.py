import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import utils.getText as getText


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
    try:
        print("Recognizing...")
        change = recognizer.recognize_google(audio)
        print(f"You said: {change}")
        codeTeach(change)
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""


def codeTeach(change: str):
    towrite = getText.getResult(change)
    f = open("func.py", 'a')
    f.write(towrite)
