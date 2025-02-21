buscar = input("Busca una palabra: ")
remplazar = input("Remplaza la palabra por: ")


with open("notas.txt", "r", encoding="utf-8") as file:
    contenido = file.read()
    


contenido_modificado = contenido.replace(buscar, remplazar)


with open("notas.txt", "w", encoding="utf-8") as file:
    file.write(contenido_modificado)


print("Remplazo completado")

