# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y
# guarde en otro archivo los mismos nombres ordenados alfabéticamente.

# Paso 1: Open file 'canciones.txt' in reading mode
with open("C:/Users/USUARIO/OneDrive/Desktop/Python/canciones.txt", "r", encoding="utf-8") as archivo:
    # Paso 2: read songs line by line and add them to a list
    songs = [linea.strip() for linea in archivo if linea.strip()]
    print(songs)

# Paso 3: put songs in alphabetic 
songs.sort()

# Paso 4: save songs in a new file called 'canciones_ordenadas.txt'
with open("canciones_ordenadas.txt", "w", encoding="utf-8") as file_out:
    for song in songs:
        file_out.write(song + "\n")

print("Las canciones han sido ordenadas y guardadas en 'canciones_ordenadas.txt'.")






