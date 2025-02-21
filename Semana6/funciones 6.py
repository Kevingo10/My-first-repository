# Cree una función que acepte un string con palabras separadas por un guión y retorne 
# un string igual pero ordenado alfabéticamente.

def palabras_alfabeticas(string):
    lista = string.split()
    lista.sort(key=str.lower)
    string = "-".join(lista)
    return string

resultado = palabras_alfabeticas("Estoy aprendiendo y Practicando mucho python con Lyfter")
print(resultado)

