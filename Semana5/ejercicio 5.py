# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, 
# seguido del numero ingresado más alto.

lista = []
numeros = input("Vamos a ver los numeros ingresados y seguidos el mayor, dale enter para continuar ")
for i in range(10):
    numero = int(input(f"Ingrese 10 numeros aleatorios {i + 1}: "))
    lista.append(numero)
    maximo = max(lista)
print(f"{lista} el numero mayor es: {maximo}")
