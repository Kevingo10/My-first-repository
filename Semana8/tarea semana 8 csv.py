# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.

import csv

# List to add videogames
videgames_list = []

# start message
print("Ingrese los datos de los videojuegos o escriba 'salir' en el nombre para terminar.")

# cicle to join data
while True:
    name = input("Ingrese el nombre del videojuego: ")
    if name.lower() == "salir":
        break
    gender = input("Ingrese el género del videojuego: ")
    developer = input("Ingrese el desarrollador del videojuego: ")
    clasification_ESRB = input("Ingrese la clasificación ESRB del videojuego: ")
    
    # Add a dictionary with list´s data
    videogame = {
        "Nombre": name,
        "Genero": gender,
        "Desarrollador": developer,
        "Clasificaion ESRB": clasification_ESRB
    }
    videgames_list.append(videogame)

# headers file CSV
videogame_headers = ["Nombre", "Genero", "Desarrollador", "Clasificaion ESRB"]

# function to save csv
def saveCsv(filename, data, headers):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(data)

# save data if there is videogames on list
if videgames_list:
    saveCsv("videogames.csv", videgames_list, videogame_headers)
    print("Los datos se han guardado en 'videogames.csv'.")
else:
    print("No se ingresaron videojuegos.")





    
