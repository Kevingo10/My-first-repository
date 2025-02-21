# Crear un codigo donde se le pida al usuario x cantidad de numeros y muestre la suma de todos

numeros = []
for i in range(100):
    numero = int(input(f"Ingrese su numero {i + 1}: "))
    numeros.append(numero)
total = sum(numeros)
print(f"la suma de los digitos ingresados es: {total}")