import wikipedia


def getInfo(title: str):
    content = wikipedia.summary(title, sentences=2, auto_suggest=False)
    return content


print(getInfo("double slit"))
