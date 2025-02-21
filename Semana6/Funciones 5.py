# Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
# “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

def mayusculas_minusculas(string):
    mayusculas = 0
    minusculas = 0
    for char in string:
        if char.isupper():
            mayusculas += 1
        elif char.islower():
            minusculas += 1
    return mayusculas, minusculas

mayusculas, minusculas = mayusculas_minusculas("Estoy practicando bastante Python")
print(f"mayuscaulas: {mayusculas} y minusculas: {minusculas}")

