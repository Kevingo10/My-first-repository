# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

def funcion_primera():
    string = "Kevin esta aprendiendo python"
    print(string)
    funcion_segunda()


def funcion_segunda():
    string2 = "En la academia Lyfter se aprende bonito"
    print(string2)

funcion_primera()


