with open("notas.txt", "a", encoding="utf-8") as file:
    while True:
        lineas = input("introduzca texto o salir para terminar: ")
        if lineas == "salir":
            break
        file.write(lineas + "\n")
print("programa finalizado")
