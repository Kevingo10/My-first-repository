# Cree un programa que elimine todos los números impares de una lista.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
numeros_sin_impares = [num for num in my_list if num % 2 == 0]
print(numeros_sin_impares)
