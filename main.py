import speech_recognition as sr
import playsound
import os
import pyttsx3

import utils.getText as getText
import utils.teach as teach
import utils.func as func

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)

def initialSetup():
    f = open("functions.txt", "r")
    a = f.read()
    possible = a.split()
    return possible


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""


def ai(condition: bool):
    possible = initialSetup()
    while condition:
        query = listen()
        try:
            for x in possible:
                if x in query:
                    function = getattr(func, x)
                    outp = function()
                    speak(outp)
                    ai(True)
                elif "create" and "function" in query:
                    teach.codeTeach(query)
                    ai(True)
                elif "stop" == query or "exit" == query:
                    condition = False
            raise ValueError("")
        except ValueError:
            try:
                speak(getText.getResult(query))
            except KeyError:
                ai()

ai(True)
