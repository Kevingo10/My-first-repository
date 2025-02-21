# Cree un codigo que le pida un numero al usuario y muestre la suma de 
# odos los números desde 1 hasta ese número.

suma = 0
numero = int(input("Ingrese un numero: "))
for i in range(1, numero + 1):
    suma += i
print(f"La suma desde 1 hasta {numero} es: {suma}")

    