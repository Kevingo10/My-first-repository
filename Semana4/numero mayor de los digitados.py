# Crear un codigo donde se le solicite x cantidad de digitos al usuario y muestre el mayor

# Creo una lista vacia para almacewnar los digitos solicitados
numeros = []

# Crear un ciclo for para solicitar x cantidad de digitos al usuario

for i in range(100):
    numero = int(input(f"Ingrese su numero {i + 1}: "))
    numeros.append(numero)
numero_mayor = max(numeros)
print(f"El numero mayor de los digitados es: {numero_mayor}") 