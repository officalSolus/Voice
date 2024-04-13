import webbrowser
import datetime

def website(url):
    webbrowser.open(url)


def time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

