# Cree una calculadora por linea de comando. Esta debe de tener un número actual, 
# y un menú para decidir qué operación hacer con otro número

def calculadora():
    num_actual = 0
    while True:
        print(f"Numero actual: {num_actual}")
        print("Seleccione una opcion: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Borrar resultado")
        print("6. Salir")


        try:
            option = int(input("Ingrese el numero de la operacion deseada: "))
        except ValueError:
            print(" Error, ingrese una opcion valida:")
            continue 


        if option == 6:
            print("Programa finalizado")
            break


        if option == 5:
            num_actual = 0
            print("El resultado se a borrado")
            continue


        try:
            numero = float(input("Ingrese un numero para la operacion matematica: "))
        except ValueError:
            print("Error: favor ingresar un numero valido")
            continue


        if option == 1:
            num_actual += numero
            print(f"El nuevo numero actual es: {num_actual}")
            
        
        elif option == 2:
            num_actual -= numero
            print(f"El nuevo numero actual es : {num_actual}")


        elif option == 3:
            num_actual *= numero
            print(f"El nuevo numero actual es: {num_actual}")

        
        elif option == 4:
            if numero == 0:
                print("No se puede dividir entre 0")
            else:
                num_actual /= numero
                print(f"El nuevo numero actual es: {num_actual}")
        else:
            print("Opcion no valida, elija una opcion entre el 1 y el 6")


calculadora()
        
        
