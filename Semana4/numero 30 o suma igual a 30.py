# Voy a crear un codigo donde se le pida al usuario 3 numeros
# si uno es 30 o la suma de los numeros da 30 es correcto

numeros = []
for i in range(3):
    numero = int(input(f"Ingrese 3 numeros, su numero {i + 1} es: "))
    numeros.append(numero)

# Verifico si el numero es 30
if 30 in numeros:
    print("Correcto")
elif sum(numeros) == 30:
    print("Correcto")
else:
    print("Incorrecto")