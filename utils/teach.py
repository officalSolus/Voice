import speech_recognition as sr
import pyttsx3
import utils.getText as getText

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)


def speak(text):
    engine.say(text)
    engine.runAndWait()


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
