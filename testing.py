import utils.func as func


def initialSetup():
    f = open("functions.txt", "r")
    a = f.read()
    possible = a.split()
    return possible


initialSetup()
possible = initialSetup()
query = "what is the time"
print(possible)
for x in possible:
    if x in query:
        function = getattr(func, x)
        function()
