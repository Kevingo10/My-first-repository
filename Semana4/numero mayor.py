# Crear un programa de solcitar 3 nums al usuario y mostrar el mayor

numeros = []

for i in range(5):
    numero = float(input(f"ingrese su numero {i + 1}: "))
    numeros.append(numero)
    numero_mayor = max(numeros)
print(f"el numero mayor es: {numero_mayor}")
