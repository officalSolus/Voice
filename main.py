import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import webbrowser

import getText
import teach


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'C:/Users/Solus/Desktop/Voice/temp.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


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


def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")


def open_website(url):
    webbrowser.open(url)


def ai(): #NOT PROPERLY DONE. WAS JUST TESTING
    speak("Hello! How can I help you?")
    while True:
        query = listen()
        if "stop" in query:
            speak("Goodbye!")
            break
        elif "time" in query:
            current_time = get_time()
            speak(f"The current time is {current_time}")
        elif "open" in query:
            words = query.split()
            website = words[words.index("open") + 1]
            speak(f"Opening {website}")
            open_website(f"{website}")
        else:
            response = "I'm sorry, I don't understand that command. Do you want to teach me how to respond to that?"
            a = listen()
            if a == 'yes':
                teach.teach()
            else:
                speak(getText.getResult(a))
            speak(response)


ai()
